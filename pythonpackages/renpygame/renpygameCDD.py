import renpy.exports as renpy

# https://www.renpy.org/doc/html/cdd.html


class Render(renpy.Render):
    """https://github.com/renpy/renpy/blob/fb803ea05cca1b933f18d51fb0398d9545879af9/renpy/display/render.pyx#L586"""

    def __init__(
        self,
        width: int,
        height: int,
    ):

        # renpy.Render init
        super().__init__(width, height)

    def get_width(self) -> int:
        width, _ = self.get_size()
        return int(width)

    def get_height(self) -> int:
        _, height = self.get_size()
        return int(height)
