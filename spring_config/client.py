import logging

import requests

from spring_config import ClientConfiguration

logging.getLogger(__name__).addHandler(logging.NullHandler())


class SpringConfigClient:
    def __init__(self, client_config: ClientConfiguration):

        address = client_config.get_address()
        branch = client_config.get_branch()
        app_name = client_config.get_app_name()
        profile = client_config.get_profile()

        _request_url = f"{address}/{branch}/{app_name}-{profile}.json"
        _request_headers = {"Authorization": client_config.get_authn_header()}

        logging.debug(f"Requesting: {_request_url}")

        response = requests.get(_request_url, headers=_request_headers)

        if response.status_code == 200:
            self._config = response.json()
        else:
            raise Exception(
                "Failed to acquire configuration",
                f"HTTP Response Code : {response.status_code}",
            )

    def get_config(self):
        return self._config

    def get(self, key: str):
        """
        This method exists as an alias to get_attribute to maintain compatibility with dict methods. Invoking `get` is
        identical to invoking `get_attributes(key, ".")`.

        :param key: The key of config value to find.
        :return: The config value or `None`
        """
        return self.get_attribute(key, ".")

    def get_attribute(self, key: str, delim: str = "."):
        """
        Find a configuration value identified by `key`. Nested values can be searched by combining their keys by `delim`.

        Using the following configuration as an example:
        ```
        # some_config_value: xyz
        # some:
        #    nested:
        #        value: abc

        # returns xyz
        cfg.get_attribute("some_config_value")

        # returns abc
        cfg.get_attribute("some.nested.value")
        ```
        """
        key_list = key.split(delim)
        logging.debug(f"Key attribute: {key_list}")

        attribute_content = self._config.get(key_list[0])
        logging.debug(f"Attribute content: {attribute_content}")

        for key in key_list[1:]:
            attribute_content = attribute_content.get(key)

        logging.debug(f"Configuration getted: {attribute_content}")

        return attribute_content

    def get_keys(self):
        """
        List all keys from configuration retrieved.
        """
        return self._config.keys()
