import tkinter as tk
from tabs_bar import TabsBar
from functions_and_style import center_window_tk


class RootWindow:
    def __init__(
        self,
        width,
        height,
        icon,
        center=True,
        tittle="Python Generation: For Beginners. MiniProjects.",
        resizable=(False, False),
    ):

        self.root = tk.Tk()

        self.root.title(tittle)
        self.root_width = width
        self.root_height = height
        self.root.resizable(*resizable)
        self.root.iconphoto(False, tk.PhotoImage(file=icon))

        if center:
            center_window_tk(app_width=self.root_width, app_height=self.root_height, root=self.root)
        else:
            self.root.geometry(f"{self.root_width}x{self.root_height}")

        self.tabs_bar = TabsBar(root=self.root)

    def draw_widgets(self):
        self.tabs_bar.draw_tabs_bar()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()
