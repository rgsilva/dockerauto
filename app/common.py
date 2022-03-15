import os

def from_host(path):
    host_prefix = os.environ["HOST_PREFIX"] if "HOST_PREFIX" in os.environ else ""
    return host_prefix + path


def docker_sock():
    if "DOCKER_SOCK" in os.environ:
        return os.environ["DOCKER_SOCK"]

    raise MissingParameterError("Missing DOCKER_SOCK environment variable")


class MissingParameterError(Exception):
    pass