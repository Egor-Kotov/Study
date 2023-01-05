import string as chars
from random import choice
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from functions_and_style import tabs_color_list
from reference import ReferenceButton

# TEXTS FOR TAB
texts = (
    " Эта программа, поможет тебе, сгенерировать безопасные пароли",
    "Выбор языка для создания паролей ",
    "   Кол-во паролей =",
    "   Длинна пароля =",
    "Содержит прописные буквы",
    "Содержит строчные буквы",
    "Содержит символы (@,%,& и тд)",
    "Содержит цифры",
    "Исключить неоднозначные символы (il1Lo0O)",
    "Сгенерировать",
    "Очистить",
)
option_menu_lists = (
    ("English", "Русский"),
    tuple(range(1, 21)),
    (1, 10, 20, 30, 40, 50),
)


# REPEATING WIDGETS
class SignatureDropWidget:
    def __init__(self, root, txt, bg="#a5e9a5"):
        self.lbl_font = ("Modern", 11, "italic")

        self.signature = tk.Label(
            root, text=txt, bg=bg, fg="#253529", font=self.lbl_font
        )


class DropWidget:
    def __init__(self, root, txt, width=8, start_elm=0, bg="#32cd32"):
        self.click = tk.StringVar()
        self.click.set(txt[start_elm])

        self.drop_widget = tk.OptionMenu(root, self.click, *txt)
        self.drop_widget.config(
            highlightthickness=0,
            bg=bg,
            font=("", 10, "bold"),
            activebackground="#28a428",
            fg="#253529",
            width=width,
        )
        self.drop_widget["menu"].config(
            bg="#32cd32",
            bd=0,
            borderwidth=0,
            activebackground="#28a428",
            fg="#253529",
            font=("", 10, "italic"),
        )

    def get_clicked(self):
        return int(self.click.get()) if self.click.get().isdigit() else self.click.get()


class CheckBox:
    def __init__(self, root, txt):
        self.var = tk.IntVar()

        self.check_box = tk.Checkbutton(
            root,
            text=txt,
            font=("Modern", 11, "italic"),
            height=1,
            width=50,
            selectcolor="#32cd32",
            activebackground="#28a428",
            bg="#a5e9a5",
            variable=self.var,
            fg="#253529",
            anchor="w",
        )
        self.check_box.select()
        self.check_box.pack(anchor="w")

    def get_var(self):
        return self.var.get()


# TAB STRUCTURE
class PasswordGenerationTab:
    def __init__(self, tabs_bar):

        # CREATE TAB ADD TO TABS_BAR
        self.tab_color = tabs_color_list[3]
        self.password_generation_tab = tk.Frame(tabs_bar, background=self.tab_color)
        tabs_bar.add(self.password_generation_tab, text="Генератор паролей")

        # CREATE REFERENCE BUTTON
        self.reference_btn = ReferenceButton(
            self.password_generation_tab,
            color=self.tab_color,
            img="imgs\\password_generation_question_btn.png",
        )

        """CREATING AND ALIGNMENT FRAMES (HEAD, LEFT, RIGHT)"""
        # HEAD
        self.head_frame = tk.Frame(self.password_generation_tab, bg=self.tab_color)
        self.head_frame.grid(row=0, column=0, columnspan=5)
        self.head_frame.grid_columnconfigure(0, minsize=280)
        self.head_frame.grid_rowconfigure(2, minsize=15)
        # LEFT
        self.left_frame = tk.Frame(
            self.password_generation_tab, bg="#a5e9a5", relief="ridge", borderwidth=6
        )
        self.left_frame.grid(row=1, column=0)
        self.left_frame.grid_rowconfigure(0, minsize=71)
        self.left_frame.grid_rowconfigure(1, minsize=65)
        self.left_frame.grid_columnconfigure(2, minsize=35)
        # RIGHT
        self.right_frame = tk.Frame(
            self.password_generation_tab,
            bg="#a5e9a5",
            relief="ridge",
            borderwidth=6,
            width=50,
        )
        self.right_frame.grid(row=1, column=1, sticky="s")
        # ALIGNMENT
        self.password_generation_tab.grid_columnconfigure(0, minsize=300)
        # self.password_generation.grid_columnconfigure(1, minsize=400)

        # HEAD FRAME FILLING - TITTLE LBL, CHOOSE LANGUAGE DROP WIDGET (CREATING AND ALIGNMENT)
        # TITTLE
        self.tittle_lbl = tk.Label(
            self.head_frame,
            text=texts[0],
            bg=self.tab_color,
            font=("Modern", 14, "bold"),
            anchor="center",
            height=2,
            fg="#253529",
        )
        self.tittle_lbl.grid(row=0, column=0, columnspan=2)
        #  CHOOSE LANGUAGE DROP WIDGET
        self.choose_lng_lbl = SignatureDropWidget(
            root=self.head_frame, txt=texts[1], bg=self.tab_color
        )
        self.choose_lng_lbl.signature.grid(row=1, column=0, sticky="e")

        self.choose_lng_drop = DropWidget(
            root=self.head_frame, txt=option_menu_lists[0]
        )
        self.choose_lng_drop.drop_widget.grid(row=1, column=1, sticky="w")

        # LEFT FRAME FILLING - NUMBER OF PASSWORDS DROP WIDGET, PASSWORD LENGTH DROP WIDGET (CREATING AND ALIGNMENT)
        # NUMBER OF PASSWORDS DROP WIDGET
        self.count_password_lbl = SignatureDropWidget(self.left_frame, texts[2])
        self.count_password_lbl.signature.grid(row=0, column=0)

        self.count_password_drop = DropWidget(
            root=self.left_frame, txt=option_menu_lists[2], width=2, start_elm=1
        )
        self.count_password_drop.drop_widget.grid(row=0, column=1)
        # PASSWORD LENGTH DROP WIDGET
        self.count_symbols_lbl = SignatureDropWidget(self.left_frame, texts[3])
        self.count_symbols_lbl.signature.grid(row=1, column=0)

        self.count_symbols_drop = DropWidget(
            root=self.left_frame, txt=option_menu_lists[1], width=2, start_elm=9
        )
        self.count_symbols_drop.drop_widget.grid(row=1, column=1)

        # RIGHT FRAME - CHECKBOXES (CREATING AND ALIGNMENT)
        self.check_A = CheckBox(self.right_frame, texts[4])
        self.check_a = CheckBox(self.right_frame, texts[5])
        self.check__ = CheckBox(self.right_frame, texts[6])
        self.check_7 = CheckBox(self.right_frame, texts[7])
        self.check_l = CheckBox(self.right_frame, texts[8])

        # CREATE AND DELETE BUTTON (CREATING AND ALIGNMENT)
        self.create_btn = tk.Button(
            self.password_generation_tab,
            text=texts[9],
            width=22,
            height=1,
            bg="#32cd32",
            font=("Modern", 12, "bold"),
            fg="#253529",
            activebackground="#28a428",
            borderwidth=2,
            command=self.generate_passwords,
        )

        self.delete_btn = tk.Button(
            self.password_generation_tab,
            text=texts[10],
            width=13,
            height=1,
            bg="#32cd32",
            font=("Modern", 12, "bold"),
            fg="#253529",
            activebackground="#28a428",
            borderwidth=2,
            command=lambda x="clear": self.generate_passwords(x),
        )
        self.create_btn.grid(row=2, column=1, sticky="s")
        self.delete_btn.grid(row=2, column=0, sticky="s")
        self.password_generation_tab.grid_rowconfigure(2, minsize=60)

        # SCROLL-TEXT WIDGET FOR DISPLAY PASSWORDS (CREATING AND ALIGNMENT)
        self.text_lbl = ScrolledText(
            self.password_generation_tab,
            width=57,
            height=10,
            bg="#a5e9a5",
            font=("", 14),
            relief="ridge",
            borderwidth=6,
            # KEEP IN THE DISABLED STATE, SO USER CANT TYPE
            state="disabled",
        )
        self.text_lbl.grid(row=3, column=0, columnspan=2)
        self.password_generation_tab.grid_rowconfigure(3, minsize=280)

    """FUNCTION FOR CREATING PASSWORDS, OR CLEAR SCROLL-TEXT WIDGET (IF PARAMETER == 'CLEAR')"""

    def generate_passwords(self, clear=None):
        if clear == "clear":
            # CLEAR SCROLL-TEXT WIDGET
            self.text_lbl.config(state="normal")
            self.text_lbl.delete(1.0, tk.END)
            self.text_lbl.config(state="disabled")
        # CREATING PASSWORDS
        else:
            # CREATING PULL OF CHARS FOR PASSWORD
            eng_low = chars.ascii_lowercase
            eng_up = chars.ascii_uppercase
            rus_low = "".join(chr(i) for i in range(ord("а"), ord("а") + 32))
            rus_up = "".join(chr(i) for i in range(ord("А"), ord("А") + 32))

            if self.choose_lng_drop.get_clicked() == "English":
                lang_low, lang_up = eng_low, eng_up
            else:
                lang_low, lang_up = rus_low, rus_up

            chars_string = ""
            quantity = self.count_password_drop.get_clicked()
            length = self.count_symbols_drop.get_clicked()

            if self.check_7.get_var():
                chars_string += chars.digits

            if self.check_A.get_var():
                chars_string += lang_up

            if self.check_a.get_var():
                chars_string += lang_low

            if self.check__.get_var():
                chars_string += chars.punctuation

            if self.check_l.get_var():
                chars_string = "".join(c for c in chars_string if c not in "il1Lo0OоО")

            # CREATING PASSWORDS
            def wrapper():
                for _ in range(quantity):
                    password = ""
                    for ch in range(length):
                        password = "%s%s" % (password, choice(chars_string))
                    self.text_lbl.config(state="normal")
                    self.text_lbl.insert(1.0, "\n" + password + "\n")

            # NOT CREATING IF CHARS PULL EMPTY
            if chars_string:
                wrapper()
                # AFTER, MOVE SCROLLBAR AND CURSOR TO THE BEGINNING
                self.text_lbl.mark_set("insert", "1.0")
                self.text_lbl.see("insert")
                self.text_lbl.config(state="disabled")
