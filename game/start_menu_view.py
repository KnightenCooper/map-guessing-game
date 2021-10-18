""" COMMENT GOES HERE"""


import random
import arcade
from arcade.gui import UIManager
from leaderboard import LeaderView

music_volume = 0.5

class start_menu(arcade.View):
    """ The first menu the user sees that allows them to choose which of the six continent games they want to play 
    or view that continent's leaderboard"""

    def __init__(self):
        """ initialized self""" 
        super().__init__()

        self.ui_manager = UIManager()
        self.view = None



    def on_draw(self):
        """ Adds the text to the menu. The text is the name of each continent and is to the left of each set of buttons"""
        arcade.start_render()
        self.ui_manager.on_draw()

        arcade.draw_text("North America:",
                         self.window.width * 0.75 -230,
                         self.window.height*.9 -20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("South America:",
                         self.window.width * 0.75 -230,
                         self.window.height*.75-20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Australia:",
                         self.window.width * 0.75 -230,
                         self.window.height *.6 -20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Asia:",
                         self.window.width * 0.75 -230,
                         self.window.height*.45-20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Africa:",
                         self.window.width * 0.75 -230,
                         self.window.height*.3-20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")
        arcade.draw_text("Europe:",
                         self.window.width * 0.75 -230,
                         self.window.height*.15-20,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center")


    def on_show_view(self):
        """ makes the background white"""
        self.setup()
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ creates all 12 buttons. Each continent gets 2 buttons. One button for 'New Game' and one for 'Leaderboard'
        The new game button will start that continents game and the leaderboard button will take the user to that continent's leaderboard system."""
        self.ui_manager.purge_ui_elements()

        # creates the textures for the buttons so they're interactive
        button_normal = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_normal.png')
        hovered_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_hover.png')
        pressed_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_press.png')

        # creates the North America buttons.
        self.button_game_north_america = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.9,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_north_america)
        # when clicked this button calls the 'on_click_button_game_north_america' function
        self.button_game_north_america.on_click = self.on_click_button_game_north_america


        self.on_button_leaderboard_north_america = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.9,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_north_america)
        # when clicked this button calls the 'on_click_button_leaderboard_north_america' function
        self.on_button_leaderboard_north_america.on_click = self.on_click_button_leaderboard_north_america

        # creates the South America buttons.
        self.button_game_south_america = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.75,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_south_america)
        # when clicked this button calls the 'on_click_button_game_south_america' function
        self.button_game_south_america.on_click = self.on_click_button_game_south_america


        self.on_button_leaderboard_south_america = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.75,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_south_america)
        # when clicked this button calls the 'on_click_button_leaderboard_south_america' function
        self.on_button_leaderboard_south_america.on_click = self.on_click_button_leaderboard_south_america
    
        # creates the Australia buttons.
        self.button_game_australia = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.6,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_australia)
        # when clicked this button calls the 'on_click_button_leaderboard_australia' function
        self.button_game_australia.on_click = self.on_click_button_game_australia


        self.on_button_leaderboard_australia = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.6,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_australia)
        # when clicked this button calls the 'on_click_button_leaderboard_australia' function
        self.on_button_leaderboard_australia.on_click = self.on_click_button_leaderboard_australia

        # creates the Asia buttons.
        self.button_game_asia = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.45,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_asia)
        # when clicked this button calls the 'on_click_button_game_asia' function
        self.button_game_asia.on_click = self.on_click_button_game_asia


        self.on_button_leaderboard_asia = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.45,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_asia)
        # when clicked this button calls the 'on_click_button_leaderboard_asia' function
        self.on_button_leaderboard_asia.on_click = self.on_click_button_leaderboard_asia

        # creates the Africa buttons.
        self.button_game_africa = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.3,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_africa)
        # when clicked this button calls the 'on_click_button_game_africa' function
        self.button_game_africa.on_click = self.on_click_button_game_africa


        self.on_button_leaderboard_africa = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.3,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_africa)
        # when clicked this button calls the 'on_click_button_leaderboard_africa' function
        self.on_button_leaderboard_africa.on_click = self.on_click_button_leaderboard_africa

        # creates the Europe buttons.
        self.button_game_europe = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75,
            center_y = self.window.height*.15,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button_game_europe)
        # when clicked this button calls the 'on_click_button_game_europe' function
        self.button_game_europe.on_click = self.on_click_button_game_europe


        self.on_button_leaderboard_europe = arcade.gui.UIImageButton(
            center_x = self.window.width * 0.75 + 190,
            center_y = self.window.height*.15,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Leaderboard'
        )
        self.ui_manager.add_ui_element(self.on_button_leaderboard_europe)
        # when clicked this button calls the 'on_click_button_leaderboard_europe' function
        self.on_button_leaderboard_europe.on_click = self.on_click_button_leaderboard_europe


    def on_click_button_game_north_america(self):
        """ function called when north america's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('north america new game button pressed')

    def on_click_button_leaderboard_north_america(self):
        """ function called when north america's 'Leaderboard' button is clicked on"""
        self.ui_manager.purge_ui_elements()
        #print('north america leaderboard button pressed')
        instruction = LeaderView(self)
        self.window.show_view(instruction)

    def on_click_button_game_south_america(self):
        """ function called when south america's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('south america new game button pressed')

    def on_click_button_leaderboard_south_america(self):
        """ function called when south america's 'Leaderboard' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('south america leaderboard button pressed')

    def on_click_button_game_australia(self):
        """ function called when australia's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('australia new game button pressed')

    def on_click_button_leaderboard_australia(self):
        """ function called when australia's 'Leaderboard' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('australia leaderboard button pressed')

    def on_click_button_game_asia(self):
        """ function called when asia's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('asia new game button pressed')

    def on_click_button_leaderboard_asia(self):
        """ function called when asia's 'Leaderboard' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('asia leaderboard button pressed')

    def on_click_button_game_africa(self):
        """ function called when africa's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('africa new game button pressed')

    def on_click_button_leaderboard_africa(self):
        """ function called when africa's 'Leaderboard' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('africa leaderboard button pressed')

    def on_click_button_game_europe(self):
        """ function called when europe's 'New Game' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('europe new game button pressed')

    def on_click_button_leaderboard_europe(self):
        """ function called when europe's 'Leaderboard' button is clicked on"""
        #self.ui_manager.purge_ui_elements()
        print('europe leaderboard button pressed')   

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