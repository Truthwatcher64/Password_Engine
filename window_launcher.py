#!/usr/bin/python3

import gi
import random
#import warnings
#warnings.filterwarnings('ignore')
import os

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class MyCheckbox(Gtk.CheckButton):
    def __init__(self, label, value):
        super().__init__(label)
        self.value = value
        self.connect("toggled", self.on_checkbox_toggled)

    def on_checkbox_toggled(self, checkbox):
        if checkbox.get_active():
            # print("Checkbox is checked. Value:", self.value)
            self.value = 1
        else:
            # print("Checkbox is checked. Value:", self.value)
            self.value = 0


class BasicWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Password Engine")
        self.set_default_size(480, 350)

        # grid
        grid = Gtk.Grid()
        self.add(grid)
        second_grid = Gtk.Grid()
        third_grid = Gtk.Grid()

        # Explanation(Label)
        explanation = Gtk.Label()
        explanation.set_text("Enter Length of Password")
        explanation.set_margin_top(5)
        explanation.set_margin_bottom(5)
        explanation.set_margin_left(10)
        explanation.set_margin_right(10)

        # Explanation2(Label)
        label_improve = Gtk.Label()
        label_improve.set_text("Enter a password and use this to improve the strength")
        label_improve.set_margin_top(8)
        label_improve.set_margin_bottom(5)
        label_improve.set_margin_left(10)
        # explanation.set_margin_right(10)

        # Entry Box(entry)
        length_entry = Gtk.Entry()
        length_entry.set_margin_top(3)
        length_entry.set_margin_bottom(8)
        length_entry.set_margin_left(150)
        length_entry.set_margin_right(150)
        length_entry.set_text("18")

        # Checkboxes(CheckBox(Gtk.Checkbox))
        # Create a checkbox with associated value
        checkbox_1 = MyCheckbox("Only Letters and Numbers", 0)
        checkbox_1.set_margin_left(10)

        checkbox_2 = MyCheckbox("Only !@#$%^&*()-_+={}[];:<>? as potential symbols", 0)
        checkbox_2.set_margin_bottom(8)
        checkbox_2.set_margin_left(10)

        # randomly produces characters up to the required length (Used in Process 1)
        def makePass(length) -> str:
            num = int(length)
            nPass = ""
            total = 0

            # get the full length
            while (total < num):
                # reset the random generator
                randomTemp = random.randint(1, 5)
                count = 0
                while (count <= randomTemp):
                    ran = random.randint(33, 126)

                    # limitercheck
                    if checkbox_1.value == 1:
                        while not chr(ran).isalnum():
                            # while ((ran<47 and ran>58) or (ran<64 and ran>91) or (ran<96 and ran>123)):
                            ran = random.randint(33, 126)
                    elif checkbox_2.value == 1:
                        while (
                                ran == 34 or ran == 39 or ran == 44 or ran == 46 or ran == 96 or ran == 126 or ran == 47 or ran == 92 or ran == 124):
                            ran = random.randint(33, 126)

                    tempChar = chr(ran)
                    nPass = nPass + tempChar
                    count += 1
                    total += 1
            return nPass

        # takes in one character and changes it or it may not change it (Used in Process 2)
        def scrambler(char1):
            num = ord(char1)
            # Aa@
            if (num == 65 or num == 97):
                ran_num = random.randint(0, 3)
                if (ran_num == 0):
                    num = 64
                else:
                    num = num
            # Ii!
            elif (num == 73 or num == 105):
                ran_num = random.randint(0, 3)
                if (ran_num == 0):
                    num = 33
                else:
                    num = num
            # Ss$
            elif (num == 83 or num == 115):
                ran_num = random.randint(0, 3)
                if (ran_num == 0):
                    num = 36
                elif (ran_num == 1):
                    num = 53
                else:
                    num = num
            # Zz2
            elif (num == 90 or num == 122):
                ran_num = random.randint(0, 2)
                if (ran_num == 0):
                    num = 36
                else:
                    num = num
            # 8&
            elif (num == 56):
                ran_num = random.randint(0, 2)
                if (ran_num == 0):
                    num = 38
                else:
                    num = num
            # Ee3
            elif (num == 69 or num == 101):
                ran_num = random.randint(0, 2)
                if (ran_num == 0):
                    num = 51
                else:
                    num = num
            return chr(num)

        # when the improve_pass_button is clicked, takes in the input box and sends new password to the output box
        def improve_pass_button_clicked(button):
            input_text = start_pass_1.get_text()
            input_string = str(input_text)
            output_string = ""
            for i in range(0, input_string.__len__()):
                output_string = output_string + scrambler(input_string[i])

            end_pass_1.set_text(output_string)

        # Input for Function to original password (Entry)
        start_pass_1 = Gtk.Entry()
        start_pass_1.set_margin_top(10)
        start_pass_1.set_margin_bottom(7)
        start_pass_1.set_margin_left(10)
        # explanation.set_margin_right(10)

        # When clicked takes the password from start_pass_1 and outputs an improved version in end_pass_1 (Button)
        improve_pass_button = Gtk.Button(label="Improve")
        improve_pass_button.connect("clicked", improve_pass_button_clicked)
        # explanation.set_margin_top(5)
        improve_pass_button.set_margin_bottom(7)
        improve_pass_button.set_margin_left(80)
        improve_pass_button.set_margin_right(80)

        # output of an improved password (Entry)
        end_pass_1 = Gtk.Entry()
        # explanation.set_margin_top(5)
        end_pass_1.set_margin_bottom(10)
        end_pass_1.set_margin_left(10)

        # explanation.set_margin_right(10)

        # makes the password and outputs the new result (Used in Process 1)
        def randomPassButton_click(button):
            if (length_entry.get_text() == ""):
                newPass = makePass(18)
            else:
                newPass = makePass(length_entry.get_text())
            text_buffer = outputBox.get_buffer()
            text_buffer.set_text("")
            text_buffer.insert_at_cursor(newPass)

        # button that executes make a new random password (Button)
        randomPassButton = Gtk.Button(label="Generate")
        randomPassButton.connect("clicked", randomPassButton_click)
        randomPassButton.set_margin_top(5)
        randomPassButton.set_margin_bottom(5)
        randomPassButton.set_margin_left(20)
        randomPassButton.set_margin_right(20)

        # outputs that new password (Textview)
        outputBox = Gtk.TextView()
        outputBox.set_editable(True)
        outputBox.set_margin_top(20)
        outputBox.set_margin_bottom(20)

        # part Three
        # Pulls a random word from the document of saved words
        def random_word():
            holder=os.getlogin()
            #print(holder)
            num = random.randint(0, 113808)
            full_path='/home/'+holder+'/.password_engine/word_list.txt'
            with open(full_path, 'r') as file:
                i = 0
                for line in file:
                    # print(line)
                    if (i == num):
                        return line
                    i += 1

        # starts the process of making a random passphrase
        def spawn_button_clicked(button):
            ran_num_1 = random.randint(3, 4)
            new_pass = ""

            # Add words and symbols to the new passphrase
            for i in range(0, ran_num_1):
                word = random_word()
                word_str = str(word)
                new_word = ""
                # Capitalize word and concatonate it
                new_word = new_word + word_str[0].upper()
                for j in range(1, word_str.__len__() - 1):
                    new_word = new_word + word_str[j]
                new_pass = new_pass + str(new_word)

                # Add the symbol or number
                testAgain = random.randint(0, 2)
                for j in range(0, testAgain):
                    ran = random.randint(33, 126)
                    while chr(ran).isalpha():  # .isalnum():
                        # while ((ran<47 and ran>58) or (ran<64 and ran>91) or (ran<96 and ran>123)):
                        ran = random.randint(33, 126)
                        while (
                                ran == 34 or ran == 39 or ran == 44 or ran == 46 or ran == 96 or ran == 126 or ran == 47 or ran == 92 or ran == 124):
                            ran = random.randint(33, 126)
                    tempChar = chr(ran)
                    new_pass = new_pass + tempChar

            output_passphrase.set_text(new_pass)

            # Description of the passphrase

        passphrase_explanation = Gtk.Label()
        passphrase_explanation.set_text("Make a passphrase that is make up of several\n words and letters")
        passphrase_explanation.set_margin_top(10)
        passphrase_explanation.set_margin_bottom(8)
        passphrase_explanation.set_margin_left(40)
        passphrase_explanation.set_margin_right(10)
        # passphrase_explanation.set_halign(Gtk.Justification.LEFT)

        # button that generates a new passphrase
        spawn_button = Gtk.Button(label="Make Phrase")
        spawn_button.connect("clicked", spawn_button_clicked)
        spawn_button.set_margin_top(8)
        spawn_button.set_margin_bottom(7)
        spawn_button.set_margin_left(45)
        spawn_button.set_margin_right(10)

        # Entry that shows the output from the passphrase generation
        output_passphrase = Gtk.Entry()
        # output_passphrase.set_margin_top(8)
        output_passphrase.set_margin_bottom(12)
        output_passphrase.set_margin_left(40)

        # output_passphrase.set_margin_right(10)

        def switch_function(widget, current_grid, new_grid):
            # Remove the current vbox from the window
            window.remove(current_grid)

            # Add the new vbox to the window
            window.add(new_grid)

            # Update the current_vbox reference
            current_grid = new_grid

            # Show the changes
            window.show_all()

        # Switch function buttons: Each is created and has a link to another of the pages
        fun_2_1_button = Gtk.Button(label="Make Password")
        fun_2_1_button.connect("clicked", switch_function, second_grid, grid)

        fun_2_3_button = Gtk.Button(label="Passphrase")
        fun_2_3_button.connect("clicked", switch_function, second_grid, third_grid)

        fun_1_2_button = Gtk.Button(label="Strengthen Password")
        fun_1_2_button.connect("clicked", switch_function, grid, second_grid)

        fun_1_3_button = Gtk.Button(label="Passphrase")
        fun_1_3_button.connect("clicked", switch_function, grid, third_grid)

        fun_3_1_button = Gtk.Button(label="Make Password")
        fun_3_1_button.connect("clicked", switch_function, third_grid, grid)

        fun_3_2_button = Gtk.Button(label="Strengthen Password")
        fun_3_2_button.connect("clicked", switch_function, third_grid, second_grid)

        # Grid Layout 1 (Make Random Password)
        grid.attach(explanation, 0, 0, 3, 1)
        #grid.attach_next_to(length_entry, explanation, Gtk.PositionType.BOTTOM, 3, 1)
        grid.attach(length_entry, 0, 1, 3, 1)
        grid.attach(checkbox_1, 0, 2, 1, 1)
        grid.attach(checkbox_2, 0, 3, 1, 1)
        grid.attach(randomPassButton, 0, 4, 1, 1)
        grid.attach(outputBox, 0, 5, 1, 1)

        tempBox = Gtk.Box(spacing=10)
        tempBox.pack_start(fun_1_2_button, True, True, 0)
        tempBox.pack_start(fun_1_3_button, True, True, 0)
        grid.attach(tempBox, 0, 6, 1, 1)

        # grid.attach(fun_1_2_button, 0, 6, 1, 1)
        # grid.attach(fun_1_3_button, 1, 6, 1, 1)
        # grid.attach_next_to(fun_1_3_button, fun_1_2_button, Gtk.PositionType.RIGHT, 1, 1)

        # Grid layout2 strengthen existing password
        second_grid.attach(label_improve, 0, 0, 3, 1)
        second_grid.attach(start_pass_1, 0, 1, 3, 1)
        second_grid.attach(improve_pass_button, 0, 2, 3, 1)
        second_grid.attach(end_pass_1, 0, 3, 3, 1)
        tempBox2 = Gtk.Box(spacing=10)
        tempBox2.pack_start(fun_2_1_button, True, True, 0)
        tempBox2.pack_start(fun_2_3_button, True, True, 0)
        tempBox2.set_halign(Gtk.Align.CENTER)
        tempBox2.set_margin_left(50)
        second_grid.attach(tempBox2, 0, 4, 1, 1)

        # Grid layout3 make a passphrase
        third_grid.attach(passphrase_explanation, 0, 0, 2, 1)
        third_grid.attach(spawn_button, 0, 1, 2, 1)
        third_grid.attach(output_passphrase, 0, 2, 3, 1)
        tempBox3 = Gtk.Box(spacing=10)
        tempBox3.pack_start(fun_3_1_button, True, True, 0)
        tempBox3.pack_start(fun_3_2_button, True, True, 0)
        tempBox3.set_margin_left(40)
        third_grid.attach(tempBox3, 0, 6, 1, 1)


window = BasicWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
