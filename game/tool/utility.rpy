init -999 python:
    def isNullOrEmpty(item: str) -> bool:
        if not item:
            return True
        return False

    def IsNullOrWhiteSpace(item: str) -> bool:
        if not item or item.isspace():
            return True
        return False

label set_background(img):
    scene expression (img) as bg
