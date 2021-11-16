# Importing arcade module
import arcade
import constants
from arcade.key import BACKSPACE
from pathlib import Path
import csv
from leaderboard import LeaderView

# Creating MainGame class       
class GetNameView(arcade.View):
    def __init__(self):
        self.output = ""
        super().__init__()
  
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(self.output, 1280/2, 720/1.75, arcade.color.BLACK, font_size=20)

        arcade.draw_text("Type name: ", 1280/2 - 150, 720/1.75, arcade.color.BLACK, font_size=20)

        arcade.draw_text("Press \"Enter\" when finished", 1280/2 - 150, 720/2, arcade.color.BLACK, font_size=20)        

    def on_key_press(self, symbol, modifier):
        """ Whenever the user presses a letter add it to the output or remove a letter from output if user presses Backspace"""

        # Checking the button pressed by looping through this array of the alphabet
        alphabet = [arcade.key.A, arcade.key.B, arcade.key.C, arcade.key.D, arcade.key.E, arcade.key.F, arcade.key.G, arcade.key.H, 
        arcade.key.I, arcade.key.J, arcade.key.K, arcade.key.L, arcade.key.M, arcade.key.N, arcade.key.O, arcade.key.P, arcade.key.Q, 
        arcade.key.R, arcade.key.S, arcade.key.T, arcade.key.U, arcade.key.V, arcade.key.W, arcade.key.X, arcade.key.Y, arcade.key.Z]

        # add each letter as the user presses it
        for letter in alphabet:
            if symbol == letter:
                print(chr(letter))
                self.output = self.output + chr(letter)

        # remove the last letter if user hits backspace
        if symbol == BACKSPACE:
            output_string = str(self.output)
            self.output = output_string.rstrip(output_string[-1])

        # if the user hits 'Enter' then add the self.output (the user's inputted name) to the csv file
        if symbol == arcade.key.ENTER:
                # set name to be same as user inputted name
                name = self.output


                # IMPORTANT
                """ the time is hardcoded as 999999999999999 and needs to be the actual time """
                # IMPORTANT


                rows = [name , 9999999999999999999999999]

                #sets the filename equal to a variable
                filename = (str(Path(__file__).parent.resolve()) + "\\leaderboard.csv")

                #opens and appends the data to the file
                with open(filename, 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(rows)
                    print(rows)

                #takes you to the leaderboard
                instruction = LeaderView() 
                self.window.show_view(instruction)

# Sources:
# https://api.arcade.academy/en/latest/arcade.key.html
# https://geekflare.com/python-remove-last-character/
# https://stackoverflow.com/questions/704152/how-can-i-convert-a-character-to-a-integer-in-python-and-viceversa
# https://github.com/mochatek/ReadyOrNot/blob/master/config.py
# https://www.geeksforgeeks.org/python-arcade-handling-keyboard-input/