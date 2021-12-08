import arcade
import constants
import pandas as pd
from pathlib import Path
from arcade.gui import UIManager

import start_menu_view

class BackButton(arcade.Sprite):
    """ Back Button sprite """
    def __init__(self, button_name, scale=1):
        """ BackButton constructor """

        # This button_name will represent view we want to return to, in this case start menu
        self.button_name = button_name
        # path to image for button
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\button\\back_button.png"

        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")


class LeaderView(arcade.View):
    """ TESTING PURPOSES ONLY... this class creates a page that says 
    Congrats! You've successfully reached the leaderboard page!!"""

    def __init__(self, filePath):
        """ TESTING PURPOSES ONLY...the class constructor.""" 
        
        self.filePath = filePath  
        super().__init__()

        # Sprite list with the back button
        self.button_list = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Sprite list with the back button
        self.button_list = arcade.SpriteList()

        # create back button
        back_button = BackButton(start_menu_view.StartMenu)
        back_button.position = 130, 100
        self.button_list.append(back_button)


    def on_show(self):
        """ TESTING PURPOSES ONLY...sets the background color of the instruction menu."""   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """TESTING PURPOSES ONLY... creates the view for the instruction menu."""
        start_x = 50
        start_y = 400
        # Clear the screen
        arcade.start_render()

        # Draw the button
        self.button_list.draw() 

        arcade.draw_text("LEADERBOARD",start_x, start_y,
                         arcade.color.RED,
                         font_size=30,
                         anchor_x="left", anchor_y="top")
        # Read the csv file and get the fastest time
        filename = (str(Path(__file__).parent.resolve()) + self.filePath)
        # store the csv file into data
        data = pd.read_csv(filename)
        # best_score = data.time.min()

        # First we sort 'data' into 'sorted_data' that has 10 values and is the 10 fastest times  
        sorted_data = data.sort_values(by ="time", ascending=True).head(10)

        # store the #1 best player and #1 best score 
        best_player = sorted_data.iat[0,0]
        best_score = sorted_data.iat[0,1]

        # store the #2 best player and #1 best score 
        best_player2 = sorted_data.iat[1,0]
        best_score2 = sorted_data.iat[1,1]

        # store the #3 best player and #1 best score 
        best_player3 = sorted_data.iat[2,0]
        best_score3 = sorted_data.iat[2,1]

        # store the #4 best player and #1 best score
        best_player4 = sorted_data.iat[3, 0]
        best_score4 = sorted_data.iat[3, 1]

        # store the #5 best player and #1 best score
        best_player5 = sorted_data.iat[4, 0]
        best_score5 = sorted_data.iat[4, 1]

        # store the #6 best player and #1 best score
        best_player6 = sorted_data.iat[5, 0]
        best_score6 = sorted_data.iat[5, 1]

        # store the #7 best player and #1 best score
        best_player7 = sorted_data.iat[6, 0]
        best_score7 = sorted_data.iat[6, 1]

        # store the #8 best player and #1 best score
        best_player8 = sorted_data.iat[7, 0]
        best_score8 = sorted_data.iat[7, 1]

        # store the #9 best player and #1 best score
        best_player9 = sorted_data.iat[8, 0]
        best_score9 = sorted_data.iat[8, 1]

        # store the #10 best player and #1 best score
        best_player10 = sorted_data.iat[9, 0]
        best_score10 = sorted_data.iat[9, 1]

        # store the best scores/players
        # first = f'#1 {best_score} by {best_player}' NOTE: for this entry I showed how you could code the answer directly into the scores array
        second = f'#2 {best_score2} by {best_player2}'
        third = f'#3 {best_score3} by {best_player3}'
        fourth = f'#4 {best_score4} by {best_player4}'
        fifth = f'#5 {best_score5} by {best_player5}'
        sixth = f'#6 {best_score6} by {best_player6}'
        seventh = f'#7 {best_score7} by {best_player7}'
        eighth = f'#8 {best_score8} by {best_player8}'
        ninth = f'#9 {best_score9} by {best_player9}'
        tenth = f'#10 {best_score10} by {best_player10}'

        # create an array to store the text that will be displayed and the height it will be displayed 
        scores = [['#1 '+ str(best_score) + ' by ' + str(best_player), .9], [second, .82], [third, .74], [fourth, .66],
                  [fifth, .58], [sixth, .5], [seventh, .42], [eighth, .34], [ninth, .26], [tenth, .18]]
        # loop through the array and draw the text onto the start menu screen based on the values in the array
        for score in scores:
            LeaderView.draw_score(score[0], score[1])

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of any sprites we've clicked on
        sprites_clicked = arcade.get_sprites_at_point((x, y), self.button_list)

        # Have we clicked on a sprite?
        if len(sprites_clicked) > 0:
            # set view to equal the button_name which is the same as the Class name for new view. 
            # Example: button_name = LeaderView
            view = sprites_clicked[0].button_name()
            # we need to setup() the next view before we show the view so the buttons work
            view.setup()  
            # show the view to the user
            self.window.show_view(view)
         
    def draw_score(text, height):
        """ draw the text labels for the scores onto the screen"""
        arcade.draw_text(text,
                    constants.SCREEN_WIDTH * 0.75 - 230,
                    constants.SCREEN_HEIGHT * height -20,
                    arcade.color.WHITE_SMOKE,
                    font_size=15,
                    anchor_x="center")


# Sources: 
# https://www.stackvidhya.com/get-value-of-cell-from-a-pandas-dataframe/#:~:text=You%20can%20get%20the%20value,iat%5B0%2C0%5D%20.
# https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/
# https://realpython.com/pandas-sort-python/#sorting-your-dataframe-on-multiple-columns
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
