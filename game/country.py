import arcade

class Country():

    def __init__(self, map_img_path):
        self.background = None
        self.window.set_mouse_visible(True)
        self.background = arcade.load_texture(map_img_path)