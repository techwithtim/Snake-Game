init:
    # import minigame
    $ import game.minigames.aliens as aliens
    

# The game starts here.
label aliens_start:
    
    e "Welcome!"

    e "You're here to defend the moon from invaders from the M-64 galaxy."

    e "You can move your van back and forth with the arrow keys, and then press space to fire a missile."

    e "Good luck!"

label aliens_retry:

    $ renpy.free_memory()
    $ score = aliens.main()

    # This eats up any remaining keypresses.
    $ renpy.pause(.1)
    
    e "You shot down [score] aliens."

    if score > 10:

        e "Not bad!"

    menu:

        "Would you like to try again?"

        "Sure.":

            "Okay, get ready..."

            jump aliens_retry

        "No thanks.":

            pass

    e "No problem."

    e "This game was based off one of the examples that came with pygame."

    e "It shows how pygame games can be integrated with Ren'Py."

    e "Thank you for playing."

    return
