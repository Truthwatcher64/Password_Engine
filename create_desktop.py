import os

def one_method():
    holder=os.getlogin()

    #Create the .desktop
    text_sequence="[Desktop Entry]\n"
    text_sequence.__add__("Terminal=false\nType=Application")
    text_sequence.__add__("Exec=/usr/bin/python3 /home/"+holder+"/.password_engine/window_launcher.py")
    text_sequence.__add__("Name=Password Engine")
    text_sequence.__add__("Icon=/home/"+holder+"/.password_engine/icon_square.png")
    with open("home/"+holder+"/Downloads/Password_Engine_Master/password_engine.desktop", "w") as file:
        file.write(text_sequence)

one_method()