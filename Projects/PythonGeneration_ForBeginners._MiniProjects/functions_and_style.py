import tkinter as tk
from tkinter.ttk import Style
from tkinter import font
from PIL import Image, ImageTk

"""
CENTER DIFFERENT WINDOWS IN TKINTER APP FUNCTION
"""


def center_window_tk(app_width, app_height, root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")


"""
GET GEY FROM VALUE IN DICTIONARY FUNCTION
"""


def get_key_from_value(value, dictionary: dict):
    k = [k for k, v in dictionary.items() if v == value]
    if k:
        return k[0]
    else:
        return None


"""
PLAY GIF ANIMATION IN TKINTER APP FUNCTION
"""


def play_gif(root, lbl, img):

    gif_file = Image.open(img)

    gif_frames = [
        (gif_file.seek(i), gif_file.copy())[1] for i in range(gif_file.n_frames)
    ]

    frame_delay = gif_file.info["duration"]

    counts_of_frames = len(gif_frames)

    frame_count = 0

    current_frame = gif_frames[frame_count]

    def wrapper():
        nonlocal frame_count, current_frame, counts_of_frames, gif_frames, frame_delay

        if frame_count >= counts_of_frames:
            frame_count = 0
            wrapper()

        else:
            current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
            lbl.config(image=current_frame)
            frame_count += 1

            root.after(frame_delay, wrapper)

    wrapper()


"""
CREATE STYLE FOR DIFFERENT TABS AND FUNCTION TO CHANGE STYLE
"""

tabs_color_list = ("#7fcbff", "white", "black", "#65da65", "#ffe3af", "#a2a2a2")


class TabsStyle:
    def __init__(self):
        self.style_sets = {
            0: "GuessNumber",
            1: "Hangman",
            2: "Ball8",
            3: "PassworGeneration",
            4: "CaesarCipher",
            5: "NumberConverter",
        }

        self.style = Style()

        for i in range(len(tabs_color_list)):
            self.style.theme_create(
                self.style_sets[i],
                parent="alt",
                settings={
                    "TCombobox": {
                        "configure": {
                            "selectbackground": "#28a428",
                            "fieldbackground": "#32cd32",
                            "background": "#32cd32",
                            "bordercolor": "#32cd32",
                            "foreground": "#253529",
                            "arrowsize": 15,
                            "arrowcolor": "#253529",
                        }
                    },
                    "TNotebook": {"configure": {"tabmargins": [6, 5, 2, 0]}},
                    "TNotebook.Tab": {
                        "configure": {"padding": [8, 5], "background": "#f0f8ff"},
                        "map": {
                            "background": [("selected", tabs_color_list[i])],
                            "foreground": [
                                ("selected", f"{'white' if i == 2 else 'black'}")
                            ],
                            "expand": [("selected", [3, 3, 3, 3])],
                        },
                    },
                },
            )

    def change_style(self, idx):
        self.style.theme_use(self.style_sets[idx])


"""
APP FOR CHOOSING FONT STYLE TO TAB, PROCESSING IMGS FOR APP
"""

if __name__ == "__main__":

    # MAKE APP FOR CHOOSING font for OUR app
    font_look_window = tk.Tk()
    font_look_window.geometry("480x480")
    frame = tk.Frame(font_look_window, width=800, height=275)
    frame.pack()
    frame.grid_propagate(0)
    frame.columnconfigure(0, weight=15)
    our_text = font.Font(family="Arial", size=25)

    def change_font(e):
        our_text.config(family=list_lbl.get(list_lbl.curselection()))

    text_lbl = tk.Text(frame, font=our_text)
    text_lbl.grid(row=0, column=0)
    text_lbl.rowconfigure(0, weight=1)
    text_lbl.columnconfigure(0, weight=1)

    list_lbl = tk.Listbox(font_look_window, selectmode="single", width=100)
    list_lbl.pack()

    for f in font.families():
        list_lbl.insert(tk.END, f)

    list_lbl.bind("<ButtonRelease-1>", change_font)

    font_look_window.mainloop()

    """CONVERT IMAGE AND CREATE NEGATIVE IMG FOR APP"""
    # image = Image.open('imgs\\NicePng_back-button-png_876153.png')
    # new_image = image.resize((50, 52))
    # new_image.save('imgs\\back_btn.png')

    # # create negative
    # img = Image.open(r'imgs\question_btn.png')
    # neg = ImageOps.invert(img.convert('RGB'))
    # neg.save('imgs\\negativ.png')
