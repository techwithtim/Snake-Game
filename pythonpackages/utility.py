__all__ = [
    "isNullOrEmpty",
    "IsNullOrWhiteSpace",
]


def isNullOrEmpty(item: str) -> bool:
    if not item:
        return True
    return False


def IsNullOrWhiteSpace(item: str) -> bool:
    if not item or item.isspace():
        return True
    return False


def flatten(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args


def os_path_join(a: str, b: str) -> str:
    return a + "/" + b
