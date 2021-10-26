import random
import arcade
from pathlib import Path
from arcade.gui import UIManager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from leaderboard import LeaderView

music_volume = 0.5



class NA_Game(arcade.View):

    def __init__(self):
        super().__init__()

        # Lists that keep track of each sprite in it
        # self.square_list = None
        self.background_list = None

        # separate background image sprite
        self.background_sprite = None

        arcade.set_background_color(arcade.color.CADET_GREY)

    def setup(self):
        # self.background = arcade.load_texture("assets/NA-template.png")
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\NA-template.png"

        # self.square_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        self.background_sprite = arcade.Sprite(self.background_img_path, scale=1, center_x=640, center_y=360)
        self.background_list.append(self.background_sprite)



    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture

        """ this will be implemented later """
        # self.square_list.draw()
        self.background_list.draw()

        # Render the text
        arcade.draw_text("North America", 10, 20, arcade.color.BLACK, 14)


# Sources:
# https://arcade-pk.readthedocs.io/en/latest/examples/sprite_move_animation.html
# https://api.arcade.academy/en/2.6.3/api/gui_widgets.html?highlight=button#arcade.gui.UITextureButton
# https://www.codegrepper.com/code-examples/python/console+log+python
# https://realpython.com/arcade-python-game-framework/
# https://api.arcade.academy/en/latest/gui/index.html
# https://api.arcade.academy/en/latest/examples/gui_widgets.html#gui-widgets
# https://api.arcade.academy/en/latest/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
# https://github.com/KnightenCooper/game
# https://api.arcade.academy/en/latest/arcade.color.html
# https://api.arcade.academy/en/2.6.3/api/window.html?highlight=button#arcade.View.on_mouse_press