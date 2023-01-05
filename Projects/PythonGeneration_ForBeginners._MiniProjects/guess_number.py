import tkinter as tk
from random import randint
from functions_and_style import tabs_color_list
from reference import ReferenceButton

# TAB STRUCTURE
class GuessNumberTab:
    def __init__(self, tabs_bar):
        self.tab_color = tabs_color_list[0]

        # CREATE TAB ADD TO TABS_BAR
        self.guess_number_tab = tk.Frame(tabs_bar, background=self.tab_color)
        tabs_bar.add(self.guess_number_tab, text="Угадайка чисел")

        # CREATE REQUIRED VARIABLES
        self.img_canvas = tk.PhotoImage(file="imgs\\guess_number_canvas.png")
        self.N = self.number = self.edge = None
        self.stage_game = self.count_try = 0
        self.notes = (
            (
                f"Добро пожаловать в числовую угадайку.\n В каких пределах Вам загадать число?\n{' ' * 9}От 1 до N включительно:",
                "Введите N и нажмите Enter =)",
                "Введите, пожалуйста, ЧИСЛО от 1 до 1000000 =)",
            ),
            (
                "\n...Загадываю...\n...Загадываю...\n  Угадывайте!\n",
                "Введите загаданное число=)",
                "загаданное число меньше)",
                "загаданное число больше)",
            ),
        )

        # INSTALL WALLPAPER ON TAB - MAKE CANVAS
        self.wallpaper_tab = tk.Canvas(
            self.guess_number_tab, width=720, height=600, bd=0, highlightthickness=0
        )
        self.wallpaper_tab.pack(fill="both", expand=1)
        self.wallpaper_tab.create_image(0, 0, image=self.img_canvas, anchor="nw")

        # CREATE REFERENCE BUTTON AND ADD TO CANVAS
        self.reference_btn = ReferenceButton(
            master=self.guess_number_tab, canvas=self.wallpaper_tab
        )

        # STARTING THE GAME
        self.guess_number_game()

    """ ENTRY FIELD FUNCTON ("ENTER" EVENT PROCESSING)"""

    def entry_field_return(self, *events):
        # TAKE VALUE IN ENTRY FIELD
        self.N = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        # STARTING GAME LOGIC FUNCTION WITH THIS VALUE
        self.play_stage_game(self.stage_game, self.N)

    """GUESS GAME START - CREATING GAME ITEMS, ADD THEM ON CANVAS"""

    def guess_number_game(self):

        self.big_lable = self.wallpaper_tab.create_text(
            355,
            200,
            text=self.notes[self.stage_game][0],
            font=("Comic Sans MS", 22, "bold"),
            anchor="center",
            fill="black",
            tag="del_tag",
        )

        # CREAT ETRY FIELD AND TO CANVAS, MAKE 'ENTER' - EVENT
        self.entry_field = tk.Entry(
            self.guess_number_tab, width=18, font=("Comic Sans MS", 18), bd=2
        )
        self.entry_field.bind("<Return>", self.entry_field_return)
        self.ef_window = self.wallpaper_tab.create_window(
            355, 290, anchor="center", tag="del_tag", window=self.entry_field
        )

        self.hint_label = self.wallpaper_tab.create_text(
            355,
            335,
            text=self.notes[self.stage_game][1],
            font=("Comic Sans MS", 12, "bold"),
            fill="#800000",
            anchor="center",
            tag="del_tag",
        )

        # MAKE RESTART_GAME BUTTON AND ADD TO CANVAS
        self.btn_play_again = tk.Button(
            self.guess_number_tab,
            text="Начать сначала",
            font=("Comic Sans MS", 12),
            width=12,
            bg=self.tab_color,
            borderwidth=2,
            command=self.play_again,
        )
        self.btn = self.wallpaper_tab.create_window(
            355, 390, anchor="center", window=self.btn_play_again, tag="del_tag"
        )

    """GAME LOGIC FUNCTION"""

    def play_stage_game(self, stage_game, guess):

        # STAGE_0 - CREATING A RANGE OF A NUMBER, MAKE A NUMBER
        if stage_game == 0:
            # VALIDITY CHECK
            if not guess.isdigit() or 1 > int(guess) or 1_000_000 < int(guess):
                self.wallpaper_tab.itemconfig(
                    self.hint_label, text=self.notes[self.stage_game][2]
                )
            # MAKE A NUMBER
            else:
                guess = int(guess)
                self.number = randint(1, guess)
                # print(self.number)
                self.edge = guess
                self.stage_game = 1
                self.wallpaper_tab.itemconfig(
                    self.big_lable, text=self.notes[self.stage_game][0]
                )
                self.wallpaper_tab.itemconfig(
                    self.hint_label, text=self.notes[self.stage_game][1]
                )

        # STAGE_1 - CHECK IF GUESS IS A NUMBER
        elif stage_game == 1:
            # VALIDITY CHECK
            if not guess.isdigit() or 0 >= int(guess) or int(guess) > self.edge:
                self.wallpaper_tab.itemconfig(
                    self.hint_label,
                    text=f"Я загадал ЧИСЛО от 1 до {self.edge}.\n      Пробуйте угадать =)",
                )
            # CHECK GUESS == NUMBER?
            else:
                guess = int(guess)
                self.count_try += 1
                if guess != self.number:
                    self.wallpaper_tab.itemconfig(
                        self.big_lable,
                        text=f"Вы ввели {guess}, {self.notes[1][3] if guess < self.number else self.notes[1][2]}",
                    )
                    self.wallpaper_tab.coords(self.big_lable, (355, 240))
                else:
                    self.wallpaper_tab.itemconfig(
                        self.big_lable,
                        text=f"        УРА!=) Победа!!!\nВаше количество попыток: {self.count_try}!",
                    )
                    self.btn_play_again.config(text="Сыграть ещё=)")
                    self.wallpaper_tab.coords(self.btn, (355, 310))
                    self.wallpaper_tab.delete(self.ef_window)
                    self.wallpaper_tab.delete(self.hint_label)

    """RESTART_GAME BUTTON LOGIC"""

    def play_again(self):

        self.N = self.number = self.edge = None
        self.stage_game = self.count_try = 0

        self.wallpaper_tab.delete("del_tag")

        self.guess_number_game()
