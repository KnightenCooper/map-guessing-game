"""
Updated start_menu
"""
import arcade
from pathlib import Path
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from leaderboard import LeaderView
from NA_Game import NA_Game
from SA_Game import SA_Game
from EU_Game import EU_Game
from ASIA_Game import ASIA_Game
from AFRICA_Game import AFRICA_Game


# button values. The BUTTON_VALUES needs to match the class name for buttons to work
BUTTON_VALUES = [NA_Game, LeaderView, SA_Game, "south_america_leaderboard", ASIA_Game, "asia_leaderboard", AFRICA_Game, "africa_leaderboard", EU_Game, "europe_leaderboard"]
POSITIONX = [SCREEN_WIDTH * 0.5, SCREEN_WIDTH * 0.5 + 190]
POSITIONY = [SCREEN_HEIGHT * .75, SCREEN_HEIGHT * .75, SCREEN_HEIGHT * .6, SCREEN_HEIGHT * .6, SCREEN_HEIGHT * .45, SCREEN_HEIGHT * .45,
 SCREEN_HEIGHT * .3, SCREEN_HEIGHT * .3, SCREEN_HEIGHT * .15, SCREEN_HEIGHT * .15]
BUTTON_IMAGE = ["new_game", "leaderboard"]

class Button(arcade.Sprite):
    """ button sprite """

    def __init__(self, button_name, n, scale=1):
        """ button constructor """

        # This button_name will represent the button and be its name, This is important when we determine if the user clicked the right button
        self.button_name = button_name
        # The below line of code uses the button's name to automatically get the correct icon for Demo.
        #self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\{self.button_name}.png"
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\\{BUTTON_IMAGE[n]}.png"

        # Call the parent
        super().__init__(self.image_file_name, scale=1, hit_box_algorithm="None")


class StartMenu(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()

        # Sprite list with all the buttons
        self.button_sprite_list = None
        # set the background color
        arcade.set_background_color(arcade.color.BLACK)


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Sprite list with all the buttons
        self.button_sprite_list = arcade.SpriteList()

        # Create every button icon by looping through the list, n is used to also loop through each buttons' icons location by getting the 
        # x value from the list POSITIONX and the y value from the list POSITIONY
        n = 0
        for button_value in BUTTON_VALUES:
            button = Button(button_value, n % 2)
            button.position = POSITIONX[n % 2], POSITIONY[n]
            self.button_sprite_list.append(button)
            n = n + 1

    def draw_country_label(text, height):
        """ draw the text labels for the countries onto the screen"""
        arcade.draw_text(text,
                    SCREEN_WIDTH * 0.5 - 230,
                    SCREEN_HEIGHT * height -20,
                    arcade.color.WHITE_SMOKE,
                    font_size=30,
                    anchor_x="center")

    def draw_title(text, height):
        """ draw the text labels for the game's title"""
        arcade.draw_text(text,
                    SCREEN_WIDTH * 0.5,
                    SCREEN_HEIGHT * height -20,
                    arcade.color.WHITE_SMOKE,
                    font_size=30,
                    anchor_x="center")

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the buttons
        self.button_sprite_list.draw()

        # create a 2-dimensional array that stores the text to be displayed and the height modifier
        country_labels = [["North America", .75], ["South America", .6], ["Asia", .45], ["Africa", .3], ["Europe", .15]]
        # loop through the array and draw the text onto the start menu screen based on the values in the array
        for country in country_labels:
            StartMenu.draw_country_label(country[0], country[1])
        StartMenu.draw_title("- Map Guessing Game -", 0.9)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of buttons we've clicked on
        buttons = arcade.get_sprites_at_point((x, y), self.button_sprite_list)

        # Have we clicked on a button?
        if len(buttons) > 0:
            # set view to equal the button_name which is the same as the Class name for new view. Example: button_name = LeaderView
            view = buttons[0].button_name()

            # if we click a game button we need to setup() the game before we show the view. This is NOT necessary if it is a leaderboard button view
            if buttons[0].button_name == NA_Game:
                view.setup()
            elif buttons[0].button_name == SA_Game:
                view.setup()
            elif buttons[0].button_name == ASIA_Game:
                view.setup() 
            elif buttons[0].button_name == AFRICA_Game:
                view.setup()
            elif buttons[0].button_name == EU_Game:
                view.setup()  
   
        # show the view to the user
        self.window.show_view(view)

            # if buttons[0].button_name == 'north_america_leaderboard':
            #     print('You clicked sldkfj')
            #     leader_view = LeaderView()
            #     self.window.show_view(leader_view)

         



          
# def main():
#     """ Main function """
#     window = MyGame()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()

# Source: 
# https://api.arcade.academy/en/latest/tutorials/card_game/index.html