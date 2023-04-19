from typing import Callable
import renpy.exports as renpy

# https://www.renpy.org/doc/html/cdd.html


class Render(renpy.Render):
    """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L586"""

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


# class Canvas(renpy.Canvas):
#     """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1610"""

#     def __init__(self, surf):

#         # renpy.Canvas init
#         super().__init__(surf)

#     def rect(self, color, rect, width=0):
#         return super().rect(color, rect, width)

#     def polygon(self, color, pointlist, width=0):
#         return super().polygon(color, pointlist, width)

#     def circle(self, color, pos, radius, width=0):
#         return super().circle(color, pos, radius, width)

#     def ellipse(self, color, rect, width=0):
#         return super().ellipse(color, rect, width)

#     def arc(self, color, rect, start_angle, stop_angle, width=1):
#         return super().arc(color, rect, start_angle, stop_angle, width)

#     def line(self, color, start_pos, end_pos, width=1):
#         return super().line(color, start_pos, end_pos, width)

#     def lines(self, color, closed, pointlist, width=1):
#         return super().lines(color, closed, pointlist, width)

#     def aaline(self, color, startpos, endpos, blend=1):
#         return super().aaline(color, startpos, endpos, blend)

#     def aalines(self, color, closed, pointlist, blend=1):
#         return super().aalines(color, closed, pointlist, blend)

#     def get_surface(self):
#         return super().get_surface()


class RenpyGameSurface(renpy.Displayable):
    """https://www.renpy.org/doc/html/cdd.html
    render(): https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L170"""

    def __init__(
        self,
            game_lambda: Callable[[int, int, float, float], Render],
            **kwargs
    ):
        # renpy.Displayable init
        super(RenpyGameSurface, self).__init__(**kwargs)

        self.game_lambda = game_lambda

    def render(self, width: int, height: int, st: float, at: float) -> Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L170"""
        # # Create the render we will return.
        # render = renpy.Render(width, width)

        # # Create a render from the child.
        # child_render = renpy.render(renpy.displayable(
        #     "alien3.gif"), width, height, st, at)

        # # Blit (draw) the child's render to our render.
        # render.blit(child_render, child_render.get_size())

        # # Return the render.
        # return render

        render = self.game_lambda(width, height, st, at)
        return render

    @property
    def game_lambda(self) -> Callable[[int, int, float, float], Render]:
        return self._game_lambda

    @game_lambda.setter
    def game_lambda(self, value: Callable[[int, int, float, float], Render]):
        self._game_lambda = value
