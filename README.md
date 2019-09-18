# spring-config-client

A Python client for [Spring Config Server](https://spring.io/projects/spring-cloud-config).

This library is inspired by [amenezes/config-client](https://github.com/amenezes/config-client) and is essentially a toned-down fork that I customized to fit my own needs.

## Project goals

- [x] Provide a basic client
- [x] Provide basic authentication
- [ ] Add support for CloudFoundry

## Installation

Install using `pip`

```shell
$ pip install spring-config-client
```

## Usage

The very very usage of this library can be implemented like this:

```python
from spring_config.client import SpringConfigClient

c = SpringConfigClient(app_name="test-application")
c.get_config()
```

By default, this package tries to fetch configuration from `http://localhost:8888` using `development` profile. These parameters can be changed by passing them into the `SpringConfigClient` constructor.

Here are some examples:

```python
# Fetch from http://someserver.com using profile "development"
c = SpringConfigClient(address="http://someserver.com", app_name="some_app")

# Fetch from http://someserver.com using profile "production"
c = SpringConfigClient(
    address="http://someserver.com",
    app_name="some_app",
    profile="production"
)
```

### Using with Flask

```python
from flask import Flask
from spring_config import client

config_client = client.SpringConfigClient(...)

app = Flask(...)

# ... continued.
```

## Requesting features

Please use the [issues section](https://github.com/realbucksavage/spring-config-client/issues) to request new features and I will try to take out my time to work on them. Contributions in any sorts are always welcome :)