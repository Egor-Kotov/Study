import tkinter as tk
from functions_and_style import center_window_tk, tabs_color_list
from webbrowser import open_new

reference_text = (
    "Добрый день. После окончания курса -",
    '"Поколение Python": курс для начинающих',
    "ученикам было предложено сделать несколько мини-проектов.",
    "Большинство этих проектов я уже создавал в консоли,",
    "поэтому решил реализовать их в GUI.",
    "Так на свет появилось это чудовище.",
)

# MAKE REFERENCE WINDOW
class ReferenceWindow:

    # MAKE CHILD WINDOW
    def __init__(
        self,
        parent,
        width,
        height,
        center=True,
        tittle="Справка",
        icon=None,
        resizable=(False, False),
    ):
        self.root = tk.Toplevel(parent, background="white")
        self.root.title(tittle)
        self.root_width = width
        self.root_height = height
        self.root.resizable(*resizable)
        self.root.iconphoto(False, tk.PhotoImage(file=icon))

        # CENTER CHILD WINDOW
        if center:
            center_window_tk(self.root_width, self.root_height, self.root)
        else:
            self.root.geometry(f"{self.root_width}x{self.root_height}")

        # ADD TEXT LABEL, ADD LINK LABEL TO TEXT LABELS
        for i in range(len(reference_text)):
            # ADD LINK LABEL TEXT
            if i == 1:
                self.link = tk.Label(
                    self.root,
                    text=reference_text[i],
                    font=("Arial", 15, "underline"),
                    fg="blue",
                    bg="white",
                    cursor="hand2",
                )
                self.link.pack()
                self.link.bind(
                    "<Button-1>",
                    lambda x: open_new("https://stepik.org/course/58852/info"),
                )
            # ADD OTHER TEXT
            else:
                tk.Label(
                    self.root, text=reference_text[i], font=("Arial", 15), bg="white"
                ).pack(fill="both", expand=1)

        # TAKE FOCUS WHEN CHILD WINDOW OPEN
        self.grab_focus()

    # FUNCTION TO TAKE FOCUS
    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()


# MAKE REFERENCE BUTTON
class ReferenceButton:

    # MAKE BUTTON, MASTER == CURRENTLY TAB
    def __init__(self, master, img="imgs\\other_question_btn.png", canvas=0, color="black"):
        if not canvas:
            self.img_btn_q = tk.PhotoImage(file=img)
            self.master = master
            self.r_button = tk.Button(
                master,
                image=self.img_btn_q,
                command=self.reference,
                width=45,
                height=45,
                border=0,
                background=color,
                activebackground=color,
                cursor="hand2",
            )

            # ADD BUTTON
            self.r_button.place(x=674, y=521)

        # ON THE CANVAS, ANOTHER WAY TO DISPLAY WIDGETS
        else:
            self.master = master
            self.canvas = canvas
            self.btn = canvas.create_text(
                697,
                544,
                font=("Arial", 39, "bold"),
                fill="white",
                text="?",
                activefill=color,
            )
            canvas.tag_bind(self.btn, "<1>", self.reference_canvas)

            canvas.bind("<Motion>", self.check_cursor)

    # FUNCTION TO MAKE REFERENCE/CHILD WINDOW, FATHER == CURRENTLY TAB
    def reference(self):
        ReferenceWindow(self.master, 590, 180, icon="imgs\\reference_window_question_btn.png")

    def reference_canvas(self, e):
        ReferenceWindow(self.master, 590, 180, icon="imgs\\reference_window_question_btn.png")

    def check_cursor(self, e):
        bbox = self.canvas.bbox(self.btn)
        if (
            bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[3] > e.y
        ):  # checks whether the mouse is inside the boundrys
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")
