import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from random import choice
from reference import ReferenceButton
from functions_and_style import tabs_color_list, play_gif

# TEXTS FOR TAB
texts = (
    "Привет Мир, я магический шар, и я знаю ответ на любой вопрос!",
    "Есть ли вопросы которые тебя волнуют???",
    "ДА!",
    "СПРОСИТЬ",
    "СПРОСИТЬ ЕЩЁ",
    "ВВЕДИ ВОПРОС",
    "Я СЛЫШУ ВОПРОС, В ТВОЕМ МОЛЧАНИИ...",
)
answers = (
    "Бесспорно!",
    "Предрешено!",
    "Никаких сомнений!",
    "Определённо да!",
    "Можешь быть уверен в этом!",
    "Мне кажется - да!",
    "Вероятнее всего!",
    "Хорошие перспективы!",
    "Знаки говорят - да!",
    "Да!",
    "Пока неясно, попробуй снова!",
    "Спроси позже!",
    "Лучше не рассказывать!",
    "Сейчас нельзя предсказать!",
    "Сконцентрируйся и спроси опять!",
    "Даже не думай!",
    "Мой ответ - нет!",
    "По моим данным - нет!",
    "Перспективы не очень хорошие!",
    "Весьма сомнительно!",
)


# TAB STRUCTURE
class Ball8Tab:
    def __init__(self, tabs_bar):

        # CREATE TAB ADD TO TABS_BAR
        self.tab_color = tabs_color_list[2]
        self.magic_8_ball_tab = tk.Frame(tabs_bar, background=self.tab_color)
        tabs_bar.add(self.magic_8_ball_tab, text="Магический шар8")

        # CREATE REQUIRED VARIABLE
        self.question = None
        self.stage = 0

        # CREATE REFERENCE BUTTON
        self.reference_btn = ReferenceButton(
            self.magic_8_ball_tab, color=self.tab_color
        )

        # CREATE TITLE (HEAD LABEL)
        self.head_lbl = tk.Label(
            self.magic_8_ball_tab,
            text=texts[0],
            fg="white",
            font=("Impact", 18),
            bg=self.tab_color,
            height=3,
        )
        self.head_lbl.pack(fill="both")

        # CREATE GIF ANIMATION LABEL
        self.gif_lbl = tk.Label(self.magic_8_ball_tab, image="", borderwidth=0)
        self.gif_lbl.pack()
        play_gif(self.magic_8_ball_tab, self.gif_lbl, "imgs\\ball_8.gif")

        # START FUNCTION LOGIC APP
        self.create_or_change_bottom_lbls()

    """LOGIC APP, CREATING AND UPDATE BOTTOM WIDGETS"""

    def create_or_change_bottom_lbls(self):

        # STAGE 0 (CREATE ALL WIDGETS, DISPLAY STAGE 0 WIDGETS)
        if self.stage == 0:
            # CREATE BOTTOM LBL
            self.bottom_lbl = tk.Label(
                self.magic_8_ball_tab,
                text=texts[1],
                fg="white",
                font=("Impact", 15),
                bg=self.tab_color,
                height=3,
            )
            self.bottom_lbl.pack(fill="both")
            # BUTTON
            self.btn = tk.Button(
                self.magic_8_ball_tab,
                text=texts[2],
                command=self.create_or_change_bottom_lbls,
                width=8,
                borderwidth=8,
                bg="#DCDCDC",
                font=("Cambria", 12, "italic"),
                relief="solid",
            )
            self.btn.pack(pady=15)
            # QUESTION LABEL
            self.question_lbl = tk.Label(
                self.magic_8_ball_tab,
                text=self.question,
                fg="#DCDCDC",
                font=("Cambria", 14, "italic"),
                bg="black",
                width=150,
                anchor="s",
                pady=10,
                height=3,
            )
            # SCROLL-TEXT LABEL, BIND EVENT
            self.text_lbl = ScrolledText(
                self.magic_8_ball_tab,
                width=42,
                height=5,
                font=("Cambria", 14),
                fg="grey",
                bg="#DCDCDC",
            )
            self.text_lbl.bind("<Button-1>", self.delete_placeholder)
            # CHANGE STAGE
            self.stage = 1

        # STAGE 1, CONFIGURATE LABELS FOR STAGE 1
        elif self.stage == 1:
            # FORGET NEEDLESS LABELS AND BUTTON (SKIP AHEAD SCROLL-TEXT LABEL)
            self.bottom_lbl.pack_forget()
            self.question_lbl.config(font=("Cambria", 14, "italic"), fg="#DCDCDC")
            self.question_lbl.pack_forget()
            self.btn.pack_forget()
            # DISPLAY WIDGETS FOR STAGE 1
            # SCROLL-TEXT LABEL
            self.text_lbl.pack(pady=15)
            self.text_lbl.configure(foreground="grey")
            self.text_lbl.insert(1.0, texts[5])
            # BUTTON
            self.btn.pack()
            self.btn.configure(text=texts[3], width=10)
            self.head_lbl.focus()
            # CHANGE STAGE
            self.stage = 2

        # STAGE 2, CONFIGURATE LABELS FOR STAGE 2
        else:
            # READ AND SAVE QUESTION TEXT
            if self.text_lbl.get(1.0, 3.0).strip() != texts[5]:
                self.question = self.text_lbl.get(1.0, 3.0)
                self.question = "".join(
                    ch if ch != "\n" and i < 98 else ""
                    for i, ch in enumerate(self.question)
                )
                self.question = (
                    '"'
                    + "".join(
                        ch + "\n" if i % 50 == 0 and i != 0 else ch
                        for i, ch in enumerate(self.question)
                    )
                    + '... ?"'
                )
            else:
                self.question = texts[-1]
            # CLEAR AND HIDE SCROLL-TEXT LABEL
            self.text_lbl.delete(1.0, tk.END)
            self.text_lbl.pack_forget()
            # ADD QUESTION TEXT TO QUESTION LABEL AND DISPLAY IT
            if self.question == texts[-1]:
                self.question_lbl.config(
                    fg="white", text=self.question, font=("Impact", 15)
                )
            else:
                self.question_lbl.config(text=self.question)
            self.question_lbl.pack(before=self.btn)
            # CONFIGURATE BOTTOM LABEL AND DISPLAY IT
            self.bottom_lbl.config(
                text=choice(answers),
                font=("Impact", 18),
                height=1,
                anchor="center",
                pady=10,
            )
            self.bottom_lbl.pack(before=self.btn)
            # CONFIGURATE BUTTON AND DISPLAY IT
            self.btn.config(text=texts[4], width=15)
            self.btn.pack()
            # CHANGE STAGE, CREATING LOOP STAGE 1 <-> STAGE 2
            self.stage = 1

    """FUNCTION PLACEHOLDER"""

    def delete_placeholder(self, event):
        if self.text_lbl.get(1.0, 1.12) == texts[5]:
            self.text_lbl.delete(1.0, tk.END)
            self.text_lbl.config(fg="black")
