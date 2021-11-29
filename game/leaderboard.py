import arcade
import constants
import pandas as pd
from pathlib import Path
#from start_menu_view import StartMenu
from arcade.gui import UIManager



class LeaderView(arcade.View):
    """ TESTING PURPOSES ONLY... this class creates a page that says 
    Congrats! You've successfully reached the leaderboard page!!"""

    def __init__(self, filePath):
        """ TESTING PURPOSES ONLY...the class constructor.""" 
        
        # self.button_name = button_name
        self.filePath = filePath  
        super().__init__()
        
        # # code for the button
        # self.manager = arcade.gui.UIManager()
        # self.manager.enable()
        # # Create a vertical BoxGroup to align buttons
        # self.v_box = arcade.gui.UIBoxLayout()

        # # Create the button
        # start_button = arcade.gui.UIFlatButton(text="Return to Menu", width=200)
        # self.v_box.add(start_button.with_space_around(bottom=20))

        # # assign self.on_click_start as callback
        # start_button.on_click = self.on_click_start
        
        # # Create a widget to hold the v_box widget, that will center the buttons
        # self.manager.add(
        #     arcade.gui.UIAnchorWidget(
        #         anchor_x="center_x",
        #         anchor_y="center_y",
        #         child=self.v_box)
        # )

    def on_show(self):
        """ TESTING PURPOSES ONLY...sets the background color of the instruction menu."""   
        arcade.set_background_color(arcade.color.BLACK)

    # def on_click_start(self, event):
    #     """ When button is clicked do this"""
    #     print('you clicked button')
    #     # view = StartMenu()
    #     # self.window.show_view(view)

    def on_draw(self):
        """TESTING PURPOSES ONLY... creates the view for the instruction menu."""
        start_x = 50
        start_y = 400
        arcade.start_render()
        #button
        #self.manager.draw()

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

        #best_player = data[data.time == data.time.min()].get_loc()
        #idx = idx.get_loc(best_score)
        #best_player = get_name[data[0]]
        #best_player = data['time'].min()[data['name']].selct_dtypes('number')

        # get_name = data.set_index(['name', 'time']).select_dtypes('number')
        #best_player = pd.Series(get_name)
        # best_player = get_name.idxmin()

        # arcade.draw_text(f'The best time is {best_score} by {best_player}, then next is {best_score2} by {best_player2}, then next is {best_score3} by {best_player3}',
        #                  constants.SCREEN_HEIGHT/3,
        #                  constants.SCREEN_WIDTH/4,
        #                  arcade.color.WHITE_SMOKE,
        #                  font_size=20)

        # arcade.draw_text(f'#1 {best_score} by {best_player}, then next is {best_score2} by {best_player2}, then next is {best_score3} by {best_player3}',
        #                  constants.SCREEN_HEIGHT/3,
        #                  constants.SCREEN_WIDTH/4,
        #                  arcade.color.WHITE_SMOKE,
        #                  font_size=20)

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

    def draw_score(text, height):
        """ draw the text labels for the scores onto the screen"""
        arcade.draw_text(text,
                    constants.SCREEN_WIDTH * 0.75 - 230,
                    constants.SCREEN_HEIGHT * height -20,
                    arcade.color.WHITE_SMOKE,
                    font_size=15,
                    anchor_x="center")



# filename = (str(Path(__file__).parent.resolve()) + "\\leaderboard.csv")
# data = pd.read_csv(filename)
# data.sort_values(by ="name", ascending=True)
# print (data.sort_values(by ="time", ascending=True).head(10))




# window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
# leader = LeaderView()
# window.show_view(leader)
# arcade.run()



# Sources: 
# https://www.stackvidhya.com/get-value-of-cell-from-a-pandas-dataframe/#:~:text=You%20can%20get%20the%20value,iat%5B0%2C0%5D%20.
# https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/
# https://realpython.com/pandas-sort-python/#sorting-your-dataframe-on-multiple-columns
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
