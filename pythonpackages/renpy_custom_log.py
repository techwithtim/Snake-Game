from typing import Optional
import renpy.exports as renpy
import renpy.store as store

store.notifications = []

__all__ = [
    "NotifyEx",
    "notifyEx",
    "notifyExPreventsLoops",
    "notifyExClean",
    "notify",
]


class NotifyEx(renpy.python.RevertableObject):
    """Notifications, to use: default ... = NotifyEx(message="...", image="...")"""

    def __init__(
        self,
        message: Optional[str],
        image: Optional[str],
        delay: float = 10.0,
    ):
        super(NotifyEx, self).__init__()
        self.message = message
        self.image = image
        self.delay = delay

    @property
    def message(self) -> Optional[str]:
        """Message of a notification."""
        return self._message

    @message.setter
    def message(self, value: Optional[str]):
        self._message = value

    @property
    def image(self) -> Optional[str]:
        """Image of a notification."""
        return self._image

    @image.setter
    def image(self, value: Optional[str]):
        self._image = value

    @property
    def delay(self) -> float:
        """Delay of visibility of a notification."""
        return self._delay

    @delay.setter
    def delay(self, value: float):
        self._delay = value


def notifyEx(msg: Optional[str] = None, img: Optional[str] = None):
    store.notifications.append(NotifyEx(msg, img))
    if len(store.notifications) == 1:
        renpy.show_screen("notifyEx")
    return


def notifyExPreventsLoops(msg: Optional[str] = None, img: Optional[str] = None):
    if len(store.notifications) > 1:
        store.notifications[0] = NotifyEx(msg, img)
    else:
        store.notifications.append(NotifyEx(msg, img))
    return


def notifyExClean(value: NotifyEx):
    if value in store.notifications:
        store.notifications.remove(value)
    return


def notify(notific: NotifyEx):
    """View defined notifications.6
    to use: $ notify(...)"""
    store.notifications.append(
        NotifyEx(notific.message, notific.image, notific.delay))
    return
