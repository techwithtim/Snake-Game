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

    def blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        return super().blit(source, pos, focus, main, index)

    def subpixel_blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        return super().subpixel_blit(source, pos, focus, main, index)

    def absolute_blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        return super().absolute_blit(source, pos, focus, main, index)

    def get_size(self) -> tuple[int, int]:
        return super().get_size()

    def render_to_texture(self, alpha=True):
        return super().render_to_texture(alpha)

    def subsurface(self, rect, focus=False):
        return super().subsurface(rect, focus)

    def depends_on(self, source, focus=False):
        return super().depends_on(source, focus)

    def kill_cache(self):
        return super().kill_cache()

    def kill(self):
        return super().kill()

    def add_focus(self, d, arg=None, x=0, y=0, w=None, h=None, mx=None, my=None, mask=None):
        return super().add_focus(d, arg, x, y, w, h, mx, my, mask)

    def take_focuses(self, cminx, cminy, cmaxx, cmaxy, transform, screen, focuses):
        return super().take_focuses(cminx, cminy, cmaxx, cmaxy, transform, screen, focuses)

    def focus_at_point(self, x, y, screen):
        return super().focus_at_point(x, y, screen)

    def main_displayables_at_point(self, x, y, layers, depth=None):
        return super().main_displayables_at_point(x, y, layers, depth)

    def is_pixel_opaque(self, x, y):
        return super().is_pixel_opaque(x, y)

    def fill(self, color):
        return super().fill(color)

    def canvas(self):
        return super().canvas()

    def screen_rect(self, sx: float, sy: float, transform: list[list[int]]):
        return super().screen_rect(sx, sy, transform)

    def place(self, d, x=0, y=0, width=None, height=None, st=None, at=None, render=None, main=True):
        return super().place(d, x, y, width, height, st, at, render, main)

    def zoom(self, xzoom, yzoom):
        return super().zoom(xzoom, yzoom)

    def add_shader(self, shader):
        return super().add_shader(shader)

    def add_uniform(self, name, value):
        return super().add_uniform(name, value)

    def add_property(self, name, value):
        return super().add_property(name, value)

    # my methods

    def get_width(self) -> int:
        width, _ = self.get_size()
        return int(width)

    def get_height(self) -> int:
        _, height = self.get_size()
        return int(height)
