import renpy
import renpy.exports as renpy_exports

renpy.store.notifications = []

__all__ = [
    "NotifyEx",
    "notifyEx",
    "notifyExPreventsLoops",
    "notifyExClean",
    "notify",
]


class NotifyEx(renpy_exports.python.RevertableObject):
    """Notifications, to use: default ... = NotifyEx(msg="...", img="...")"""

    def __init__(
        self,
        msg: str,
        img: str,
        delay: int = 10.0,
    ):
        super(NotifyEx, self).__init__()
        self.msg = msg
        self.img = img
        self.remain = 10.0  # Delay of visibility of a notification.


def notifyEx(msg: str = None, img: str = None):
    renpy.store.notifications.append(NotifyEx(msg, img))
    if len(renpy.store.notifications) == 1:
        renpy_exports.show_screen("notifyEx")
    return


def notifyExPreventsLoops(msg: str = None, img: str = None):
    if len(renpy.store.notifications) > 1:
        renpy.store.notifications[0] = NotifyEx(msg, img)
    else:
        renpy.store.notifications.append(NotifyEx(msg, img))
    return


def notifyExClean(value):
    if value in renpy.store.notifications:
        renpy.store.notifications.remove(value)
    return


def notify(notific):
    """View defined notifications.6
    to use: $ notify(...)"""
    renpy.store.notifications.append(NotifyEx(notific.msg, notific.img))
    return
