# IMPORTANT: insert updateFlags() in start or before using flags
# flags are Boolean values, a good use is for example in quests to know quickly if MC has the possibility to do a certain thing, after unlocking it somehow.
# has the same alements as flag_keys, all set as False
# I suggest to leave it empty and add the elements only if it is an initial value and set as True
default flags = {}
define flag_keys = [
    # Block all actions with check_block_spendtime
]

init python:
    def updateFlags(flags: dict[str, bool], flag_keys: list[str]):
        """update flags by making it with the same elements of flag_keys. in case you have to add them set them as False"""
        # check if there are less elements than flag_keys
        # in case you add them set with False
        for x in flag_keys:
            if ((x in flags) == False):
                flags[x] = False
        # check if there are more elements than flag_keys
        # in case it eliminates them
        flags_to_del = []
        for x in flags:
            if ((x in flag_keys) == False):
                flags_to_del.append(x)
        for x in flags_to_del:
            del flags[x]
        del flags_to_del
        return flags

    def getFlags(flag_id: str) -> bool:
        """returns the value of the flag_id in flags"""
        if (not flag_id in flags):
            updateFlags(flags = flags, flag_keys = flag_keys)
            if (not flag_id in flags):
                renpy.log("Error(getFlags): in flags is not there flag_id: "+flag_id)
            else:
                return False
        return flags[flag_id]
