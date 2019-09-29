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

The very basic usage of this library looks like this:

```python
from spring_config import ClientConfigurationBuilder
from spring_config.client import SpringConfigClient

config = ClientConfigurationBuilder().app_name("test-application").build()

c = SpringConfigClient(config)
c.get_config()
```

By default, `ClientConfigurationBuilder` builds a `ClientConfiguration` object with server address and application profile set to `http://localhost:8888` and `development`. These can be changed like this:

Here are some examples:

```python
# Fetch from http://someserver.com using profile "development"
config = (
    ClientConfigurationBuilder()
    .app_name("test-application")
    .address("http://someserver.com")
    .build()
)

# Fetch from http://someserver.com using profile "production"
config = (
    ClientConfigurationBuilder()
    .app_name("test-application")
    .address("http://someserver.com")
    .profile("production")
    .build()
)
```

### Authentication

If your configuration server requires to use basic authentication, you can create the client configuration like this:

```python
from spring_config import ClientConfigurationBuilder

config = (
    ClientConfigurationBuilder()
    .app_name("test-application")
    .authentication(("username", "password"))
    .build()
)
```

### Configuration options

The `ClientConfigurationBuilder` allow controlling these parameters.

- Application Name : `app_name("some-app")` - Default `None`, required.
- Server Address : `address("http://some-server")` - Default `http://localhost:8888`, optional.
- Profile : `profile("production")` - Default `development`, optional.
- Branch : `branch("devel/0.1")` - Default `master`, optional.

## Requesting features

Please use the [issues section](https://github.com/realbucksavage/spring-config-client/issues) to request new features and I will try to take out my time to work on them. Contributions in any sorts are always welcome :)