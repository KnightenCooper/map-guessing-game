# main function
import arcade
import constants
from start_menu_view import StartMenu
from leaderboard import LeaderView
from pathlib import Path


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
    window.center_window()

    # This is code for the music, it automatically stops playing when you close the window
    music = arcade.load_sound(str(Path(__file__).parent.resolve()) +"\\background.wav", True)
    arcade.play_sound(music, 0.1  , 0, True)

    arcade.run()

main()