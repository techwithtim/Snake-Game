# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    image bg m64 = "m64.jpg"
    image eileen happy = "eileen_happy.png"

    # Declare characters used by this game.
    $ e = Character('Eileen', color="#c8ffc8")

    $ import aliens
    

# The game starts here.
label start:

    scene bg m64
    show eileen happy at left
    
    show screen alpha_magic
    
    e "Welcome!"

    e "You're here to defend the moon from invaders from the M-64 galaxy."

    e "You can move your van back and forth with the arrow keys, and then press space to fire a missile."

    e "Good luck!"

label retry:

    $ renpy.free_memory()
    $ score = aliens.main()

    # This eats up any remaining keypresses.
    $ renpy.pause(.1)
    
    e "You shot down %(score)d aliens."

    if score > 10:

        e "Not bad!"

    menu:

        "Would you like to try again?"

        "Sure.":

            "Okay, get ready..."

            jump retry

        "No thanks.":

            pass

    e "No problem."

    e "This game was based off one of the examples that came with pygame."

    e "It shows how pygame games can be integrated with Ren'Py."

    e "Thank you for playing."

    return


        



screen alpha_magic:
    add Appearing("background.gif", 100, 200):
        xalign 0.5
        yalign 0.5




init python:

    import math

    class Appearing(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Appearing, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            # The distance at which the child will become fully opaque, and
            # where it will become fully transparent. The former must be less
            # than the latter.
            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            # The alpha channel of the child.
            self.alpha = 0.0

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            # Create a transform, that can adjust the alpha channel of the
            # child.
            t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

            # Base on the distance, figure out an alpha.
            if distance <= self.opaque_distance:
                alpha = 1.0
            elif distance >= self.transparent_distance:
                alpha = 0.0
            else:
                alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # If the alpha has changed, trigger a redraw event.
            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]
