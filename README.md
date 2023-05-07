# Renpygame

**IMPORTANT**: This is a continuation of a project not mine, abandoned from 2008 [Renpygame](https://renpy.org/wiki/renpy/frameworks/Renpygame) (not working).

----

Renpygame is a framework that allows pygame games to be integrated with Ren'Py. It's intended for people who are capable programmers. Currently compared to 2008, it is not possible to directly use the [pygame_sdl2](https://github.com/renpy/pygame_sdl2) library, especially to "draw".

The idea is to create a library that uses [pygame_sdl2](https://github.com/renpy/pygame_sdl2) and overrides functions that can be handled by the [renpy](https://github.com/renpy/renpy) library.

The big problem is that the mode for drawing is very different. The only way I found was to use [CDD](https://www.renpy.org/doc/html/cdd.html) and use that events to draw and update an element.

Use of events to draw limits a lot -> you can't create loops to update a renpy.Displayable -> that's why you can't copy and paste a game, but modify it slightly.

## Why use pygame-renpygame and not renpy-CDD?

pygame-renpygame's pros:

- You can use pygame and renpy functions
- huge number of minigames on github
- popularity (pygame is also often used in universities)
- typification (I am endeavouring to add the type everywhere)

renpy's pros:

- durability (CDD is developed by the same developer as renpy)

## Performance

**Important**: I am currently trying to solve performance problems in animations using CDD. for the time being i will not evaluate this problem because it is only a problem of incorrect implementation.

(I don't made any tests for now) Renpygame use CDD for draw and renpy for open a file, but I use a typification and is a external library. So, the performance is the same as renpy, excluding possible implementation errors.

## Instructions

## Supported Modules

A good number of functions should already work even if they have not yet been tested

- [ ] renpygame.color
- [ ] renpygame.constants (Still to be tested, should already be working)
- [ ] renpygame.cursors (Still to be tested, should already be working)
- [ ] renpygame.display (Incomplete)
- [x] renpygame.display.Surface
- [ ] renpygame.draw
- [ ] renpygame.event (Still to be tested, should already be working)
- [ ] renpygame.font
- [ ] renpygame.image (Incomplete)
- [ ] renpygame.joystick
- [ ] renpygame.key (Incomplete)
- [ ] renpygame.locals (Still to be tested, should already be working)
- [ ] renpygame.mixer (Incomplete)
- [ ] renpygame.mixer.music (Incomplete)
- [ ] renpygame.mouse (Still to be tested, should already be working)
- [x] renpygame.rect
- [ ] renpygame.sprite (Incomplete)
- [ ] renpygame.time (Still to be tested, should already be working)
- [ ] renpygame.transform (Incomplete)
