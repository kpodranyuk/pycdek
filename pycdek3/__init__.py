from .client import AbstractOrder, AbstractOrderLine, Client, TestClient
VERSION = (0, 1, 0)


def get_version():
    return '.'.join(map(str, VERSION))


__version__ = get_version()
