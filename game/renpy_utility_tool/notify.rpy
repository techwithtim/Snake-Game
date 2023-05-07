init python:
    import renpy.store as store

    store.notifications = []

# Width of the images.
define gui.notifyEx_width = gui.label_text_size
# Height of the images.
define gui.notifyEx_height = gui.label_text_size

define gui.notifyEx_color = "#000000"
define gui.notifyEx_text_color = "#ffffff"

label enable_notifyEx:
    show screen notifyEx
    return
label disable_notifyEx:
    hide notifyEx
    return

init -999 python:
    import pythonpackages.renpy_utility.renpy_custom_notify as myNotify

    def notify_add(message: str = None, image: str = None):
        return myNotify.notify_add(message, image)

    def notify_prevents_loops(message: str = None, image: str = None):
        return myNotify.notify_prevents_loops(message, image)

    def notify_remove(value):
        return myNotify.notify_remove(value)

    def notify(notific):
        return myNotify.notify(notific)

style notify_text is default:
    color gui.notifyEx_color
    yalign 0.5

style notify_hbox is default:
    ysize gui.notifyEx_height

screen notifyEx:

    zorder 100

    style_prefix "notify"

    vbox:
        for d in notifications:
            use notifyExInternal( d )
            # aerate a little.
            null height 5

screen notifyExInternal( n ):

    style_prefix "notify"

    frame at notify_appear:
        hbox:
            if not n.image is None:
                add n.image
            else:
                # Ensure that all the texts will be aligned.
                null width gui.notifyEx_width

            # aerate a little.
            null width 5

            if not n.message is None:
                text n.message color gui.notifyEx_text_color

    timer 0.05 repeat True action [ SetField( n, "delay", n.delay - 0.05 ), If( n.delay <= 0, Function( notify_remove, n ), NullAction() ) ]
