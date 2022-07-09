init -999 python:
    def isNullOrEmpty(item: str):
        if not item or item.isspace():
            return True
        return False
