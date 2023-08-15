chmod +x password_engine.desktop
cp password_engine.desktop /home/truth/.local/share/applications/
chmod +x uninstall_linux.sh
chmod +x organize_linux.sh
#installs the desktop file to get it to work
desktop-file-install --dir=/home/truth/.local/share/applications password_engine.desktop
chmod +x window_launcher.py
cd ..
cp -a Password_Engine-main /home/truth/.password_engine
