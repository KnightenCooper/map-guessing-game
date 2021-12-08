# main function
import arcade
import constants
from start_menu_view import StartMenu
from leaderboard import LeaderView
from pathlib import Path
# library and class imports

def main():
    """ the main function: compiles all code and runs the program. 
    args: none.
    """
    # creates the program window
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, fullscreen=False)
    width, height = window.get_size()

    # set viewport sets the view for the screen according to the width and height provided
    window.set_viewport(0, width, 0, height)

    # Initializes and sets up the start menu, and then shows that view in the window
    start_view = StartMenu()
    start_view.setup()
    window.show_view(start_view)
    window.center_window()

    # This is code for the music, it automatically stops playing when you close the window
    # Background music is loaded as "music" and then played with a volume of 0.1, it automatically stops playing when you close the window
    music = arcade.load_sound(str(Path(__file__).parent.resolve()) +"\\background.wav", True)
    arcade.play_sound(music, 0.1, 0, True)
    # starts running the game
    arcade.run()

# main function called to start the program
main()