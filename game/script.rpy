image side eileen = "eileen_happy.png"

define e = Character("Eileen", color="#c8ffc8", image="eileen")

# The game starts here.
label start:
    menu:
        "Aliens":
            call aliens_start
        "Quit":
            return
        "An what do you want to play?"
    jump start