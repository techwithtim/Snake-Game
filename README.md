# Renpygame
Renpygame is a framework that allows pygame games to be integrated with Ren'Py. It's intended for people who are capable programmers. The philosophy of renpygame is to provide a minimal layer over pygame, and to rely on the programmer to reset things he changes.

To try out renpygame, download the renpygame demo from the [Frameworks](https://www.renpy.org/wiki/renpy/Frameworks) page, and unpack it inside a Ren'Py You can then select the renpygame-demo project from the launcher, launch it, and see an example of Ren'Py integrated with one of the pygame demo games.

To use renpygame in your own project, copy the renpygame directory from the base directory of the renpygame-demo project into the base directory of your own project. The base directory is the directory above the game directory, the directory that contains the game directory.

## Porting Pygame Code
To use renpygame, you need to change imports of pygame to imports of renpygame. For example, the code:

```renpy
import pygame
from pygame.locals import *
```

would become

```renpy
import renpygame
import renpygame as pygame
from renpygame.locals import *
```

The code can then be used mostly unchanged.

Renpygame expects that the renpygame.display.set_mode function will be called whenever we switch from Ren'Py to renpygame. It's up to the user to take a look at _preferences.fullscreen and set the FULLSCREEN flag as appropriate. For example:

```renpy
init python:

   import renpygame
   import renpygame as pygame
   from renpygame.locals import *

   def set_mode():
        if _preferences.fullscreen:
            fsflag = FULLSCREEN
        else:
            fsflag = 0

        screen = renpygame.display.set_mode((800, 600), fsflag, 32)
        return screen
```

## Supported Modules
The following modules are supported:

* renpygame.color
* renpygame.constants
* renpygame.cursors
* renpygame.display
* renpygame.draw
* renpygame.event
* renpygame.font
* renpygame.image
* renpygame.joystick
* renpygame.key
* renpygame.locals
* renpygame.mixer
* renpygame.mixer.music
* renpygame.mouse
* renpygame.sprite
* renpygame.time
* renpygame.transform


Functions that take a file have been modified so that the files are searched for in archives (except for Fonts), and in the game directory.

