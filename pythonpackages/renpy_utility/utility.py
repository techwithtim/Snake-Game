from typing import Optional

__all__ = [
    "isNullOrEmpty",
    "IsNullOrWhiteSpace",
]


def isNullOrEmpty(item: Optional[str]) -> bool:
    if not item:
        return True
    return False


def IsNullOrWhiteSpace(item: Optional[str]) -> bool:
    if not item or item.isspace():
        return True
    return False


def os_path_join(a: str, b: str) -> str:
    return a + "/" + b
