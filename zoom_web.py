from tkinter import *
import time
import webbrowser

 # Ratio settings (for future resizing)
ratio_w = 11
ratio_h = 6

# Window
root = Tk()
root.geometry("550x300")
root.title("Zoom Web")
root.resizable(width=False, height=False)

# Font
myfont = ("Arial", 20)

# Functions
def enter_data():
    txt_name = ent.get()
    meeting_id = txt_name.replace(" ", "")
    if len(meeting_id) in (10,11):
        link = "https://pwa.zoom.us/wc/join/" + meeting_id
        error_message = Label(root, text="                                                     ")
        error_message.grid(row=5, columnspan=2)
        error_message.config(font=myfont)
        time.sleep(1)
        webbrowser.open(link, 1)
    else:
        error_message = Label(root, text="Please enter a valid meeting ID")
        error_message.grid(row=5, columnspan=2)
        error_message.config(font=myfont)

# Variables
spacer = Label(root, text = "")
spacer2 = Label(root, text = "")
spacer3 = Label(root, text = "")
m_id = Label(root, text = "     Meeting ID:    ")
btn = Button(root, text="Enter", bg="dodger blue", fg="white", command=enter_data)
ent = Entry(root, justify='center')

# Variable Grids
m_id.grid(row=1)
spacer.grid(row=0)
spacer2.grid(row=2)
spacer3.grid(row=4)
ent.grid(row=1, column=1)
btn.grid(row=3, columnspan=2)

# Variable Configuration
m_id.config(font=myfont)
spacer.config(font=myfont)
spacer2.config(font=myfont)
spacer3.config(font=myfont)
ent.config(font=myfont)
btn.config(font=myfont)

# Main
root.mainloop()
