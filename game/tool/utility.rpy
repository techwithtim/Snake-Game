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

label set_background(img):
    scene expression (img) as bg
