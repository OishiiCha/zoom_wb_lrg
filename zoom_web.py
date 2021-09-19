from tkinter import *
import time
import webbrowser

root = Tk()
root.geometry("300x200")
root.title("Zoom Web")
root.resizable(width=False, height=False)



def enter_data():
    txt_name = ent.get()
    meeting_id = txt_name.replace(" ", "")
    if len(meeting_id) in (10,11):
        link = "https://us02web.zoom.us/wc/join/" + meeting_id + "?wpk=wcpk04759071e74dff4c8fcd93dc08777af5"
        error_message = Label(root, text="                                                     ")
        error_message.grid(row=5, columnspan=2)
        time.sleep(1)
        webbrowser.open(link, 1)
    else:
        error_message = Label(root, text="Please enter a valid meeting ID")
        error_message.grid(row=5, columnspan=2)


spacer = Label(root, text = "")
spacer2 = Label(root, text = "")
spacer3 = Label(root, text = "")
m_id = Label(root, text = "     Meeting ID:    ")


ent = Entry(root)

m_id.grid(row=1)
spacer.grid(row=0)
spacer2.grid(row=2)
spacer3.grid(row=4)


ent.grid(row=1, column=1)

btn = Button(root, text="Enter", bg="grey", fg="white", command=enter_data)
btn.grid(row=3, columnspan=2)


root.mainloop()
