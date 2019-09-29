import base64
from spring_config.utils import str_is_blank


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

    def discard_singleton(cls):
        if cls in cls._instances:
            del cls._instances[cls]


class ClientConfiguration:
    def __init__(
        self,
        address: str,
        app_name: str,
        profile: str,
        branch: str,
        authentication: tuple = ("", ""),
    ):
        self._address = address
        self._app_name = app_name
        self._profile = profile
        self._branch = branch

        _uname, _passw = authentication
        _basic = base64.b64encode(f"{_uname}:{_passw}".encode())
        self._authn_header = f"Basic {_basic.decode()}"

    def get_address(self) -> str:
        return self._address

    def get_branch(self) -> str:
        return self._branch

    def get_app_name(self) -> str:
        if str_is_blank(self._app_name):
            raise ValueError("Config Error: app_name cannot be blank")

        return self._app_name

    def get_profile(self) -> str:
        return self._profile

    def get_authn_header(self) -> str:
        return self._authn_header


class ClientConfigurationBuilder:

    _app_name = None
    _branch = "master"
    _address = "http://localhost:8888"
    _profile = "development"
    _authn = ("", "")

    def app_name(self, app_name: str):
        self._app_name = app_name
        return self

    def address(self, address: str):
        if not str_is_blank(address):
            self._address = address
        return self

    def profile(self, profile: str):
        if not str_is_blank(profile):
            self._profile = profile
        return self

    def authentication(self, authn_details: tuple):
        self._authn = authn_details
        return self

    def branch(self, branch: str):
        if not str_is_blank(branch):
            self._branch = branch

        return self

    def build(self) -> ClientConfiguration:
        return ClientConfiguration(
            self._address, self._app_name, self._profile, self._branch, self._authn
        )
