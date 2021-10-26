# main function
import arcade


import constants
from start_menu_view_UPDATED import StartMenu
from leaderboard import LeaderView


def main():
    """ the main function: compiles all code and runs the program. 
    args: none.
    """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, fullscreen=False)
    width, height = window.get_size()

    window.set_viewport(0, width, 0, height)

    start_view = StartMenu()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()

    # window = MyGame()
    # window.setup()
    # arcade.run()
main()

# def main():
#     """ Main function """
#     window = LeaderView()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()