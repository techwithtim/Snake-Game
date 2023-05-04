import renpy.exports as renpy

from pythonpackages.renpygame import mixer_music

music = mixer_music

# https://www.renpy.org/doc/html/audio.html#functions


class Sound:
    """pygame: https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound"""

    def __init__(self, filename: str):
        self.filename = filename
        return

    def play(self, loops: int = 0, maxtime: int = -1, fade_ms: int = 0):
        """pygame: https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play
        renpy: https://www.renpy.org/doc/html/audio.html#renpy.play"""
        renpy.play(self.filename, channel=None)
        return

    def stop(self):
        """pygame: https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.stop"""
        # TODO: implement
        print("renpygame.mixer.Sound.stop: not implemented yet")
        return

    def pause(self):
        """pygame: https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.pause"""
        # TODO: implement
        print("renpygame.mixer.Sound.pause: not implemented yet")
        return

    def unpause(self):
        """pygame: https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.unpause"""
        # TODO: implement
        return

    def fadeout(self, time):
        # TODO: implement
        print("renpygame.mixer.Sound.fadeout: not implemented yet")
        return

    def set_volume(self, value: float):
        # TODO: implement
        print("renpygame.mixer.Sound.set_volume: not implemented yet")
        return

    def get_volume(self) -> float:
        # TODO: implement
        print("renpygame.mixer.Sound.get_volume: not implemented yet")
        return 0

    def get_num_channels(self) -> int:
        # TODO: implement
        print("renpygame.mixer.Sound.get_num_channels: not implemented yet")
        return 0

    def get_length(self) -> float:
        # TODO: implement
        print("renpygame.mixer.Sound.get_length: not implemented yet")
        return 0

    def get_raw(self) -> bytes:
        # TODO: implement
        print("renpygame.mixer.Sound.get_raw: not implemented yet")
        return bytes()

    # my methods
    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, value: str):
        self._filename = value
