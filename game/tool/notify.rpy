init python:
    ## Notifications
    # to use: default ... = NotifyEx(msg="...", img="...")
    class NotifyEx( renpy.python.RevertableObject ):
        def __init__( self, msg, img ):
            super(NotifyEx, self).__init__()
            self.msg = msg
            self.img = img
            self.remain = gui.notifyEx_delay
    ## view undefined notifications
    # to use: $ notifyEx(msg="...")
    # to use: $ notifyEx(msg="...", img="...")
    # to use: $ notifyEx(img="...")
    def notifyEx( msg=None, img=None ):
        notifications.append( NotifyEx( msg, img ) )
        if len( store.notifications ) == 1: renpy.show_screen( "notifyEx" )
    def notifyExClean( value ):
        if value in store.notifications: store.notifications.remove( value )
        if len( store.notifications ) == 0: renpy.hide_screen( "notifyEx" )
    ## view defined notifications
    # to use: $ notify(...)
    def notify( n ):
        notifications.append( NotifyEx( n.msg, n.img ) )
        if len( store.notifications ) == 1: renpy.show_screen( "notifyEx" )

# Delay of visibility of a notification.
define gui.notifyEx_delay = 10.0
# Width of the images.
define gui.notifyEx_width = 64
# Height of the images.
define gui.notifyEx_height = 64

default notifications = []

style notify_text is default:
    # color "#49aae6"
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
                text n.msg

    timer 0.05 repeat True action [ SetField( n, "remain", n.remain - 0.05 ), If( n.remain <= 0, Function( notifyExClean, n ), NullAction() ) ]
