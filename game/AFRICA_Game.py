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

class AFRICA_Game(arcade.View):

    def __init__(self):
        super().__init__()
        # Start a streak total. Increase it by one at each incorrect answer. When streak reaches three, go to the else statement.
        self.streak = 0

        # list of countries          1          2          3         4        5             6               7         8        9       10       11        12
        self.AFRICA_countries = ["Morocco", "Algeria", "Tunisia", "Libya", "Egypt", "Western Sahara", "Mauritania", "Mali", "Niger", "Chad", "Sudan", "Eritrea",
        #    13          14             15            16           17           18             19               20          21      22       23        24         25
         "Senegal", "The Gambia", "Guinea-Bissau", "Guinea", "Sierra Leone", "Liberia", "Cote d'lvoire", "Burkina Faso", "Ghana", "Togo", "Benin", "Nigeria", "Cameroon",
        #             26                  27            28          29          30             31              32              33                             34
         "Central African Republic", "South Sudan", "Djibouti", "Ethiopia", "Somalia", "Equatorial Guinea", "Gabon", "Republic of the Congo", "Democratic Republic of the Congo",
        #   35        36        37       38          39         40        41        42          43           44          45         46            47
         "Uganda", "Kenya", "Rwanda", "Burundi", "Tanzania", "Angola", "Zambia", "Malawi", "Mozambique", "Zimbabwe", "Namibia", "Botswana", "South Africa",
        #    48         49           50                  51
         "Lesotho", "Eswatini", "Madagascar", "Sao Tome and Principe"]

        # These lists hold the x and y coordinates that each square should go for each country, they are correlated by number
        #                           1    2    3    4     5    6    7    8    9    10   11    12    13   14   15   16   17   18   19   20   21   22   23   24
        self.square_positions_x = [732, 807, 909, 934, 1038, 594, 701, 773, 871, 943, 1042, 1145, 590, 495, 534, 580, 628, 678, 739, 701, 752, 788, 824, 853,
        # 25   26   27    28    29    30    31   32   33   34   35    36    37    38    39    40   41    42    43    44    45   46   47   48    49    50    51
         891, 969, 1044, 1185, 1121, 1242, 756, 764, 851, 986, 1243, 1108, 1213, 1172, 1085, 935, 1008, 1117, 1110, 1041, 930, 991, 980, 1101, 1136, 1183, 747]

        #                           1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
        self.square_positions_y = [632, 595, 685, 588, 580, 578, 520, 508, 502, 479, 487, 559, 479, 469, 430, 404, 367, 339, 411, 248, 340, 338, 374, 427,
        # 25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46  47  48   49   50   51
         384, 404, 406, 531, 418, 508, 223, 160, 108, 329, 393, 349, 301, 283, 284, 240, 219, 157, 224, 183, 160, 157, 77, 60, 104, 187, 275]

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
        self.display_country = self.AFRICA_countries[random.randrange(0, (len(self.AFRICA_countries)))]
            
    def setup(self):
        """ get the game set up and ready to play by creating sprites and buttons """
        # loading images for the background and square
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\AFRICA-template.png"
        self.square_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\black-square.png"
        # initializes sprite list for the background
        self.background_list = arcade.SpriteList()
        # creates the background image as a sprite and adds it to the background_list 
        self.background_sprite = arcade.Sprite(self.background_img_path, scale=1, center_x=640, center_y=360)
        self.background_list.append(self.background_sprite)

        # Sprite list with each square for each country
        self.country_list = arcade.SpriteList()
        # sprite list containing red squares
        self.wrong_list = arcade.SpriteList()
        # sprite list containing green squares
        self.right_list = arcade.SpriteList()

        # Create every country icon by looping through the country list, n is used to also loop through each countries' icons location by getting the x and y values
        # This creates the buttons that will be used for the user to click and guess
        n = 0
        for country_value in self.AFRICA_countries:
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
        self.AFRICA_countries.remove(self.display_country)

        # if there is at least 2 countries left in the list, get a random one
        if len(self.AFRICA_countries) > 1:
            self.display_country = self.AFRICA_countries[random.randrange(0, (len(self.AFRICA_countries)))]

        # if there is only one country left then just use that one
        if len(self.AFRICA_countries) == 1:
            self.display_country = self.AFRICA_countries[0]

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        # draws the background map
        self.background_list.draw()
        # draws each square for each list
        self.country_list.draw()
        self.wrong_list.draw()
        self.right_list.draw()

        # Render the text of the counrty that user should guess
        arcade.draw_text(self.display_country, 10, 570, arcade.color.BLACK, 40)

        # Render the text that tells user which continent they are looking at
        arcade.draw_text("Africa", 10, 670, arcade.color.BLACK, 40)

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
            print('Correct answer is ' + correct_answer)
            
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
                AFRICA_Game.new_random_country(self)
                # makes the square green by creating a new green sprite over the black sprite with the same position and appends it to the sprite list to be rendered
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\green-square.png")
                right.position = countries[0].position
                self.right_list.append(right)
                # clears red squares if there are any
                if len(self.wrong_list) > 0:
                    self.wrong_list = arcade.SpriteList()

            # If the guess is incorrect, reset the streak, create red sprite and add it to the list
            elif countries[0].country_name in self.AFRICA_countries :
                # reset streaks
                self.streak = 0
                
                # creates a red square sprite and adds it to the respective sprite list
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\red-square.png")
                wrong.position = countries[0].position
                self.wrong_list.append(wrong)
                
                
                # This is unimplemented but if you want the game skip to the next country after 3 wrong guesses then uncomment this
                
                # if self.streak == 3:
                #     self.streak = 0
                #     # move onto the next country and update what country is shown
                #     AFRICA_Game.new_random_country(self)


            # if the user has guessed all of the countries then we get their name and log their score into the leaderboard
            if len(self.AFRICA_countries) == 0:

                # self.output passes the user's final time and the filepath will add the time to correct .csv file  
                print("Final time - " + self.output)     

                # Initializes GetNameView class and passes the final time and leaderboard file path, then shows the view for the leaderboard
                view = GetNameView(self.output, "\\AFRICA_leaderboard.csv")
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