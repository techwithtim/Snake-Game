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
