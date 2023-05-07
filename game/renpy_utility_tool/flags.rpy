init python:
    import pythonpackages.renpy_utility.flags as myFlags

# flags are Boolean values, a good use is for example in quests to know quickly if MC has the possibility to do a certain thing, after unlocking it somehow.
# has the same alements as flag_keys, all set as False
# I suggest to leave it empty and add the elements only if it is an initial value and set as True
default flags = {}
define flag_keys = [
]

init python:
    def update_flags():
        """update flags by making it with the same elements of flag_keys. in case you have to add them set them as False"""
        return myFlags.update_flags(flags, flag_keys)

    def get_flags(flag_id: str) -> bool:
        """returns the value of the flag_id in flags"""
        return myFlags.get_flags(flag_id, flags)

    def set_flags(flag_id: str, value: bool):
        return myFlags.set_flags(flag_id, value, flags)
