"""
Class for CountryIcons
"""
import arcade
from pathlib import Path


class CountryClickableIcons(arcade.Sprite):
    """ Country sprite """

    def __init__(self, country_name, scale=1):
        """ Country constructor """

        # This country_name will represent the country and be its name, This is important when we determine if the user clicked the right country
        self.country_name = country_name
        # The below line of code uses the country's name to automatically get the correct icon for Demo.
        self.image_file_name = str(Path(__file__).parent.resolve()) + f"\\assets\\black-square.png"

        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")


# Source: 
# https://api.arcade.academy/en/latest/tutorials/card_game/index.html