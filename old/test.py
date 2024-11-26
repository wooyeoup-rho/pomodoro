from tkinter import *
import math
from tkinter import font

from customtkinter import CTkButton
import pyglet, os, sys

window = Tk()
window.title("Pomodoro")
window.config(width=400, height=600, padx=100, pady=50)

pyglet.options["win32_gdi_font"] = True
font_path = os.path.join(os.path.dirname(__file__), "assets/fonts/PressStart2P-Regular.ttf")
pyglet.font.add_file(font_path)

label = Label(text="Pomodoro", font=("Press Start 2P", 24))
label.grid(row=0,column=1)

animation_platform = Canvas(width=320, height=240, bg="green")
frames = [PhotoImage(file="assets/images/tomato_1.png"), PhotoImage(file="assets/images/tomato_2.png"), PhotoImage(file="assets/images/tomato_3.png"), PhotoImage(file="assets/images/tomato_4.png")]
numbers_of_frames = len(frames)
frame_delay = 200
frame = 0
animation_platform.create_image(0,0, anchor="nw", image=frames[frame], tag="animation")
animation_platform.grid(row=1,column=1)

def animation():
    global frame
    if frame < numbers_of_frames-1:
        frame += 1
    else:
        frame = 0
    animation_platform.itemconfigure('animation', image=frames[frame])
    window.after(frame_delay, animation)

window.after(frame_delay, animation)

window.mainloop()