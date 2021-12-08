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

class ASIA_Game(arcade.View):
    """ creates the asia game view """

    def __init__(self):
        super().__init__()
        # Start a streak total. Increase it by one at each incorrect answer. When streak reaches three, go to the else statement.
        self.streak = 0

        # list of countries       1           2         3          4            5           6              7           8        9        10            11
        self.ASIA_countries = ["Russia", "Mongolia", "China", "Kazakhstan", "Turkey", "North Korea", "South Korea", "Japan", "India", "Myanmar", "Saudi Arabia", 
        #  12        13           14           15             16         17         18         19          20             21             22            23
         "Iran", "Indonesia", "Malaysia", "Philippines", "Singapore", "Taiwan", "Georgia", "Armenia", "Azerbaijan", "Turkmenistan", "Uzbekistan", "Kyrgyzstan", 
        #     24          25        26        27        28        29       30          31          32         33        34            35                 36 
         "Tajikistan", "Cyprus", "Syria", "Lebanon", "Israel", "Jordan", "Iraq", "Afghanistan", "Kuwait", "Bahrain", "Qatar", "United Arab Emirates", "Yemen", 
        #  37        38         39       40          41          42          43        44         45          46
         "Oman", "Pakistan", "Nepal", "Bhutan", "Bangladesh", "Sri Lanka", "Laos", "Vietnam", "Cambodia", "Thailand"]

        # These lists hold the x and y coordinates that each square should go for each country, they are correlated by number
        #                           1    2    3    4    5    6    7   nn 8    9   10   11   12   13   14   15   16    17   18   19   20    21   22   23   24
        self.square_positions_x = [818, 865, 894, 699, 515, 999, 1005, 1067, 748, 838, 555, 619, 927, 921, 979, 791, 1016, 544, 577, 615, 637, 668, 736, 792,
        # 25   26   27   28   29  30   31   32    33   34   35   36   37   38   39   40   41   42   43    44   45   46
         378, 407, 319, 378, 429, 489, 661, 493, 482, 516, 596, 577, 625, 697, 781, 820, 789, 741, 1151, 1089, 927, 816]

        #                           1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19    20   21   22   23   24
        self.square_positions_y = [542, 438, 339, 446, 391, 400, 370, 370, 284, 273, 282, 341, 122, 164, 205, 106, 289, 505, 536, 547, 500, 534, 516, 394,
        # 25   26   27   28   29  30   31   32    33   34   35   36   37   38   39   40   41   42   43   44   45   46
         379, 425, 328, 298, 244, 461, 225, 275, 147, 133, 152, 197, 194, 154, 350, 366, 218, 132, 228, 258, 215, 184]

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
        self.display_country = self.ASIA_countries[random.randrange(0, (len(self.ASIA_countries)))]
            
    def setup(self):
        """ get the game set up and ready to play by creating sprites and buttons """
        # loading images for the background and square
        self.background_img_path = str(Path(__file__).parent.resolve()) + f"\\assets\\ASIA-template.png"
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
        for country_value in self.ASIA_countries:
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
        self.ASIA_countries.remove(self.display_country)

        # if there is at least 2 countries left in the list, get a random one
        if len(self.ASIA_countries) > 1:
            self.display_country = self.ASIA_countries[random.randrange(0, (len(self.ASIA_countries)))]

        # if there is only one country left then just use that one
        if len(self.ASIA_countries) == 1:
            self.display_country = self.ASIA_countries[0]

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
        arcade.draw_text("Asia", 10, 670, arcade.color.BLACK, 40)

        # draws the timer
        arcade.draw_text(self.output,
                         115, SCREEN_HEIGHT // 1.5,
                         arcade.color.BLACK, 40,
                         anchor_x="center")

    
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        # Get list of countries we've clicked on from the country sprite list
        countries = arcade.get_sprites_at_point((x, y), self.country_list)
        # uncomment if you want to print x and y coordinates of where the mouse was clicked (useful for button placement)
        # print(x,y)

        # Have we clicked on a country?
        if len(countries) > 0:

            # The correct is the country that is being displayed, this variable exists for code readability
            correct_answer = self.display_country
            
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
                ASIA_Game.new_random_country(self)
                # makes the square green by creating a new green sprite over the black sprite with the same position and appends it to the sprite list to be rendered
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\green-square.png")
                right.position = countries[0].position
                self.right_list.append(right)
                # clears red squares if there are any
                if len(self.wrong_list) > 0:
                    self.wrong_list = arcade.SpriteList()

            # If the guess is incorrect, reset the streak, create red sprite and add it to the list
            elif countries[0].country_name in self.ASIA_countries :
                # reset streaks
                self.streak = 0
                
                # creates a red square sprite and adds it to the respective sprite list
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\\red-square.png")
                wrong.position = countries[0].position
                self.wrong_list.append(wrong)

            # if the user has guessed all of the countries then we get their name and log their score into the leaderboard
            if len(self.ASIA_countries) == 0:
                # self.output passes the user's final time and the filepath will add the time to correct .csv file 
                # Initializes GetNameView class and passes the final time and leaderboard file path, then shows the view for the leaderboard
                view = GetNameView(self.output, "\\ASIA_leaderboard.csv")
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