# zoom_web_lrg
Zoom Web Linux large version, this is intended for the Rapsberry Pi due to there not being a RPI Zoom client. 
Enter the zoom meeting number, press enter, then you will be directed to the web client for that meeting ID.

![Screenshot 2021-09-19 174340](https://user-images.githubusercontent.com/86476845/133935675-afec42e7-6a76-49a2-ad28-33643b3738c4.png)

# Dependencies required:
git
python3
pip
tkinter


# Installation in linux terminal (Debian/Ubuntu):
Updates and dependency installation
```
sudo apt update -y && sudo apt full-upgrade -y && sudo apt dist-upgrade -y && sudo apt install git python3 python3-pip python-tk python3-tk -y
```

Zoom Web installation
```
git clone https://github.com/OishiiCha/zoom_web_lrg.git && cd zoom_web_lrg && python3 desktop_file.py

```
