import random
import arcade
from pathlib import Path
from arcade.gui import UIManager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from leaderboard import LeaderView
from guess_logic import MyGame

music_volume = 0.5



class NA_Game(arcade.View):

    def __init__(self):
        super().__init__()

        # list of countries         1             2         3        4       5            6                   7          8           9    
        self.NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", 
        "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama"]
        #    10            11          12            13          14

        # 14 total countries        1    2    3    4      5     6     7    8     9    10   11    12    13    14
        self.square_positions_x = [930, 870, 910, 1125, 1175, 1220, 1190, 890, 1070, 940, 1100, 1130, 1020, 1200]
        self.square_positions_y = [290, 460, 150, 215, 220, 205, 110, 70, 130, 35, 110, 90, 30, 60]
        #                           1    2    3    4    5    6    7    8    9  10   11  12  13  14

        # Lists that keep track of each sprite in it
        self.square_list = None
        self.background_list = None

        # separate background image sprite
        self.background_sprite = None
        self.black_square = None

        arcade.set_background_color(arcade.color.CADET_GREY)

    def setup(self):
        # self.background = arcade.load_texture("assets/NA-template.png")
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\NA-template.png"
        self.square_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\black-square.png"

        self.square_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        self.background_sprite = arcade.Sprite(self.background_img_path, scale=1, center_x=640, center_y=360)
        self.background_list.append(self.background_sprite)

        n = 0
        for country in self.NA_countries:
            self.black_square = arcade.Sprite(self.square_img_path, scale=1, center_x=self.square_positions_x[n], center_y=self.square_positions_y[n])
            self.square_list.append(self.black_square)
            n = n + 1

        #Create Buttons for user to click one for each country
        MyGame.setup(self)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # draws the background map
        self.background_list.draw()
        # draws each square
        self.square_list.draw()

        # Render the text
        arcade.draw_text("North America", 10, 670, arcade.color.BLACK, 40)

        #create buttons
        MyGame.on_draw(self)

    # Add on_mouse_press from guess_logic.py file
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of countries we've clicked on
        countries = arcade.get_sprites_at_point((x, y), self.country_list)

        # Have we clicked on a country?
        if len(countries) > 0:
            # print the name of the country clicked
            print('You clicked ' + countries[0].country_name)

            """ Eventually the program will need to check if the country has already been correctly guessed and if so know to NOT add red 
            and keep the icon green because the user got that country correct """


            # add a variable to store the correct answer, in the final version this is be determined by getting country names from a list
            correct_answer = 'usa'
            # if the country clicked is the correct answer then make the icon green
            if countries[0].country_name == correct_answer:
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\knighten_testing\\right.png")
                right.position = countries[0].position
                self.country_list.append(right)

            # if it is the wrong guess then we make the icon red
            else:
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\knighten_testing\\wrong.png")
                wrong.position = countries[0].position
                self.country_list.append(wrong)


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