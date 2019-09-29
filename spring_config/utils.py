class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

    def discard_singleton(cls):
        if cls in cls._instances:
            del cls._instances[cls]


def str_is_blank(string: str) -> bool:
    return bool(not string or not string.strip())
