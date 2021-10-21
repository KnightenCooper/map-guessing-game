import arcade
import constants
from arcade.gui import UIManager

class Timer(arcade.View):

    print("timer")

    def __init__(self, pause_view):    
        super().__init__()
        self.total_time = 0.0
        self.output = "00:00:00"

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.total_time = 0.0
    
    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(self.output,
                        self.window.width/2,
                        self.window.height/2+90,
                        arcade.color.BLACK, 
                        100,
                        anchor_x="center")  

    def on_update(self, delta_time):
        self.total_time += delta_time

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        seconds_100s = int((self.total_time - seconds) * 100)

        self.output = f"{minutes:02d}:{seconds:02d}:{seconds_100s:2d}"


# Sources
# https://api.arcade.academy/en/latest/examples/timer.html
# https://github.com/grant516/cse210-project