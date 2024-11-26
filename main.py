from tkinter import *
import math
import pyglet, os, sys

# ---------------------------- RESOURCE PATH ------------------------------- #
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------------------- FONT ------------------------------- #
pyglet.options["win32_gdi_font"] = True
font_path = resource_path("assets/fonts/PressStart2P-Regular.ttf")
pyglet.font.add_file(font_path)

# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_BG = "#FEF3E2"
LIGHT_ONE = "#FAB12F"
LIGHT_TWO = "#FA812F"
LIGHT_THREE = "#FA4032"

DARK_BG = "#1F2544"
DARK_ONE = "#FFD0EC"
DARK_TWO = "#81689D"
DARK_THREE = "#474F7A"

FONT_NAME = "Press Start 2P"

INACTIVE_FONT_COLOR = "#FFFFFF"
ACTIVE_FONT_COLOR = "#CACACA"
DISABLED_FONT_COLOR = "#7D7D7D"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

FRAME_DELAY = 200

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global active_image
    global active_timer

    reps = 0

    if active_timer:
        window.after_cancel(timer)

    session_label.config(text="Timer")
    timer_text.config(text="00:00")
    count_label.config(text="")
    start_button.configure(
        command=start,
        image=active_image,
        fg=INACTIVE_FONT_COLOR,
        activeforeground=ACTIVE_FONT_COLOR
    )

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global disabled_image
    global active_timer
    active_timer = True

    start_button.configure(
        command=NONE,
        image=disabled_image,
        fg=DISABLED_FONT_COLOR,
        activeforeground=DISABLED_FONT_COLOR
    )
    start_timer()

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        session_label.config(text="Work", fg=color_one)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        session_label.config(text="Long Break", fg=color_three)
    else:
        count_down(short_break_sec)
        session_label.config(text="Short Break", fg=color_two)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_seconds = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    timer_text.config(text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global reps
        count_label.config(text="✔" * int(reps / 2))
        start_timer()
        bring_to_front()

# ---------------------------- ANIMATION ------------------------------- #
def animation():
    global frame
    if frame < numbers_of_frames-1:
        frame += 1
    else:
        frame = 0
    canvas.itemconfigure("animation", image=frames[frame])
    window.after(FRAME_DELAY, animation)

# ---------------------------- UTILITY ------------------------------- #
def toggle_light():
    global bg_color
    global color_one
    global color_two
    global color_three
    global frames
    global active_image
    global disabled_image
    global toggle_image

    light_mode = False if bg_color == LIGHT_BG else True

    frames = [
        PhotoImage(file=resource_path("assets/images/tomato_dark_1.png")),
        PhotoImage(file=resource_path("assets/images/tomato_dark_2.png")),
        PhotoImage(file=resource_path("assets/images/tomato_dark_3.png")),
        PhotoImage(file=resource_path("assets/images/tomato_dark_4.png"))
    ] if bg_color == LIGHT_BG else [
        PhotoImage(file=resource_path("assets/images/tomato_1.png")),
        PhotoImage(file=resource_path("assets/images/tomato_2.png")),
        PhotoImage(file=resource_path("assets/images/tomato_3.png")),
        PhotoImage(file=resource_path("assets/images/tomato_4.png"))
    ]

    toggle_image = PhotoImage(file=resource_path("assets/images/toggle_button_light.png"))\
        if light_mode else PhotoImage(file=resource_path("assets/images/toggle_button_dark.png"))
    active_image = PhotoImage(file=resource_path("assets/images/light_button.png"))\
        if light_mode else PhotoImage(file=resource_path("assets/images/dark_button.png"))
    disabled_image = PhotoImage(file=resource_path("assets/images/light_button_disabled.png"))\
        if light_mode else PhotoImage(file=resource_path("assets/images/dark_button_disabled.png"))

    bg_color = LIGHT_BG if light_mode else DARK_BG
    color_one = LIGHT_ONE if light_mode else DARK_ONE
    color_two = LIGHT_TWO if light_mode else DARK_TWO
    color_three = LIGHT_THREE if light_mode else DARK_THREE

    window.config(bg=bg_color)
    canvas.config(bg=bg_color)
    session_label.config(fg=color_one, bg=bg_color)
    toggle_button.config(
        bg=bg_color,
        activebackground=bg_color,
        image=toggle_image
    )
    start_button.config(
        fg=INACTIVE_FONT_COLOR if not active_timer else DISABLED_FONT_COLOR,
        activeforeground=ACTIVE_FONT_COLOR if not active_timer else DISABLED_FONT_COLOR,
        bg=bg_color,
        activebackground=bg_color,
        image=active_image if not active_timer else disabled_image
    )
    reset_button.config(
        fg=INACTIVE_FONT_COLOR,
        activeforeground=ACTIVE_FONT_COLOR,
        bg=bg_color,
        activebackground=bg_color,
        image=active_image
    )
    count_label.config(fg=color_one, bg=bg_color)
    timer_text.config(fg=color_one, bg=bg_color)

def bring_to_front():
    window.deiconify()
    window.lift()
    window.focus_force()

# ---------------------------- UI SETUP ------------------------------- #
reps = 0
frame = 0
timer = None
active_timer = False

bg_color = LIGHT_BG
color_one = LIGHT_ONE
color_two = LIGHT_TWO
color_three = LIGHT_THREE

window = Tk()
window.title("Pomodoro")
window.config(width=800, height=600, padx=20, pady=20, bg=bg_color)

icon_photo = PhotoImage(file=resource_path("assets/images/pomodoro.png"))
window.iconphoto(False, icon_photo)

session_label = Label(text="Timer", font=(FONT_NAME, 32), fg=color_one, bg=bg_color)
session_label.grid(row=1,column=0, columnspan=3)

frames = [
    PhotoImage(file=resource_path("assets/images/tomato_1.png")),
    PhotoImage(file=resource_path("assets/images/tomato_2.png")),
    PhotoImage(file=resource_path("assets/images/tomato_3.png")),
    PhotoImage(file=resource_path("assets/images/tomato_4.png"))
]
numbers_of_frames = len(frames)

active_image = PhotoImage(file=resource_path("assets/images/light_button.png"))
disabled_image = PhotoImage(file=resource_path("assets/images/light_button_disabled.png"))
toggle_image = PhotoImage(file=resource_path("assets/images/toggle_button_light.png"))

canvas = Canvas(width=320, height=240, bg=bg_color, highlightthickness=0)
canvas.create_image(0,0, anchor="nw", image=frames[frame], tag="animation")
canvas.grid(row=2, column=1)

timer_text = Label(text="00:00", font=(FONT_NAME, 24, "bold"), fg=color_one, bg=bg_color)
timer_text.grid(row=3, column=1)

count_label = Label(text="", font=(FONT_NAME, 12), fg=color_one, bg=bg_color)
count_label.grid(row=4, column=1)

toggle_button = Button(
    window,
    bg=bg_color,
    fg=INACTIVE_FONT_COLOR,
    activebackground=bg_color,
    activeforeground=ACTIVE_FONT_COLOR,
    width=64,
    height=64,
    borderwidth=0,
    highlightthickness=0,
    image=toggle_image,
    command=toggle_light
)
toggle_button.grid(row=1, column=0, sticky="w")

start_button = Button(
    window,
    bg=bg_color,
    fg=INACTIVE_FONT_COLOR,
    activebackground=bg_color,
    activeforeground=ACTIVE_FONT_COLOR,
    width=150,
    height=80,
    borderwidth=0,
    highlightthickness=0,
    image=active_image,
    text="Start",
    font=(FONT_NAME, 16, "bold"),
    compound="center",
    command=start
)
start_button.grid(row=3,column=0)

reset_button = Button(
window,
    bg=bg_color,
    fg=INACTIVE_FONT_COLOR,
    activebackground=bg_color,
    activeforeground=ACTIVE_FONT_COLOR,
    width=150,
    height=80,
    borderwidth=0,
    highlightthickness=0,
    image=active_image,
    text="Reset",
    font=(FONT_NAME, 16, "bold"),
    compound="center",
    command=reset_timer
)
reset_button.grid(row=3, column=2)

window.after(FRAME_DELAY, animation)

window.mainloop()