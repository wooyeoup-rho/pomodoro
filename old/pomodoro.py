from tkinter import *
import math
from customtkinter import CTkButton
import os, sys

# CONSTANTS
LIGHT_BG = "#FEF3E2"
LIGHT_ONE = "#FAB12F"
LIGHT_TWO = "#FA812F"
LIGHT_THREE = "#FA4032"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 6
timer = None
timer_on = False
pause_on = False

if getattr(sys, 'frozen', False):
    # Running as a bundled executable
    application_path = sys._MEIPASS
else:
    # Running in the IDE or directly
    application_path = os.path.dirname(__file__)

image_path = os.path.join(application_path, 'tomato.png')


class Pomodoro:
    def __init__(self, root):
        self.session_label = None
        self.root = root
        self.root.title("Pomodoro")

        self.show_main()

    def show_options(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Label(self.root, text="Options Menu").pack(pady=5)
        Entry(self.root).pack(pady=5)
        Button(self.root, text="Back", command=self.show_main).pack(pady=10)

    def show_main(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.session_label = Label(text="Timer", font=(FONT_NAME, 32), fg=LIGHT_ONE, bg=LIGHT_BG)
        self.session_label.grid(row=1, column=0, columnspan=3)

        self.canvas = Canvas(width=200, height=224, bg=LIGHT_BG, highlightthickness=0)
        self.canvas.create_image(100, 112, image=PhotoImage(file=image_path))
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
        self.canvas.grid(row=2, column=1)

        self.start_button = CTkButton(self.root, text="Start", command=self.start, font=(FONT_NAME, 18, "bold"), width=70, height=30,
                                 fg_color=LIGHT_TWO, hover_color=LIGHT_THREE, border_spacing=5)
        self.start_button.grid(row=3, column=0)

        self.reset_button = CTkButton(self.root, text="Reset", command=self.reset_timer, font=(FONT_NAME, 18, "bold"), width=70,
                                 height=30, fg_color=LIGHT_TWO, hover_color=LIGHT_THREE, border_spacing=5)
        self.reset_button.grid(row=3, column=2)

        self.count_label = Label(text="", font=(FONT_NAME, 12), fg=LIGHT_ONE, bg=LIGHT_BG)
        self.count_label.grid(row=4, column=1)

        self.options_button = Button(text="Options", command=self.show_options)
        self.options_button.grid(row=0, column=2)

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer(self):
        global reps
        global timer_on
        reps = 0
        timer_on = False
        self.root.after_cancel(timer)
        self.session_label.config(text="Timer")
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.count_label.config(text="")
        self.start_button.configure(state="normal")

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer(self):
        global reps
        global timer_on

        if timer_on:
            reps += 1

            work_sec = WORK_MIN * 1
            short_break_sec = SHORT_BREAK_MIN * 1
            long_break_sec = LONG_BREAK_MIN * 1

            if reps % 2 != 0:
                self.count_down(work_sec)
                self.session_label.config(text="Work", fg=LIGHT_ONE)
            elif reps % 8 == 0:
                self.count_down(long_break_sec)
                self.session_label.config(text="Long Break", fg=LIGHT_THREE)
            else:
                self.count_down(short_break_sec)
                self.session_label.config(text="Short Break", fg=LIGHT_TWO)

    def start(self):
        global timer_on
        timer_on = True
        self.start_button.configure(state="disabled")
        self.start_timer()

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_seconds = count % 60

        if count_seconds < 10:
            count_seconds = f"0{count_seconds}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_seconds}")
        if count > 0:
            global timer
            timer = root.after(1000, self.count_down, count - 1)
        else:
            global reps
            self.count_label.config(text="✔" * int(reps / 2))
            self.start_timer()
            self.bring_to_front()

    def bring_to_front():
        root.deiconify()
        root.lift()
        root.focus_force()

root = Tk()
pomodoro = Pomodoro(root)
root.mainloop()