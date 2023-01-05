import string as st
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from webbrowser import open_new
from functions_and_style import tabs_color_list
from reference import ReferenceButton

# TEXTS FOR TAB
texts = (
    "Что такое Шифр Цезаря?",
    "Cдвиг ",
    "Запуск",
    "ВВЕДИТЕ ТЕКСТ",
    "ЗДЕСЬ БУДЕТ МАГИЯ...",
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя",
    "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "Возможно, Вы ошиблись с выбором языка?\n",
    "...\nТекст был сокращен ввиду большого размера. Попробуйте разбить его на части.",
)
option_menu_lists = (
    ("English", "Русский", "Русский без ё"),
    ("Все варианты", "Шифровать", "Дешифровать",),
    tuple(range(1, 26)),
    tuple(range(1, 33)),
    tuple(range(1, 32)),
)


# REPEATING WIDGETS
class DropWidget:
    def __init__(
        self,
        root,
        canvas,
        txt,
        x,
        y=272,
        width=11,
        start_elm=0,
        state="normal",
        bg="#ffe3af",
        command=None,
    ):
        self.click = tk.StringVar()
        self.click.set(txt[start_elm])

        self.drop_widget = tk.OptionMenu(root, self.click, *txt, command=command)
        self.drop_widget.config(
            highlightthickness=0,
            font=("Calibri", 16, "italic"),
            bg=bg,
            activebackground="#ffc559",
            width=width,
            state=state,
        )
        self.drop_widget["menu"].config(
            font=("Calibri", 16),
            bg="#ffe3af",
            activebackground="#ffc559",
            activeforeground="black",
        )

        canvas.create_window(x, y, window=self.drop_widget)

    def get_clicked(self):
        return int(self.click.get()) if self.click.get().isdigit() else self.click.get()


class CCScrolledText:
    def __init__(
        self,
        root,
        canvas,
        placeholder,
        y,
        state="normal",
        font=("Calibri", 16),
        fg="grey",
        bg="#ffe3af",
        width=58,
        height=8,
        x=355,
    ):
        self.text_widget = ScrolledText(
            root, font=font, fg=fg, width=width, height=height, bg=bg, wrap="word"
        )
        self.text_widget.insert(1.0, placeholder)
        self.text_widget.bind("<Button-1>", self.delete_placeholder)
        self.text_widget.config(state=state)

        canvas.create_window(x, y, window=self.text_widget)

    def delete_placeholder(self, event):
        if self.text_widget.get(1.0, 1.13) == texts[3]:
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.config(fg="black")

    def widget_input(self):
        return self.text_widget.get(1.0, 100.0)


# TAB STRUCTURE
class CaesarCipherTab:
    def __init__(self, tabs_bar):

        # CREATE TAB ADD TO TABS_BAR
        self.tab_color = tabs_color_list[3]
        self.caesar_cipher = tk.Frame(tabs_bar, background="white")
        tabs_bar.add(self.caesar_cipher, text="Шифр Цезаря")

        # INSTALL WALLPAPER ON TAB - MAKE CANVAS
        self.img_wallpaper = tk.PhotoImage(file="imgs\\caesar_cipher_canvas.png")
        self.wallpaper_tab = tk.Canvas(
            self.caesar_cipher, width=720, height=600, bd=0, highlightthickness=0
        )
        self.wallpaper_tab.pack(fill="both", expand=1)
        self.wallpaper_tab.create_image(0, 0, image=self.img_wallpaper, anchor="nw")

        # CREATE REFERENCE BUTTON
        self.btn_quest = ReferenceButton(
            self.caesar_cipher, canvas=self.wallpaper_tab, color="#ffc559"
        )

        # CREATE LINK TO CAESAR-CIPHER-INFO (CREATE LINK, BIND OPEN IT, BIND CHANGE CURSOR ON IT)
        self.hyperlink = self.wallpaper_tab.create_text(
            104,
            553,
            text=texts[0],
            fill="white",
            font=("", 12, "bold", "underline"),
            activefill="#ffc559",
        )
        self.wallpaper_tab.tag_bind(
            self.hyperlink,
            "<1>",
            lambda e: open_new(
                "https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F"
            ),
        )
        self.wallpaper_tab.bind("<Motion>", self.check_hand)

        # CREATE SCROLL-WIDGET
        self.input_widget = CCScrolledText(
            root=self.caesar_cipher,
            canvas=self.wallpaper_tab,
            y=125,
            placeholder=texts[3],
        )

        # CREATE DROP-WIDGETS (LANGUAGE, ENCRYPTION/DECRYPTION, SHIFT)
        self.language = DropWidget(
            root=self.caesar_cipher,
            canvas=self.wallpaper_tab,
            txt=option_menu_lists[0],
            x=118,
            start_elm=0,
            command=self.update_shift,
        )

        self.encrypt_decrypt = DropWidget(
            root=self.caesar_cipher,
            canvas=self.wallpaper_tab,
            txt=option_menu_lists[1],
            x=322,
            width=13,
            start_elm=0,
            command=self.open_shift,
        )

        self.signature_sift = self.wallpaper_tab.create_text(
            465, 272, font=("Calibri", 16, "italic"), text=texts[1], fill="grey"
        )
        self.shift = DropWidget(
            root=self.caesar_cipher,
            canvas=self.wallpaper_tab,
            txt=option_menu_lists[2],
            x=525,
            width=2,
            start_elm=0,
            state="disabled",
            bg="#d7d7d7",
        )

        # CREATE BTN-START
        self.start_btn = tk.Button(
            borderwidth=3,
            font=("Calibri", 18, "italic", "bold"),
            bg="#ffe3af",
            activebackground="#ffc559",
            text=texts[2],
            command=self.ave_caesar,
        )
        self.wallpaper_tab.create_window(625, 272, window=self.start_btn)

        # CREATE SCROLL-WIDGET
        self.output_widget = CCScrolledText(
            root=self.caesar_cipher,
            canvas=self.wallpaper_tab,
            y=415,
            placeholder=texts[4],
            state="disabled",
        )

    """FUNCTION TO CHANGE CURSOR ON LINK AND REFERENCE_BTN"""

    def check_hand(self, e):  # runs on mouse motion
        bbox_link = self.wallpaper_tab.bbox(self.hyperlink)
        bbox_ref_btn = self.wallpaper_tab.bbox(self.btn_quest.btn)
        if (
            bbox_link[0] < e.x
            and bbox_link[2] > e.x
            and bbox_link[1] < e.y
            and bbox_link[3] > e.y
        ) or (
            bbox_ref_btn[0] < e.x
            and bbox_ref_btn[2] > e.x
            and bbox_ref_btn[1] < e.y
            and bbox_ref_btn[3] > e.y
        ):  # checks whether the mouse is inside the boundary
            self.wallpaper_tab.config(cursor="hand2")
        else:
            self.wallpaper_tab.config(cursor="")

    """FUNCTION TO OPEN(UNLOCKED/LOCKED) SHIFT_DROP-WIDGET"""

    def open_shift(self, event):
        # UNLOCKED
        if self.encrypt_decrypt.get_clicked() != "Все варианты":
            self.shift.drop_widget.config(state="normal", bg="#ffe3af")
            self.wallpaper_tab.itemconfig(self.signature_sift, fill="black")
        # LOCKED
        else:
            self.shift.click.set("1")
            self.wallpaper_tab.itemconfig(self.signature_sift, fill="grey")
            self.shift.drop_widget.config(state="disabled", bg="#d7d7d7")

    """FUNCTION TO CHANGE SHIFT_DROP-WIDGET WHEN CHANGE LANGUAGE"""

    def update_shift(self, event):
        menu = self.shift.drop_widget["menu"]
        menu.delete(0, tk.END)
        if self.language.get_clicked() == option_menu_lists[0][1]:
            for string in option_menu_lists[3]:
                menu.add_command(
                    label=string,
                    command=lambda value=string: self.shift.click.set(value),
                )
        elif self.language.get_clicked() == option_menu_lists[0][2]:
            for string in option_menu_lists[4]:
                menu.add_command(
                    label=string,
                    command=lambda value=string: self.shift.click.set(value),
                )
        else:
            for string in option_menu_lists[2]:
                menu.add_command(
                    label=string,
                    command=lambda value=string: self.shift.click.set(value),
                )
        self.shift.click.set("1")

    """FUNCTION WITH PROGRAM LOGIC"""

    def ave_caesar(self):
        # IF INPUT EMPTY, PLACEHOLDER THEN RETURN
        if (
            self.input_widget.widget_input().strip() == texts[3]
            or self.input_widget.widget_input().strip() == ""
        ):
            self.output_widget.text_widget.config(state="normal", foreground="grey")
            self.output_widget.text_widget.delete(1.0, tk.END)
            self.output_widget.text_widget.insert(
                1.0, texts[3] + " В ВЕРХНЕЕ ПОЛЕ ВВОДА"
            )
            self.output_widget.text_widget.config(state="disabled")
            return
        # ELSE
        # CHANGE STATE OF OUTPUT WIDGET (FOR PRINT OUTPUT)
        self.output_widget.text_widget.config(state="normal", foreground="black")
        self.output_widget.text_widget.delete(1.0, tk.END)
        # INPUT-TEXT PROCESSING
        if len(self.input_widget.widget_input().strip()) > 7801:
            text = self.input_widget.widget_input().strip()[:7801] + texts[10]
        else:
            text = self.input_widget.widget_input().strip()
        # CREATE VARIABLES FOR DECRYPTION/ENCRYPTION
        eng_l = st.ascii_lowercase * 2
        eng_u = st.ascii_uppercase * 2
        rus_your_l = texts[5]
        rus_your_u = texts[6]
        rus_l = texts[7]
        rus_u = texts[8]

        if self.language.get_clicked() == option_menu_lists[0][0]:
            lang_l, lang_u, top = eng_l, eng_u, 25
        elif self.language.get_clicked() == option_menu_lists[0][1]:
            lang_l, lang_u, top = rus_your_l, rus_your_u, 32
        else:
            lang_l, lang_u, top = rus_l, rus_u, 31

        """FUNCTION FOR DECRYPTION/ENCRYPTION"""

        def wrapper(shift):

            result = ""

            for char in text:
                if char.isalpha() and char.isupper() and char in lang_u:
                    i = lang_u.find(char) + shift
                    result = "%s%s" % (result, lang_u[i])

                elif char.isalpha() and char in lang_l:
                    i = lang_l.find(char) + shift
                    result = "%s%s" % (result, lang_l[i])

                else:
                    result = "%s%s" % (result, char)

            return result

        # IF ALL SHIFT VARIANTS
        if self.encrypt_decrypt.get_clicked() == option_menu_lists[1][0]:
            for i in range(top, -1, -1):
                self.output_widget.text_widget.insert(
                    1.0,
                    "\n"
                    + f"Сдвиг {i} при шифровании или сдвиг {top+1-i} при дешифровке:\n"
                    + wrapper(i)
                    + "\n",
                )
        # IF DECRYPTION
        elif self.encrypt_decrypt.get_clicked() == option_menu_lists[1][2]:
            shift = -self.shift.get_clicked()
            self.output_widget.text_widget.insert(
                1.0, "\n" + f"Сдвиг {shift}\n" + wrapper(shift) + "\n"
            )
        # IF ENCRYPTION
        else:
            self.output_widget.text_widget.insert(
                1.0,
                "\n"
                + f"Сдвиг {self.shift.get_clicked()}\n"
                + wrapper(self.shift.get_clicked())
                + "\n",
            )
        # IF INPUT TEXT NOT CHANGE AFTER ENCRYPTION/DECRYPTION, CHECK LANGUAGE
        if self.input_widget.widget_input().strip() == wrapper(5).strip():
            self.output_widget.text_widget.insert(1.0, texts[9].upper())
        # LOCKED OUTPUT
        self.output_widget.text_widget.config(state="disabled")
