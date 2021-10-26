"""
DEMO of guess logic
"""
import arcade
from pathlib import Path


# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Country DEMO"
# Constants for sizing
COUNTRY_SCALE = 0.6

# How big are the countries?
COUNTRY_WIDTH = 140 * COUNTRY_SCALE
COUNTRY_HEIGHT = 190 * COUNTRY_SCALE

# How big is the mat we'll place the country on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(COUNTRY_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(COUNTRY_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# Country constant values
COUNTRY_VALUES = ["mexico", "canada", "usa"]
POSITIONX = [START_X, START_X * 3, START_X * 5]
POSITIONY = [BOTTOM_Y, BOTTOM_Y, BOTTOM_Y]


class Country(arcade.Sprite):
    """ Country sprite """

    def __init__(self, country_name, scale=1):
        """ Country constructor """

        # This country_name will represent the country and be its name, This is important when we determine if the user clicked the right country
        self.country_name = country_name
        # The below line of code uses the country's name to automatically get the correct icon for Demo.
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\knighten_testing\{self.country_name}.png"

        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite list with all the countries
        self.country_list = None
        # make the background black
        arcade.set_background_color(arcade.color.WARM_BLACK)


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        
        # Sprite list with all the countries
        self.country_list = arcade.SpriteList()

        # Create every country icon by looping through the list, n is used to also loop through each countries' icons location by getting the 
        # x value from the list POSITIONX and the y value from the list POSITIONY
        n = 0
        for country_value in COUNTRY_VALUES:
            country = Country(country_value, COUNTRY_SCALE)
            country.position = POSITIONX[n], POSITIONY[n]
            self.country_list.append(country)
            n = n + 1


    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        # arcade.start_render()
        # add text to tell user to click greatest country
        # arcade.draw_text("Click the Greatest Country of All Time:",
        #                  start_y = 300,
        #                  start_x = 500,
        #                  color = arcade.color.WHITE_SMOKE,
        #                  font_size=30,
        #                  anchor_x="center")
        # Draw the countries
        self.country_list.draw()

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
                right = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\knighten_testing\\right.png", COUNTRY_SCALE)
                right.position = countries[0].position
                self.country_list.append(right)

            # if it is the wrong guess then we make the icon red
            else:
                wrong = arcade.Sprite(str(Path(__file__).parent.resolve()) +"\\assets\knighten_testing\\wrong.png", COUNTRY_SCALE)
                wrong.position = countries[0].position
                self.country_list.append(wrong)



          
def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

# Source: 
# https://api.arcade.academy/en/latest/tutorials/card_game/index.html