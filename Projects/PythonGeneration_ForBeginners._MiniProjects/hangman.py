import random
import tkinter as tk
from PIL import Image, ImageTk
from functions_and_style import tabs_color_list
from reference import ReferenceButton
from hangman_files import hangman_words, hangman_imgs

# TEXTS FOR TAB
texts = (
    'Игра "Виселица"',
    "Выберите уровень сложности:",
    "Низкий\n(11 попыток)",
    "Средний\n(8 попыток)",
    "Высокий\n(6 попыток)",
    "Выберите количество\nизвестных букв:",
    "Ноль",
    "Одна",
    "Две",
    "Введите букву и нажмите Enter.",
    "Введите, пожалуйста, ОДНУ РУССКУЮ букву\nИ нажмите Enter =)",
    "Увы, мимо =( Такой скрытой буквы нет в слове.\nПродолжай... Если хочешь жить =)",
    "Попал! Вперед к свободе!\nЖми Enter=)",
    "Хочешь сыграть еще раз???\nНажми кнопку 'Назад' - коричневую стрелку слева.\nЭта кнопка перезапустит партию сначала,\nв любой момент игры!",
)


# TAB STRUCTURE:
class HangmanTab:
    def __init__(self, tabs_bar):
        # TAB COLOR
        self.tab_color = tabs_color_list[1]

        # CREATE TAB ADD TO TABS_BAR
        self.hangman_tab = tk.Frame(tabs_bar, background=self.tab_color)
        tabs_bar.add(self.hangman_tab, text="Виселица")

        # CREATE REFERENCE BUTTON
        self.reference_btn = ReferenceButton(
            self.hangman_tab,
            color=self.tab_color,
            img="imgs\\hangman_question_btn.png",
        )

        # CREATE AND ADD REPLAY BUTTON
        self.img_replay_btn = Image.open("imgs\\hangman_replay_btn.png")
        self.img_replay_btn = ImageTk.PhotoImage(self.img_replay_btn)

        self.replay_btn = tk.Button(
            self.hangman_tab,
            image=self.img_replay_btn,
            command=self.destroy_widgets,
            highlightthickness=0,
            border=0,
            bg=self.tab_color,
            activebackground=self.tab_color,
            cursor="hand2",
        )
        self.replay_btn.place(x=0, y=510)

        # LAUNCHING CHOOSING START CONDITION FUNCTION (STARTING ALL HANGMAN GAME STAGES)
        self.choose_starting_conditions()

    """
    FUNCTION FOR CHOOSING START CONDITION OF HANGMAN GAME (AND THEN LAUNCHING THE START GAME FUNCTION)
    """

    def choose_starting_conditions(self, stage="start"):

        # 1 STAGE - CHOOSE NUMBER OF TRYING BLOCK (CREATE TITLE LBL, SIGNATURE FOR BUTTON FRAME, BUTTONS IN FRAME)
        # NUMBER OF TRYING IS SAVED IN NEXT STAGE
        if stage == "start":
            # REQUIRED VARIABLES FOR GAME
            self.btn_stack = {}
            self.open_letters_idx = []
            self.attempt = 1

            # CREATE TITLE - NAME OF GAME
            self.title = tk.Label(
                self.hangman_tab,
                text=texts[0],
                font=("Fixedsys", 40, "bold"),
                bg=self.tab_color,
                fg="#996548",
            )
            self.title.pack(pady=75)

            # CREATE SIGNATURE FOR BUTTONS
            self.starting_conditions = tk.Label(
                self.hangman_tab,
                text=texts[1],
                font=("Fixedsys", 25, "bold"),
                bg=self.tab_color,
                fg="#996548",
            )
            self.starting_conditions.pack(pady=30)

            # CREATE BUTTON FRAME AND ADD BUTTONS IN IT (FOR LOOP ADD BUTTONS TO DICTIONARY(btn_stack))
            self.btn_frame = tk.Frame(self.hangman_tab, bg=self.tab_color)
            self.btn_frame.pack(pady=35)

            for i, v in enumerate((12, 9, 7,)):
                self.btn_stack[i] = tk.Button(
                    self.btn_frame,
                    text=texts[2 + i],
                    command=lambda x=v: self.choose_starting_conditions(x),
                    font=("Fixedsys", 14, "bold"),
                    bg=self.tab_color,
                    fg="white",
                    relief="raised",
                    borderwidth=6,
                    cursor="hand2",
                    activebackground="#62412e",
                    background="#996548",
                )
                self.btn_stack[i].grid(row=0, column=i * 2, columnspan=2, padx=30)

        # STAGE 2 - CHOOSE NUMBER OF OPEN LETTERS IN WORD BLOCK (CREATE SIGNATURE FOR BUTTONS FRAME AND BUTTONS)
        # NUMBER OF OPEN LETTERS IS SAVED IN NEXT STAGE
        elif stage in (12, 9, 7):

            # SAVE NUBER OF TRYING
            self.difficulty_level = stage

            # CONFIG SIGNATURE FOR BUTTONS
            self.starting_conditions.config(
                text=texts[5], font=("Fixedsys", 25, "bold")
            )
            self.starting_conditions.pack(pady=20)

            # CONFIG BUTTONS TEXTS AND FUNCTIONS
            for k, v in self.btn_stack.items():
                v.config(
                    text=texts[6 + k],
                    command=lambda x=k: self.choose_starting_conditions(x),
                )

        # STAGE 3 - SAVED NUM OPEN LETTERS IN WORD, DESTROY UNNECESSARY WIDGETS, LAUNCHING THE START GAME FUNCTION
        elif stage in (0, 1, 2):
            # SAVED NUMBER OPEN LETTERS IN WORD
            self.number_open_letters = stage
            # DESTROY WIDGETS
            self.destroy_widgets(stage=0)
            # LAUNCHING THE START GAME FUNCTION
            self.game_start()

    """
    GAME START FUNCTIONS -
    - DRAWING SCREEN OF GAME (IMG OF GAME, REBUS LBL(ENCODED HIDDEN WORD), INPUT-ENTRY, HINT IN GAME)
    """

    def game_start(self):
        # DRAWING GAME IMG
        self.drawing_game_img(stage="start")

        # CHOOSE WORD FOR THIS GAME (self.hidden_word)
        self.choose_word()

        # GENERATE LIST IDXS OF OPEN LETTERS IN HIDDEN WORD
        self.generate_open_l_i()

        # CREATE REBUS FRAME (FRAME FOR ENCODED HIDDEN WORD) AND LAUNCHING REBUS FUNCTION
        self.rebus_frame = tk.Frame(self.hangman_tab, bg="#7F7F7F")
        self.rebus_frame.pack(fill="both")

        self.rebus()

        # CREATE INPUT ENTRY, BIND IT FRO ENTER KEY
        self.input = tk.Entry(
            self.hangman_tab,
            relief="ridge",
            borderwidth=10,
            width=3,
            font=("Fixedsys", 22, "bold"),
            bg="#7F7F7F",
        )
        self.input.pack(pady=25)

        self.input.bind("<Return>", self.entry_field_return)

        # CREATE HINT LABEL FOR GAME
        self.hint = tk.Label(
            self.hangman_tab,
            text=texts[9],
            fg="#996548",
            font=("Fixedsys", 13, "bold"),
            bg=self.tab_color,
        )
        self.hint.pack()

        # FOCUS INPUT ENTRY WIDGET
        self.input.focus()

    """
    GAME LOGIC FUNCTION (PROCESSING INPUT TEXT - self.guess, GET IN INPUT ENTRY FUNCTION)
    """

    def game_logic(self):

        # IF INPUT != RUSSIAN ONE LETTER - CONFIG HINT TEXT
        if self.guess.lower() not in "абвгдежзийклмнопрстуфхцчшщъыьэюя" or (
            len(self.guess) == 0 or len(self.guess) > 1
        ):
            self.hint.config(text=texts[10])

        # IF INPUT == RUSSIAN LETTER AND PLAYER HAVE ATTEMPTS FOR GAME
        elif (
            self.attempt < self.difficulty_level
            and self.hidden_word != self.rebus_word_txt
        ):
            # CHECK IF THE PLAYER GUESSED THE LETTER?:

            # YES: CONFIG REBUS LBL AND CONFIG HINT (LIST IDXS OPEN LETTERS CHANGE)
            if self.generate_open_l_i(self.attempt):
                self.rebus(stage=1)
                self.hint.config(text=texts[12])

            # NO: CONFIG GAME IMG
            else:
                self.drawing_game_img(stage="mistake")
                self.attempt += 1
                self.hint.config(text=texts[11])

        # IF PLAYER WIN = GUESSED THE WORD (CHANGE GAME IMG AND HINT, DESTROY INPUT ENTRY)
        if self.hidden_word == self.rebus_word_txt:
            self.drawing_game_img("win")

            self.input.destroy()

            self.hint.config(text=texts[13], pady=45)

        # IF PLAYER HAS SPENT ALL ATTEMPTS = LOSE GAME (CHANGE GAME IMG, OPEN HIDDEN WORD, DESTROY INPUT, CONFIG HINT)
        elif self.attempt == self.difficulty_level:
            self.drawing_game_img(stage="game_over")

            self.rebus(stage=2)

            self.input.destroy()

            self.hint.config(text=texts[13], pady=45)

    """FUNCTION TO CHOOSE RANDOM HIDDEN WORD (FROM hangman_files.hangman_words)"""

    def choose_word(self):
        self.hidden_word = hangman_words[random.randint(0, len(hangman_words) - 1)]
        # IF LEN CHOOSING WORD IS LESS NUBER OPEN LETTERS, LAUNCHING FUNCTION AGAIN
        if len(self.hidden_word) <= self.number_open_letters:
            return self.choose_word()

    """FUNCTION TO GENERATE INDEXES LIST OF OPEN LETTERS (STAGE 0 - IN START GAME, STAGE 1 = AFTER EVERY VALID INPUT)"""

    def generate_open_l_i(self, stage=0):

        # STAGE 0 - GENERATE INDEXES FOR OPEN LETTERS IN START GAME (START CONDITION)
        if stage == 0:
            while len(self.open_letters_idx) < self.number_open_letters:
                i = random.randint(0, len(self.hidden_word) - 1)
                if i not in self.open_letters_idx:
                    self.open_letters_idx.append(i)

        # STAGE 1 - GENERATE INDEXES FOR OPEN LETTERS IN WORD, AFTER PLAYER VALID INPUT
        else:
            # CREATE FLAG TO CHECK CHANGES OF LIST OPEN LETTERS INDEXES
            self.change = False
            # GO FOR ALL ELEMENTS OF HIDDEN WORD AND IF (INPUT == ELEMENT AND ELEMENT IDX NOT IN LIST)
            # ADD IDX OF ELEMENT IN LIST
            for i, ch in enumerate(self.hidden_word):
                if i not in self.open_letters_idx and self.guess == ch:
                    self.open_letters_idx.append(i)
                    # CHANGE FLAG (LIST HAVE NEW ELEMENTS)
                    self.change = True
            # AFTER ALL ITERATION IF LIST CHANGE RETURN TRUE
            if self.change:
                return True

    """
    FUNCTION TO CREATE REBUS-WORD-FRAME (ENCODED HIDDEN WORD) AND REBUS_WORD_TXT TO COMPARING WITH HIDDEN WORD,
    EVERY TIME NEW (IF LIST IDXS CHANGE)
    """

    def rebus(self, stage=0):

        # IF REBUS FRAME EXISTS DESTROY IT
        if stage:
            self.rebus_wordFrames.destroy()

        # CREATE REBUS FRAME AND REBUS_WORD_TXT TO COMPARING WITH HIDDEN WORD
        self.rebus_word_txt = ""
        self.rebus_wordFrames = tk.Frame(self.rebus_frame, bg="#7F7F7F")
        for i, ch in enumerate(self.hidden_word):

            # STAGE 2 - LOOSE, CREATE OPEN WORD IN REBUS FRAME
            if stage == 2:
                tk.Label(
                    self.rebus_wordFrames,
                    text=ch.upper(),
                    relief="ridge",
                    borderwidth=4,
                    font=("Fixedsys", 20, "bold"),
                ).pack(side="left", padx=7)

            # STAGE 0 - NORMAL GAME
            # IF IDX OF ELEMENT NOT IN IDXS LIST, ADD '_' INSTEAD OF ELEMENT
            elif i not in self.open_letters_idx:
                self.rebus_word_txt = "%s%s" % (self.rebus_word_txt, "_")
                tk.Label(
                    self.rebus_wordFrames,
                    text="_",
                    relief="ridge",
                    borderwidth=4,
                    font=("Fixedsys", 20, "bold"),
                ).pack(side="left", padx=7)
            # IF IDX OF ELEMENT IN IDXS LIST, ADD ELEMENT
            else:
                self.rebus_word_txt = "%s%s" % (self.rebus_word_txt, ch)
                tk.Label(
                    self.rebus_wordFrames,
                    text=ch.upper(),
                    relief="ridge",
                    borderwidth=4,
                    font=("Fixedsys", 20, "bold"),
                ).pack(side="left", padx=7)

        self.rebus_wordFrames.pack()

        print(
            self.hidden_word,
            self.rebus_word_txt,
            self.hidden_word == self.rebus_word_txt,
        )

    """FUNCTION GET INPUT, AND LAUNCHING GAME LOGIC FUNCTION"""

    def entry_field_return(self, *args):
        # TAKE VALUE IN ENTRY FIELD, SAVE IT
        self.guess = self.input.get().lower()
        self.input.delete(0, tk.END)
        # START GAME LOGIC WITH THIS INPUT
        self.game_logic()

    """FUNCTION TO DROWN IMGS DURING GAME"""

    def drawing_game_img(self, stage):

        # START GAME - CREATE IMG LBL ADD START IMG ON IT
        if stage == "start":
            if self.difficulty_level in (7, 9):
                start = hangman_imgs[-4]
            else:
                start = hangman_imgs[-5]

            game_img = Image.open(start)
            game_img = ImageTk.PhotoImage(game_img)
            self.game_img_lbl = tk.Label(
                self.hangman_tab,
                image=game_img,
                bg="grey",
                highlightthickness=0,
                borderwidth=0,
            )
            self.game_img_lbl.image = game_img
            self.game_img_lbl.pack()

        # UPDATE IMG WHEN GUESS == MISTAKE
        elif stage == "mistake":
            if self.difficulty_level == 12:
                idx: int = self.attempt
            else:
                idx: int = self.attempt + 3

            game_img = Image.open(hangman_imgs[idx])
            game_img = ImageTk.PhotoImage(game_img)
            self.game_img_lbl.config(image=game_img)
            self.game_img_lbl.image = game_img

        # UPDATE IMG WHEN GAME OVER, ATTEMPTS END
        elif stage == "game_over":
            game_img = Image.open(
                f"{hangman_imgs[-3] if self.difficulty_level in (9, 12) else hangman_imgs[-2]}"
            )
            game_img = ImageTk.PhotoImage(game_img)
            self.game_img_lbl.config(image=game_img)
            self.game_img_lbl.image = game_img

        # UPDATE IMG WHEN WIN
        elif stage == "win":
            game_img = Image.open(hangman_imgs[-1])
            game_img = ImageTk.PhotoImage(game_img)
            self.game_img_lbl.config(image=game_img)
            self.game_img_lbl.image = game_img

    """FUNCTION TO DESTROY WIDGETS"""

    def destroy_widgets(self, stage=1):
        # DESTROY ALL, EXCEPT REFERENCE_BTN AND REPLAY_BTN (USING AFTER GET STAR CONDITION)
        for i, w in enumerate(self.hangman_tab.winfo_children()):
            if i not in (0, 1):
                w.destroy()
        # COMMAND TO REPLAY_BTN, LAUNCHING GAME AGAIN
        if stage:
            self.choose_starting_conditions()
