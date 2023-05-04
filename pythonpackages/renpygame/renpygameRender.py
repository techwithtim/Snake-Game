import renpy.exports as renpy


class Render(renpy.Render):
    """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L586"""

    def __init__(
        self,
        width: int,
        height: int,
    ):
        # renpy.Render init
        super().__init__(width, height)
        # * Render properties, will come set in super().__init__

        self.renpygame_render = None

    @property
    def mark(self):
        return super().mark

    @property
    def cache_killed(self):
        return super().cache_killed

    @property
    def killed(self):
        return super().killed

    @property
    def width(self) -> int:
        """must be int"""
        return int(super().width)

    @property
    def height(self) -> int:
        """must be int"""
        return int(super().height)

    @property
    def layer_name(self):
        return super().layer_name

    @property
    def children(self):
        return super().children

    @property
    def forward(self):
        return super().forward

    @property
    def reverse(self):
        return super().reverse

    @property
    def alpha(self):
        return super().alpha

    @property
    def over(self):
        return super().over

    @property
    def nearest(self):
        return super().nearest

    @property
    def focuses(self):
        return super().focuses

    @property
    def pass_focuses(self):
        return super().pass_focuses

    @property
    def focus_screen(self):
        return super().focus_screen

    @property
    def render_of(self):
        return super().render_of

    @property
    def xclipping(self):
        return super().xclipping

    @property
    def yclipping(self):
        return super().yclipping

    @property
    def modal(self):
        return super().modal

    @property
    def text_input(self):
        return super().text_input

    @property
    def parents(self):
        return super().parents

    @property
    def depends_on_list(self):
        return super().depends_on_list

    @property
    def operation(self):
        return super().operation

    @property
    def operation_complete(self):
        return super().operation_complete

    @property
    def operation_alpha(self):
        return super().operation_alpha

    @property
    def operation_parameter(self):
        return super().operation_parameter

    @property
    def surface(self):
        return super().surface

    @property
    def alpha_surface(self):
        return super().alpha_surface

    @property
    def half_cache(self):
        return super().half_cache

    @property
    def mesh(self):
        return super().mesh

    @property
    def shaders(self):
        return super().shaders

    @property
    def uniforms(self):
        return super().uniforms

    @property
    def properties(self):
        return super().properties

    @property
    def cached_texture(self):
        return super().cached_texture

    @property
    def cached_model(self):
        return super().cached_model

    @property
    def loaded(self):
        return super().loaded

    def blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
        """render.blit(): https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L778"""
        if hasattr(source, "renpygame_render") and source.renpygame_render:
            source = source.renpygame_render
        return super().blit(source, pos, focus, main, index)

    def subpixel_blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
        return super().subpixel_blit(source, pos, focus, main, index)

    def absolute_blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
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

    def add_focus(
        self, d, arg=None, x=0, y=0, w=None, h=None, mx=None, my=None, mask=None
    ):
        return super().add_focus(d, arg, x, y, w, h, mx, my, mask)

    def take_focuses(self, cminx, cminy, cmaxx, cmaxy, transform, screen, focuses):
        return super().take_focuses(
            cminx, cminy, cmaxx, cmaxy, transform, screen, focuses
        )

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

    def place(
        self,
        d,
        x=0,
        y=0,
        width=None,
        height=None,
        st=None,
        at=None,
        render=None,
        main=True,
    ):
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

    @property
    def renpygame_render(self) -> renpy.Render:
        """if set will be used during blit() instead of using the parent class.
        This is used during conversions and is useful to prevent errors.
        # TODO: instead of using this variable during the conversion, one could set all the variables to the old element in the new
        """
        return self._original_render

    @renpygame_render.setter
    def renpygame_render(self, value: renpy.Render):
        self._original_render = value

    def get_width(self) -> int:
        width, _ = self.get_size()
        return int(width)

    def get_height(self) -> int:
        _, height = self.get_size()
        return int(height)

    def import_renpy_render(self, renpy_render: renpy.Render):
        self = renpy_render
