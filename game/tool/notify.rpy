
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
    import pythonpackages.renpy_custom_notify as myNotify

    def notifyEx(msg: str = None, img: str = None):
        return myNotify.notifyEx(msg, img)

    def notifyExPreventsLoops(msg: str = None, img: str = None):
        return myNotify.notifyExPreventsLoops(msg, img)

    def notifyExClean(value):
        return myNotify.notifyExClean(value)

    def notify(notific):
        return myNotify.notify(notific)

style notify_text is default:
    color gui.notifyEx_color
    yalign 0.5

style notify_hbox is default:
    ysize gui.notifyEx_height

screen notifyEx():

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
            if not n.img is None:
                add n.img
            else:
                # Ensure that all the texts will be aligned.
                null width gui.notifyEx_width

            # aerate a little.
            null width 5

            if not n.msg is None:
                text n.msg color gui.notifyEx_text_color

    timer 0.05 repeat True action [ SetField( n, "remain", n.remain - 0.05 ), If( n.remain <= 0, Function( notifyExClean, n ), NullAction() ) ]
