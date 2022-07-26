init -999 python:
    def isNullOrEmpty(item: str) -> bool:
        if not item:
            return True
        return False

    def IsNullOrWhiteSpace(item: str) -> bool:
        if not item or item.isspace():
            return True
        return False

    def null_or_image(s):
        """It checks for the presence of an image, in case it is not there it returns a null value. Possible use: avoid mistakes in the management of clothes."""
        # s = renpy.substitute(s)
        if renpy.has_image(s):
            return s
        elif renpy.list_files(s):
            return s
        else:
            return Null()
    config.displayable_prefix['check'] = null_or_image

    def compare(a= 0, b= 0) -> int:
        if a is None and b is None:
            return 0
        elif b is None:
            return 1
        elif a is None:
            return -1
        return a - b

    def isGreaterThan(a= 0, b= 0) -> bool:
        return compare(a, b) > 0

label set_background(img):
    scene expression (img) as bg
