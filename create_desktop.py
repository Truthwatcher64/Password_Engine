import os

def install_method():
    holder=os.getlogin()

    #Create the .desktop file (password_engine.desktop)
    text_sequence="[Desktop Entry]\n"
    text_sequence=text_sequence+"Terminal=false\nType=Application\n"
    text_sequence=text_sequence+"Exec=/usr/bin/python3 /home/"+holder+"/.password_engine/window_launcher.py\n"
    text_sequence=text_sequence+"Name=Password Engine\n"
    text_sequence=text_sequence+"Icon=/home/"+holder+"/.password_engine/icon.png\n"
    with open("/home/"+holder+"/Downloads/Password_Engine_Master/password_engine.desktop", "w") as file:
        file.write(text_sequence)

def uninstall_method():
    holder=os.getlogin()

    #create an uninstall script (uninstall_linux.sh)
    text_sequence="rm /home/"+holder+"/.local/share/applications/password_engine.desktop\n"
    text_sequence=text_sequence+"rm -r /home/"+holder+"/.password_engine\n"
    with open("/home/"+holder+"/Downloads/Password_Engine_Master/uninstall_linux.sh", "w") as file:
        file.write(text_sequence)


install_method()
uninstall_method()
