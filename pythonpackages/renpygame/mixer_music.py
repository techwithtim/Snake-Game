import renpy.exports as renpy

# https://www.renpy.org/doc/html/audio.html#functions
# https://www.pygame.org/docs/ref/music.html


global current_music_filename


def load(filename: str) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.load"""
    global current_music_filename
    current_music_filename = filename
    return


def unload() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.unload"""
    global current_music_filename
    current_music_filename = None
    return


def play(loops: int = 0, start: float = 0.0, fade_ms: int = 0) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.play"""
    if current_music_filename is None:
        print("renpygame.mixer_music.play: no music loaded")
        return
    renpy.music.play(current_music_filename, loop=loops, fadeout=fade_ms)
    return


def rewind() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.rewind"""
    # TODO: implement
    print("renpygame.mixer_music.rewind: not implemented yet")
    return


def stop() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.stop"""
    renpy.music.stop()
    return


def pause() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.pause"""
    renpy.music.set_pause(True)
    return


def unpause() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.unpause"""
    renpy.music.set_pause(False)
    return


def fadeout(time: float) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.fadeout"""
    # TODO: implement
    print("renpygame.mixer_music.fadeout: not implemented yet")
    return


def set_volume(volume: float) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_volume"""
    renpy.music.set_volume(volume)
    return


def get_volume() -> float:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_volume"""
    # TODO: implement
    print("renpygame.mixer_music.get_volume: not implemented yet")
    return 0.0


def get_busy() -> bool:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_busy"""
    # TODO: implement
    print("renpygame.mixer_music.get_busy: not implemented yet")
    return False


def set_pos(pos: float) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_pos"""
    # TODO: implement
    print("renpygame.mixer_music.set_pos: not implemented yet")
    return


def get_pos() -> float:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_pos"""
    renpy.music.get_pos()
    return 0.0


def queue(fileobj, namehint: str = "", loops: int = 0) -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.queue"""
    renpy.music.queue(fileobj, loop=loops)
    return


def set_endevent() -> None:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_endevent"""
    # TODO: implement
    print("renpygame.mixer_music.set_endevent: not implemented yet")
    return


def get_endevent() -> type:
    """pygame: https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_endevent"""
    # TODO: implement
    print("renpygame.mixer_music.get_endevent: not implemented yet")
    return type
