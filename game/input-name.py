import arcade
import constants
from arcade.gui.events import UITextEvent
from arcade.gui import UIManager

class InputName(arcade.View):
    """ TESTING PURPOSES ONLY... this class creates a page that says 
    Congrats! You've successfully reached the leaderboard page!!"""

    def __init__(self):
        """ TESTING PURPOSES ONLY...the class constructor."""   
        super().__init__()

    def on_show(self):
        """ TESTING PURPOSES ONLY...sets the background color of the instruction menu."""   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """TESTING PURPOSES ONLY... creates the view for the instruction menu."""  
        arcade.start_render()
        arcade.draw_text("Please enter your name",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2+90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")



