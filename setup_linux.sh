#Makes the .desktop file executable and then copies it to ~/.local/share/applications, uninstall script is also made
chmod +x create_desktop.py
python create_desktop.py

chmod +x password_engine.desktop
cp password_engine.desktop ~/.local/share/applications/
chmod +x uninstall_script.sh



#installs the desktop file to get it to work
desktop-file-install --dir=~/.local/share/applications password_engine.desktop

#Moves files to ~/.password_engine
chmod +x window_launcher.py
cd ..
cp -a Password_Engine_Master ~/.password_engine






