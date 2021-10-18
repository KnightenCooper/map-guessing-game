# main function
import arcade


import constants
from start_menu_view import start_menu


def main():
    """ the main function: compiles all code and runs the program. 
    args: none.
    """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, fullscreen=True)
    width, height = window.get_size()

    window.set_viewport(0, width, 0, height)

    start_view = start_menu()
    window.show_view(start_view)
    arcade.run()

main()