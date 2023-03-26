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
    store.notifications.append(NotifyEx(msg, img))
    if len(store.notifications) == 1:
        renpy.show_screen("notifyEx")
    return


def notifyExPreventsLoops(msg: str = None, img: str = None):
    if len(store.notifications) > 1:
        store.notifications[0] = NotifyEx(msg, img)
    else:
        store.notifications.append(NotifyEx(msg, img))
    return


def notifyExClean(value):
    if value in store.notifications:
        store.notifications.remove(value)
    return


def notify(notific):
    """View defined notifications.6
    to use: $ notify(...)"""
    store.notifications.append(NotifyEx(notific.msg, notific.img))
    return
