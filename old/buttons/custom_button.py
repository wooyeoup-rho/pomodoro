# CONSTANTS #
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 80

class CustomButton():
    def __init__(self, **kwargs):
        self.canvas = kwargs["canvas"]
        self.inactive = kwargs["inactive_image"]
        self.active = kwargs["active_image"]

        self.button_image = self.canvas.create_image(
            0, 0,
            anchor="nw",
            image=self.inactive
        )

        self.button_text = self.canvas.create_text(
            BUTTON_WIDTH/2, BUTTON_HEIGHT/2,
            text=kwargs["text"],
            fill=kwargs["fill_color"],
            font=kwargs["font"]
        )

        self.canvas.tag_bind(self.button_image, "<ButtonPress>", self.on_press)
        self.canvas.tag_bind(self.button_image, "<ButtonRelease>", self.on_release)
        self.canvas.tag_bind(self.button_image, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.button_image, "<Leave>", self.on_leave)

        # Bind hover and leave events to the text as well
        self.canvas.tag_bind(self.button_text, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.button_text, "<Leave>", self.on_leave)

    def on_press(self, event):
        self.canvas.itemconfig(self.button_image, image=self.active)

    def on_release(self, event):
        self.canvas.itemconfig(self.button_image, image=self.inactive)
        self.execute_command()

    def on_hover(self, event):
        self.canvas.itemconfig(self.button_image, image=self.active)
        self.canvas.config(cursor="hand2")

    def on_leave(self, event):
        self.canvas.itemconfig(self.button_image, image=self.inactive)
        self.canvas.config(cursor="")

    def execute_command(self):
        print("Button clicked!")  # Replace this with your desired action