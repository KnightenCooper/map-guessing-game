import random
import arcade
from pathlib import Path
from arcade.gui import UIManager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from leaderboard import LeaderView
from icons import CountryClickableIcons
import pyglet
from get_name_view import GetNameView
# library and class imports

class EU_Game(arcade.View):

    def __init__(self):
        super().__init__()
        # Start a streak total. Increase it by one at each incorrect answer. When streak reaches three, go to the else statement.
        self.streak = 0

        # list of countries      1          2         3         4          5          6          7           8         9          10        11         12
        self.EU_countries = ["Iceland", "Norway", "Sweden", "Finland", "Estonia", "Latvia", "Lithuania", "Russia", "Belarus", "Ukraine", "Poland", "Denmark",
        #    13          14            15          16          17           18           19         20          21             22         23        24
         "Germany", "Netherlands", "Belgium", "Luxembourg", "France", "Switzerland", "Portugal", "Spain", "United Kingdom", "Ireland", "Italy", "Czechia",
        #    25          26          27         28         29        30        31          32         33         34         35            36         37
         "Slovakia", "Austria", "Slovenia", "Croatia", "Hungary", "Serbia", "Romania", "Moldova", "Bulgaria", "Bosnia", "Montenegro", "Albania", "Greece",
        #   38         39        40           41                 42            43
         "Turkey", "Cyprus", "Andorra", "Liechtenstein", "North Macedonia", "Kosovo"]

        # These lists hold the x and y coordinates that each square should go for each country, they are correlated by number
        #                           1    2    3    4     5     6     7     8    9     10    11   12   13   14   15   16   17   18   19   20   21   22   23   24
        self.square_positions_x = [638, 847, 907, 987, 1011, 1016, 1007, 1139, 1061, 1132, 979, 797, 861, 783, 613, 611, 763, 839, 561, 683, 731, 673, 874, 928,
        # 25   26   27   28   29   30    31    32    33    34   35   36    37    38   39     40   41   42    43
         974, 932, 767, 804, 987, 1011, 1056, 1159, 1075, 867, 924, 1116, 1015, 1199, 1228, 563, 798, 1158, 965]

        #                           1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
        self.square_positions_y = [587, 478, 451, 526, 464, 433, 397, 514, 385, 311, 337, 408, 312, 356, 301, 266, 230, 228, 124, 117, 347, 355, 199, 288,
        # 25   26  27  28   29   30   31   32   33  34  35  36  37   38  39   40   41  42  43
         268, 249, 74, 48, 240, 199, 236, 224, 182, 55, 82, 34, 48, 150, 47, 200, 147, 52, 64]

        # Lists that keep track of each sprite in it
        self.square_list = None
        self.background_list = None

        # separate background image sprite
        self.background_sprite = None
        # square image sprite
        self.black_square = None
        # set background color to white
        arcade.set_background_color(arcade.color.WHITE)

        # timer declarations
        self.total_time = 0.0
        self.output = "00:00:00"
        self.final_time = ''

        # store a random country for display (this is the country you have to guess)
        self.display_country = self.EU_countries[random.randrange(0, (len(self.EU_countries)))]
            
    def setup(self):
        """ get the game set up and ready to play by creating sprites and buttons """
        # loading images for the background and square
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\EU-template.png"
        self.square_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\black-square.png"
        # initializes sprite list for the background
        self.background_list = arcade.SpriteList()
        # creates the background image as a sprite and adds it to the background_list 
        self.background_sprite = arcade.Sprite(self.background_img_path, scale=1, center_x=640, center_y=360)
        self.background_list.append(self.background_sprite)

        # Sprite list with each square for each country
        self.country_list = arcade.SpriteList()

        # Create every country icon by looping through the country list, n is used to also loop through each countries' icons location by getting the x and y values
        # This creates the buttons that will be used for the user to click and guess
        n = 0
        for country_value in self.EU_countries:
            # for each country in the country list

            """ Each country is passed through CountryClickableIcons class to be created as a sprite (black square) and then
            is given it's respective x and y coordinates and added to the list of all black square sprites for each country"""
            country = CountryClickableIcons(country_value)
            country.position = self.square_positions_x[n], self.square_positions_y[n]
            self.country_list.append(country)
            n = n + 1

        # start clock at 0
        self.total_time = 0.0

    def new_random_country(self):
        """ Delete the current country from the list and select a new random country"""
        # remove current country
        self.EU_countries.remove(self.display_country)

        # if there is at least 2 countries left in the list, get a random one
        if len(self.EU_countries) > 1:
            self.display_country = self.EU_countries[random.randrange(0, (len(self.EU_countries)))]

        # if there is only one country left then just use that one
        if len(self.EU_countries) == 1:
            self.display_country = self.EU_countries[0]

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
        arcade.draw_text("Europe", 10, 670, arcade.color.BLACK, 40)

        # draws the timer
        arcade.draw_text(self.output,
                         115, SCREEN_HEIGHT // 1.5,
                         arcade.color.BLACK, 40,
                         anchor_x="center")


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of countries we've clicked on from the country sprite list
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
                #increase streak if right
                self.streak += 1
                if (self.streak == 3):
                    # reset streaks
                    self.streak = 0
                    tada_sound = arcade.load_sound(str(Path(__file__).parent.resolve()) +"\\\\assets\\tada.mp3")
                    arcade.play_sound(tada_sound, 0.5)
                # play positive sound if right 
                else:
                    correct_sound = arcade.load_sound(str(Path(__file__).parent.resolve()) +"\\assets\\correct.mp3")
                    arcade.play_sound(correct_sound, 0.5)
                # move onto the next country and update what country is shown
                EU_Game.new_random_country(self)
                # makes the square green by creating a new green sprite over the black sprite with the same position and appends it to the sprite list to be rendered
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\green-square.png")
                right.position = countries[0].position
                self.country_list.append(right)

                
            # if it is the wrong guess then we make the icon red, reset the streak counter, and see if the user is out of guesses
            # if guess is incorrect then we do this
            elif countries[0].country_name in self.EU_countries :
                # reset streaks
                self.streak = 0
                
                # makes the square red by creating a new green sprite over the black sprite with the same position and appends it to the sprite list to be rendered
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\red-square.png")
                wrong.position = countries[0].position
                self.country_list.append(wrong)
                

                # This is unimplemented but if you want the game skip to the next country after 3 wrong guesses then uncomment this
                
                # if self.streak == 3:
                #     self.streak = 0
                #     # move onto the next country and update what country is shown
                #     EU_Game.new_random_country(self)


            # if the user has guessed all of the countries then we get their name and log their score into the leaderboard
            if len(self.EU_countries) == 0:

                # self.output passes the user's final time and the filepath will add the time to correct .csv file  
                print(self.output)

                # Initializes GetNameView class and passes the final time and leaderboard file path, then shows the view for the leaderboard
                view = GetNameView(self.output, "\\EU_leaderboard.csv")
                self.window.show_view(view)


    # timer function
    def on_update(self, delta_time):
        # function continously updates as the game goes on

        # adds the change in time (delta_time) to the total_time
        self.total_time += delta_time

        # gets the minutes
        minutes = int(self.total_time) // 60
        # gets the seconds
        seconds = int(self.total_time) % 60
        # gets the milliseconds
        hundredths = int(((self.total_time - seconds) % 60) * 100)

        self.output = f"{minutes:02d}:{seconds:02d}:{hundredths:02d}"

    def on_key_press(self, symbol: arcade.key.ESCAPE, modifiers):
        # this function waits for the ESC key to be pressed and when it does, it quits the game and closes the window
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

