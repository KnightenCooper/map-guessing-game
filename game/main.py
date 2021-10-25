# main function
import arcade


import constants
# from start_menu_view import start_menu
from guess_logic_demo import GuessLogic


def main():
    """ the main function: compiles all code and runs the program. 
    args: none.
    """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, fullscreen=False)
    width, height = window.get_size()

    window.set_viewport(0, width, 0, height)

    start_view = GuessLogic()
    window.show_view(start_view)
    arcade.run()


main()