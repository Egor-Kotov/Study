import tkinter as tk
from PIL import Image, ImageTk
from functions_and_style import tabs_color_list, get_key_from_value
from reference import ReferenceButton

# TEXTS FOR TAB
texts = (
    "Конвертер систем счисления",
    "Из какой системы счисления\n перевести число?",
    "В какую систему счисления\n перевести число?",
    "Перевести",
    "Очистить",
    (2, 8, 10, 16),
    "Введите число",
)


# REPEATING WIDGETS
class RadioFrame:
    def __init__(
        self,
        root,
        title,
        btn_txt,
        row,
        column,
        color=tabs_color_list[5],
        font=("Bahnschrift SemiLight SemiConde", 15),
        fg="black",
        state="normal",
        btn_func=None,
    ):
        self.frame = tk.Frame(root, bg=color)

        self.title = tk.Label(self.frame, font=font, bg=color, text=title)
        self.title.grid(row=0, column=0, columnspan=4, pady=25)

        self.choice = tk.IntVar(value=2)

        for i, v in enumerate(texts[5]):
            tk.Radiobutton(
                self.frame,
                text=v,
                font=font,
                variable=self.choice,
                value=v,
                bg=color,
                activebackground=color,
                cursor="hand2",
            ).grid(row=1, column=i, pady=25)

        self.input_output = tk.Entry(
            self.frame, font=font, fg=fg, width=24, state=state
        )
        self.input_output.grid(row=2, column=0, columnspan=4, pady=25)

        self.btn = tk.Button(
            self.frame,
            font=font,
            text=btn_txt,
            borderwidth=3,
            bg="#cbcbcb",
            activebackground="#828282",
            command=btn_func,
        )
        self.btn.grid(row=3, column=0, columnspan=4, pady=25)

        self.frame.grid(row=row, column=column)


# TAB STRUCTURE
class NumberConverterTab:
    def __init__(self, tabs_bar):

        # CREATE TAB ADD TO TABS_BAR
        self.tab_color = tabs_color_list[5]
        self.tab_font = ("Bahnschrift SemiLight SemiConde", 20)
        self.number_converter_tab = tk.Frame(tabs_bar, background=self.tab_color)
        tabs_bar.add(self.number_converter_tab, text=texts[0])

        # CREATE REFERENCE BUTTON
        self.reference_btn = ReferenceButton(
            master=self.number_converter_tab,
            color=self.tab_color,
            img="imgs\\number_converter_question_btn.png",
        )

        # CREATE TITLE LBL
        self.title = tk.Label(
            self.number_converter_tab,
            text="\n" + texts[0],
            font=("Bahnschrift SemiLight SemiConde", 20),
            bg=self.tab_color,
        )
        self.title.pack(pady=30)

        # CREATE MAIN FRAME
        self.main_frame = tk.Frame(self.number_converter_tab, bg=self.tab_color,)
        # EDGE FRAME - PLUG (COLUMN = 0)
        self.edge_frame = tk.Frame(self.main_frame, width=53, bg=self.tab_color)
        self.edge_frame.grid(row=0, column=0)
        # LEFT RADIO FRAME (COLUMN = 1), INSTALL AND BIND PLACEHOLDER
        self.radio_left = RadioFrame(
            root=self.main_frame,
            title=texts[1],
            fg="grey",
            btn_txt=texts[3],
            btn_func=self.conversion,
            row=0,
            column=1,
        )

        self.radio_left.input_output.insert(0, texts[6])
        self.radio_left.input_output.bind("<Button-1>", self.delete_placeholder)
        # MIDDLE FRAME - PLUG (COLUMN = 2), ARROW IMG
        self.middle_frame = tk.Frame(
            self.main_frame, width=150, height=4, bg=self.tab_color
        )

        self.ar_img = Image.open("imgs\\number_converter_arrow.png")
        self.ar_img = ImageTk.PhotoImage(self.ar_img)
        self.arrow = tk.Label(self.middle_frame, image=self.ar_img, bg=self.tab_color)
        self.arrow.grid(row=1, column=0, padx=20)

        self.middle_frame.grid(row=0, column=2)
        self.middle_frame.grid_rowconfigure(index=0, minsize=100)
        # RIGHT RADIO FRAME (COLUMN = 3)
        self.radio_right = RadioFrame(
            root=self.main_frame,
            title=texts[2],
            btn_txt=texts[4],
            btn_func=self.delete_btn,
            row=0,
            column=3,
            state="disabled",
        )
        # MAIN FRAME ALIGNMENT
        self.main_frame.pack(fill="both")

        # HINT ERROR INPUT
        self.hint = tk.Label(
            self.number_converter_tab,
            bg=self.tab_color,
            fg="red",
            text="",
            font=("Bahnschrift SemiLight SemiConde", 15),
        )
        self.hint.pack()

    """APP LOGIC FUNCTION"""

    def conversion(self):
        hexadecimal = {
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }

        # INPUT VALIDATION CHECK FUNCTION, IF NOT VALIDATE OR VALIDATE CONFIG HINT LBL
        def is_number():
            self.radio_right.input_output.config(state="normal")
            #  16 SYSTEM
            if self.radio_left.choice.get() == 16:
                for ch in self.radio_left.input_output.get():
                    if ch.upper() not in "0123456789ABCDEF":
                        self.radio_right.input_output.delete(0, tk.END)
                        self.hint.config(
                            text="Шестнадцатиричное число может содержать только цифры 0 - 9, буквы A,B,C,D,E,F"
                        )
                        return False
                self.hint.config(text="")
                return True
            # 2 SYSTEM
            elif self.radio_left.choice.get() == 2:
                for ch in self.radio_left.input_output.get():
                    if ch not in "01":
                        self.radio_right.input_output.delete(0, tk.END)
                        self.hint.config(
                            text="Двоичное число может содержать только цифры 0 и 1"
                        )
                        return False
                self.hint.config(text="")
                return True
            # 8 SYSTEM
            elif self.radio_left.choice.get() == 8:
                for ch in self.radio_left.input_output.get():
                    if ch not in "01234567":
                        self.radio_right.input_output.delete(0, tk.END)
                        self.hint.config(
                            text="Восьмеричное число может содержать только цифры 0 - 7"
                        )
                        return False
                self.hint.config(text="")
                return True
            # 10 SYSTEM
            elif (
                self.radio_left.choice.get() == 10
                and self.radio_left.input_output.get().isdigit()
            ):
                self.hint.config(text="")
                return True
            else:
                self.radio_right.input_output.delete(0, tk.END)
                self.hint.config(
                    text="Десятичное число может содержать только цифры 0 - 9"
                )
                return False

        """FUNCTION CONVERSION NUMBER TO DECIMAL"""

        def conversion_to_decimal(num: str, system: int):
            input_num = num[::-1]
            decimal = 0

            for i, ch in enumerate(input_num):
                if ch.isdigit():
                    decimal += int(ch) * (system ** i)
                else:
                    decimal += (system ** i) * hexadecimal[ch.upper()]

            return decimal

        """FUNCTION CONVERSION DECIMAL NUMBER TO OTHER"""

        def conversion_to_other(num: int, system: int):
            convert_num = ""

            while num > 0:
                if num % system > 9:
                    convert_num = "%s%s" % (
                        convert_num,
                        get_key_from_value(value=num % system, dictionary=hexadecimal),
                    )
                else:
                    convert_num = "%s%s" % (convert_num, num % system)
                num //= system

            return convert_num[::-1]

        """START APP (CONVERT AND INSERT NUMBER IN OUTPUT)"""

        if is_number():

            number = conversion_to_decimal(
                num=self.radio_left.input_output.get(),
                system=self.radio_left.choice.get(),
            )

            number = conversion_to_other(
                num=number, system=self.radio_right.choice.get()
            )

            self.radio_right.input_output.delete(0, tk.END)
            self.radio_right.input_output.insert(0, number)

    """FUNCTION CLEAR OF TEXT ENTRY INPUT AND OUTPUT"""

    def delete_btn(self):
        self.radio_left.input_output.delete(0, tk.END)
        self.radio_right.input_output.delete(0, tk.END)

    """PLACEHOLDER FUNCTION"""

    def delete_placeholder(self, event):
        if self.radio_left.input_output.get() == texts[6]:
            self.radio_left.input_output.delete(0, tk.END)
            self.radio_left.input_output.config(fg="black")
