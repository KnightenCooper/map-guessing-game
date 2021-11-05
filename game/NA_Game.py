import random
import arcade
from pathlib import Path
from arcade.gui import UIManager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from leaderboard import LeaderView
from guess_logic import MyGame, Country
import pyglet
import csv

music_volume = 0.5


class NA_Game(arcade.View):

    def __init__(self):
        super().__init__()
        # Start a strike total. Increase it by one at each incorrect answer. When strike reaches three, go to the else statement.
        self.strike = 0

        # list of countries         1             2         3        4       5            6                   7          8           9    
        self.NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", 
        "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama"]
        #    10            11          12            13          14

        # list of countries(Used for display)1     2         3        4       5            6                   7          8           9    
        self.display_NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", 
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

        #timer declarations
        self.total_time = 0.0
        self.output = "00:00:00"

        # store country for display
        self.display_country = self.display_NA_countries[random.randrange(0, (len(self.display_NA_countries) - 1))]

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



        # Sprite list with all the countries that is used for buttons (the above code draws the icons and this code creates buttons for guess logic)
        self.country_list = arcade.SpriteList()

        # Create every country icon by looping through the list, n is used to also loop through each countries' icons location by getting the 
        # This creates the buttons that will be used 
        n = 0
        for country_value in self.NA_countries:
            country = Country(country_value)
            country.position = self.square_positions_x[n], self.square_positions_y[n]
            self.country_list.append(country)
            n = n + 1

        self.total_time = 0.0


        #Create Buttons for user to click one for each country
        # MyGame.setup(self)

    def new_random_country(self):
        """ Delete the current country from the list and select a new random country"""
        # remove current country
        self.display_NA_countries.remove(self.display_country)
        # if there is at least one value then get a new random country
        if len(self.display_NA_countries) > 1:
            self.display_country = self.display_NA_countries[random.randrange(0, (len(self.display_NA_countries) - 1))]

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
        arcade.draw_text(self.display_country, 10, 570, arcade.color.BLACK, 40)

        # Render the text
        arcade.draw_text("North America", 10, 670, arcade.color.BLACK, 40)

        #draws the timer
        arcade.draw_text(self.output,
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                         arcade.color.BLACK, 25,
                         anchor_x="center")
        #create buttons
        # MyGame.on_draw(self)





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




            # The correct is the country that is being displayed, this variable exists for code readability
            correct_answer = self.display_country
            print(correct_answer)
            

            # if the country clicked is the correct answer then make the icon green
            if countries[0].country_name == correct_answer:
                # move onto the next country and update what country is shown
                NA_Game.new_random_country(self)


                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\green-square.png")
                right.position = countries[0].position
                self.square_list.append(right)

                
            # if it is the wrong guess then we make the icon red
            else:
                
                self.strike += 1
                print("YOU FOOL!!!!" + str(self.strike))
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\red-square.png")
                wrong.position = countries[0].position
                self.square_list.append(wrong)
                if self.strike == 3:

                    self.strike = 0
                    # move onto the next country and update what country is shown
                    NA_Game.new_random_country(self)
            if len(self.display_NA_countries) == 1:
                name = input('What is your name? ')
                
                rows = [name , self.output]

                #sets the filename equal to a variable
                filename = (str(Path(__file__).parent.resolve()) + "\\leaderboard.csv")


                #opens and appends the data to the file
                with open(filename, 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(rows)
                    print(rows)
                
                #takes you to the leaderboard
                instruction = LeaderView() 
                self.window.show_view(instruction)
    #logic for the timer
    def on_update(self, delta_time):

        self.total_time += delta_time

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        seconds_100s = int((self.total_time - seconds) * 100)

        self.output = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"



    def on_key_press(self, symbol: arcade.key.ESCAPE, modifiers):
        pyglet.app.exit()


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
# https://api.arcade.academy/en/latest/examples/timer.html
# https://github.com/grant516/cse210-project
# https://api.arcade.academy/en/latest/_modules/arcade/window_commands.html#exit
# https://api.arcade.academy/en/latest/api/window.html?highlight=key%20press#arcade.View.on_key_press
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

