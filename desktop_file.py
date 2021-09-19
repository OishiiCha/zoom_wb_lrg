import getpass
import os

f = open("Zoom_Web.desktop", "x")

usr = str(getpass.getuser())
f.write("[Desktop Entry]\nVersion=1.0\nName=Zoom Web\nComment=Opens Zoom Web Client\nExec=python3 /home/"+ usr +"/zoom_web_py/zoom_web.py\nIcon=/home/"+ usr +"/zoom_web_py/zoom.ico\nTerminal=false\nType=Application\nCategories=Application;")


os.system("mv Zoom_Web.desktop ~/Desktop/")
os.system("cd")
os.system("chmod +x ~/Desktop/Zoom_Web.desktop")
os.system("gio set ~/Desktop/Zoom_Web.desktop metadata::trusted true")
