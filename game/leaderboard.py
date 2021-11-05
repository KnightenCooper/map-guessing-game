import arcade
import constants
import pandas as pd
from pathlib import Path

# from arcade.gui import UIManager

class LeaderView(arcade.View):
    """ TESTING PURPOSES ONLY... this class creates a page that says 
    Congrats! You've successfully reached the leaderboard page!!"""

    def __init__(self):
        """ TESTING PURPOSES ONLY...the class constructor."""   
        super().__init__()

    def on_show(self):
        """ TESTING PURPOSES ONLY...sets the background color of the instruction menu."""   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """TESTING PURPOSES ONLY... creates the view for the instruction menu."""  
        arcade.start_render()
        arcade.draw_text("LEADERBOARD",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2+90,
                         arcade.color.WHITE,
                         font_size=45,
                         anchor_x="center")
        # Read the csv file and get the fastest time
        filename = (str(Path(__file__).parent.resolve()) + "\\leaderboard.csv")
        data = pd.read_csv(filename)
        best_score = data.time.min()
        #best_player = data[data.time == data.time.min()].get_loc()
        #idx = idx.get_loc(best_score)
        #best_player = get_name[data[0]]
        #best_player = data['time'].min()[data['name']].selct_dtypes('number')

        # get_name = data.set_index(['name', 'time']).select_dtypes('number')
        #best_player = pd.Series(get_name)
        # best_player = get_name.idxmin()

        arcade.draw_text(f'The best time is {best_score} by ]',
                         constants.SCREEN_HEIGHT/3,
                         constants.SCREEN_WIDTH/4,
                         arcade.color.WHITE_SMOKE,
                         font_size=20)


# window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
# leader = LeaderView()
# window.show_view(leader)
# arcade.run()