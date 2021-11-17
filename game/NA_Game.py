import random
import arcade
from pathlib import Path
from arcade.gui import UIManager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from leaderboard import LeaderView
from icons import CountryClickableIcons
import pyglet
import csv
from get_name_view import GetNameView


class NA_Game(arcade.View):

    def __init__(self):
        super().__init__()
        # Start a strike total. Increase it by one at each incorrect answer. When strike reaches three, go to the else statement.
        self.strike = 0

        # list of countries         1             2         3        4       5            6                   7          8           9    
        self.NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", 
        "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama"]
        #    10            11          12            13          14

        #                           1    2    3    4      5     6     7    8     9    10   11    12    13    14
        self.square_positions_x = [930, 870, 910, 1125, 1175, 1220, 1190, 890, 1070, 940, 1100, 1130, 1020, 1200]
        self.square_positions_y = [290, 460, 150, 215, 220, 205, 110, 70, 130, 35, 110, 90, 30, 60]
        #                           1    2    3    4    5    6    7    8    9  10   11  12  13  14

        # Lists that keep track of each sprite in it
        self.square_list = None
        self.background_list = None

        # separate background image sprite
        self.background_sprite = None
        self.black_square = None
        # make the background grey
        arcade.set_background_color(arcade.color.WHITE)

        #timer declarations
        self.total_time = 0.0
        self.output = "00:00:00"

        # store country for display
        # (I REMOVED -1 AFTER len(self.NA_countries))
        self.display_country = self.NA_countries[random.randrange(0, (len(self.NA_countries)))]
            
    def setup(self):
        """ get the game set up and ready to play by creating background and clickable icons """
        # self.background = arcade.load_texture("assets/NA-template.png")
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\NA-template.png"
        self.square_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\black-square.png"

        self.background_list = arcade.SpriteList()

        self.background_sprite = arcade.Sprite(self.background_img_path, scale=1, center_x=640, center_y=360)
        self.background_list.append(self.background_sprite)

        # Sprite list with all the countries that is used for buttons (the above code draws the icons and this code creates buttons for guess logic)
        self.country_list = arcade.SpriteList()

        # Create every country icon by looping through the list, n is used to also loop through each countries' icons location by getting the x and y values
        # This creates the buttons that will be used for the user to click and guess
        n = 0
        for country_value in self.NA_countries:
            country = CountryClickableIcons(country_value)
            country.position = self.square_positions_x[n], self.square_positions_y[n]
            self.country_list.append(country)
            n = n + 1
        # start clock at 0
        self.total_time = 0.0

    def new_random_country(self):
        """ Delete the current country from the list and select a new random country"""
        # remove current country
        self.NA_countries.remove(self.display_country)
        # if there is at least one value then get a new random country
        if len(self.NA_countries) > 1:
            self.display_country = self.NA_countries[random.randrange(0, (len(self.NA_countries)))]
        # if there is only one value then use that value
        if len(self.NA_countries) == 1:
            self.display_country = self.NA_countries[0]

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        # draws the background map
        self.background_list.draw()
        # draws each square
        self.country_list.draw()

        # Render the text of the counrty that user should guess
        arcade.draw_text(self.display_country, 10, 570, arcade.color.BLACK, 40)

        # Render the text that tells user which continent they are looking at
        arcade.draw_text("North America", 10, 670, arcade.color.BLACK, 40)

        # draws the timer
        arcade.draw_text(self.output,
                         115, SCREEN_HEIGHT // 1.5,
                         arcade.color.BLACK, 40,
                         anchor_x="center")

    # Add on_mouse_press from guess_logic.py file
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of countries we've clicked on
        # countries = arcade.get_sprites_at_point((x, y), self.country_list)
        countries = arcade.get_sprites_at_point((x, y), self.country_list)

        # prints x and y coordinates of where the mouse was clicked
        print(x,y)

        # Have we clicked on a country?
        if len(countries) > 0:
            # print the name of the country clicked
            print('You clicked ' + countries[0].country_name)

            # The correct is the country that is being displayed, this variable exists for code readability
            correct_answer = self.display_country
            print(correct_answer)
            
            # if the country clicked is the correct answer then move onto the next country and make the icon green 
            if countries[0].country_name == correct_answer:
                # move onto the next country and update what country is shown
                NA_Game.new_random_country(self)
                # make the country green
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\green-square.png")
                right.position = countries[0].position
                self.country_list.append(right)
                # rest strikes
                self.strike = 0
                
            # if it is the wrong guess then we make the icon red, increase the strike counter, and see if the user is out of guesses
            # if asset is not green then do this
            elif countries[0].country_name in self.NA_countries :
                self.strike += 1
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\red-square.png")
                wrong.position = countries[0].position
                self.country_list.append(wrong)
                # if the user has made 3 guesses then we reset the strike counter and move onto the next country
                

                # if self.strike == 3:
                #     self.strike = 0
                #     # move onto the next country and update what country is shown
                #     NA_Game.new_random_country(self)


            # if the user has attempted to guess all possible countries then we get their name and log their score into the leaderboard
            if len(self.NA_countries) == 0:



                # name = input('What is your name? ')
                
                # rows = [name , self.output]

                # #sets the filename equal to a variable
                # filename = (str(Path(__file__).parent.resolve()) + "\\leaderboard.csv")

                # #opens and appends the data to the file
                # with open(filename, 'a') as csvfile:
                #     csvwriter = csv.writer(csvfile)
                #     csvwriter.writerow(rows)
                #     print(rows)
                
                # Takes you to get your name
                view = GetNameView()
                self.window.show_view(view)

                #takes you to the leaderboard
                # instruction = LeaderView() 
                # self.window.show_view(instruction)
                
    #logic for the timer
    def on_update(self, delta_time):

        self.total_time += delta_time

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        hundredths = int(((self.total_time - seconds) % 60) * 100)

        self.output = f"{minutes:02d}:{seconds:02d}:{hundredths:02d}"

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

