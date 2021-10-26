"""
Updated start_menu
"""
import arcade
from pathlib import Path
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from leaderboard import LeaderView
from timer import Timer


# button constant values
BUTTON_VALUES = ["north_america_game", "north_america_leaderboard", "south_america_game", "south_america_leaderboard"]
POSITIONX = [SCREEN_WIDTH * 0.75, SCREEN_WIDTH * 0.75 + 190, SCREEN_WIDTH * 0.75, SCREEN_WIDTH * 0.75 + 190]
POSITIONY = [SCREEN_HEIGHT * .9, SCREEN_HEIGHT * .9, SCREEN_HEIGHT * .75, SCREEN_HEIGHT * .75]


class Button(arcade.Sprite):
    """ button sprite """

    def __init__(self, button_name, scale=1):
        """ button constructor """

        # This button_name will represent the button and be its name, This is important when we determine if the user clicked the right button
        self.button_name = button_name
        # The below line of code uses the button's name to automatically get the correct icon for Demo.
        #self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\{self.button_name}.png"
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\\button.png"

        # Call the parent
        super().__init__(self.image_file_name, scale=1, hit_box_algorithm="None")


class StartMenu(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()

        # Sprite list with all the buttons
        self.button_sprite_list = None
        # make the background WHITE_SMOKE
        arcade.set_background_color(arcade.color.WARM_BLACK)


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Sprite list with all the buttons
        self.button_sprite_list = arcade.SpriteList()

        # Create every button icon by looping through the list, n is used to also loop through each buttons' icons location by getting the 
        # x value from the list POSITIONX and the y value from the list POSITIONY
        n = 0
        for button_value in BUTTON_VALUES:
            button = Button(button_value)
            button.position = POSITIONX[n], POSITIONY[n]
            self.button_sprite_list.append(button)
            n = n + 1


    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the buttons
        self.button_sprite_list.draw()

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

        # Get list of buttons we've clicked on
        buttons = arcade.get_sprites_at_point((x, y), self.button_sprite_list)

        # Have we clicked on a button?
        if len(buttons) > 0:
            if buttons[0].button_name == 'north_america_game':
                print('You clicked ' + buttons[0].button_name)
                game = Timer(self) 
                self.window.show_view(game)

            if buttons[0].button_name == 'north_america_leaderboard':
                print('You clicked ' + buttons[0].button_name)
                leader_view = LeaderView()
                self.window.show_view(leader_view)

         
            else:
                print('You clicked ' + buttons[0].button_name)



          
# def main():
#     """ Main function """
#     window = MyGame()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()

# Source: 
# https://api.arcade.academy/en/latest/tutorials/card_game/index.html