"""
Updated start_menu
"""
import arcade
from pathlib import Path
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from leaderboard import LeaderView
from timer import Timer


# Country constant values
COUNTRY_VALUES = ["north_america_game", "north_america_leaderboard", "south_america_game", "south_america_leaderboard"]
POSITIONX = [SCREEN_WIDTH * 0.75, SCREEN_WIDTH * 0.75 + 190, SCREEN_WIDTH * 0.75, SCREEN_WIDTH * 0.75 + 190]
POSITIONY = [SCREEN_HEIGHT * .9, SCREEN_HEIGHT * .9, SCREEN_HEIGHT * .75, SCREEN_HEIGHT * .75]


class Button(arcade.Sprite):
    """ Country sprite """

    def __init__(self, country_name, scale=1):
        """ Country constructor """

        # This country_name will represent the country and be its name, This is important when we determine if the user clicked the right country
        self.country_name = country_name
        # The below line of code uses the country's name to automatically get the correct icon for Demo.
        #self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\{self.country_name}.png"
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\\button.png"

        # Call the parent
        super().__init__(self.image_file_name, scale=1, hit_box_algorithm="None")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite list with all the countries
        self.country_list = None
        # make the background WHITE_SMOKE
        arcade.set_background_color(arcade.color.WARM_BLACK)


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Sprite list with all the countries
        self.country_list = arcade.SpriteList()

        # Create every country icon by looping through the list, n is used to also loop through each countries' icons location by getting the 
        # x value from the list POSITIONX and the y value from the list POSITIONY
        n = 0
        for country_value in COUNTRY_VALUES:
            country = Button(country_value)
            country.position = POSITIONX[n], POSITIONY[n]
            self.country_list.append(country)
            n = n + 1


    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the countries
        self.country_list.draw()

        arcade.draw_text("North America:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT *.9 -20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("South America:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT *.75-20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Australia:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT  *.6 -20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Asia:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT *.45-20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Africa:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT *.3-20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Europe:",
                         SCREEN_WIDTH * 0.75 -230,
                         SCREEN_HEIGHT *.15-20,
                         arcade.color.WHITE_SMOKE,
                         font_size=30,
                         anchor_x="center")



    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of countries we've clicked on
        countries = arcade.get_sprites_at_point((x, y), self.country_list)

        # Have we clicked on a country?
        if len(countries) > 0:
            # print the name of the country clicked

            """ Eventually the program will need to check if the country has already been correctly guessed and if so know to NOT add red 
            and keep the icon green because the user got that country correct """


            # add a variable to store the correct answer, in the final version this is be determined by getting country names from a list
            correct_answer = 'usa'
            # if the country clicked is the correct answer then make the icon green
            if countries[0].country_name == 'north_america':
                print('You clicked ' + countries[0].country_name)
            # if it is the wrong guess then we make the icon red
            else:
                print('You clicked ' + countries[0].country_name)



          
def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

# Source: 
# https://api.arcade.academy/en/latest/tutorials/card_game/index.html