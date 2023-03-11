import json

from pythonpackages.renpy_custom_log import *

__all__ = [
    "updateFlags",
    "getFlags",
    "setFlags",
]


def updateFlags(flags: dict[str, bool], flag_keys: list[str]):
    """update flags by making it with the same elements of flag_keys. in case you have to add them set them as False"""
    # check if there are less elements than flag_keys
    # in case you add them set with False
    for x in flag_keys:
        if (not (x in flags)):
            flags[x] = False
    # check if there are more elements than flag_keys
    # in case it eliminates them
    flags_to_del = []
    for x in flags:
        if (not (x in flag_keys)):
            flags_to_del.append(x)
    for x in flags_to_del:
        del flags[x]
    del flags_to_del
    return flags


def getFlags(flag_id: str, flags: dict[str, bool]) -> bool:
    """returns the value of the flag_id in flags"""
    if (flag_id in flags):
        return flags[flag_id]
    else:
        return False


def setFlags(flag_id: str, value: bool, flags: dict[str, bool]):
    flags[flag_id] = value
    return
