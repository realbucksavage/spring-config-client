import base64
import logging
import sys

import requests

from spring_config import Singleton, ClientConfiguration
from spring_config.utils import str_is_blank

logging.getLogger(__name__).addHandler(logging.NullHandler())


class SpringConfigClient(metaclass=Singleton):
    def __init__(self, client_config: ClientConfiguration):

        address = client_config.get_address()
        branch = client_config.get_branch()
        app_name = client_config.get_app_name()
        profile = client_config.get_profile()

        _request_url = f"{address}/{branch}/{app_name}-{profile}.json"
        _request_headers = {"Authorization": client_config.get_authn_header()}

        logging.debug(f"Requesting: {_request_url}")

        try:
            response = requests.get(_request_url, headers=_request_headers)

            if response.status_code == 200:
                self._config = response.json()
            else:
                raise Exception(
                    "Failed to acquire configuration",
                    f"HTTP Response Code : {response.status_code}",
                )

        except requests.RequestException as err:
            logging.exception(f"Cannot send a request to {_request_url}", err)

            # Exit the application
            sys.exit(1)

    def get_config(self):
        return self._config

    def get_attribute(self, value: str, delim: str = "."):
        """Get attribute from configurations.
        Use <dot> to define a path on a key tree.

        https://github.com/amenezes/config-client/blob/master/config/spring.py#L100
        """
        key_list = value.split(delim)
        logging.debug(f"Key attribute: {key_list}")

        attribute_content = self._config.get(key_list[0])
        logging.debug(f"Attribute content: {attribute_content}")

        for key in key_list[1:]:
            attribute_content = attribute_content.get(key)

        logging.debug(f"Configuration getted: {attribute_content}")

        return attribute_content

    def get_keys(self):
        """List all keys from configuration retrieved."""
        return self._config.keys()
