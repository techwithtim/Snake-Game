from typing import Optional
import renpy.exports as renpy
import renpy.store as store

store.notifications = []

DEFAULT_NOTIFY_DELAY = 10.0

__all__ = [
    "NotifyEx",
    "notify_add",
    "notify_prevents_loops",
    "notify_remove",
    "notify",
]


class NotifyEx(renpy.python.RevertableObject):
    """Notifications, to use: default ... = NotifyEx(message="...", image="...")"""

    def __init__(
        self,
        message: Optional[str],
        image: Optional[str],
        delay: Optional[float] = None,
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
        return self._delay if self._delay is not None else DEFAULT_NOTIFY_DELAY

    @delay.setter
    def delay(self, value: Optional[float]):
        self._delay = value


def notify_add(message: Optional[str] = None, image: Optional[str] = None, delay: Optional[float] = None):
    store.notifications.append(NotifyEx(message, image, delay))
    if len(store.notifications) == 1:
        renpy.show_screen("notifyEx")
    return


def notify_prevents_loops(msg: Optional[str] = None, img: Optional[str] = None):
    if len(store.notifications) > 1:
        store.notifications[0] = NotifyEx(msg, img)
    else:
        store.notifications.append(NotifyEx(msg, img))
    return


def notify_remove(value: NotifyEx):
    if value in store.notifications:
        store.notifications.remove(value)
    return


def notify(notific: NotifyEx):
    """View defined notifications.6
    to use: $ notify(...)"""
    store.notifications.append(
        NotifyEx(notific.message, notific.image, notific.delay))
    return
