init python:
    from pythonpackages.renpygame.rect import Rect
    from pythonpackages.renpygame.sprite import Sprite

screen rect(
    left = 0,
    top = 0,
    width = 0,
    height = 0,
    img = None,
):
    add Rect(left = left, top = top, width = width, height = height, image = img)

screen sprite(
    left = 0,
    top = 0,
    width = 0,
    height = 0,
    img = None,
):
    add Sprite(left = left, top = top, width = width, height = height, image = img)
