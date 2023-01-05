from tkinter.ttk import Notebook
from guess_number import GuessNumberTab
from ball_8 import Ball8Tab
from password_generator import PasswordGenerationTab
from caesar_cipher import CaesarCipherTab
from number_converter import NumberConverterTab
from hangman import HangmanTab
from functions_and_style import TabsStyle


class TabsBar:
    def __init__(self, root):

        self.tabs_control = Notebook(root, width=600, height=600)
        self.tabs_control.bind("<<NotebookTabChanged>>", self.tab_change)

        self.style = TabsStyle()

        self.guess = GuessNumberTab(self.tabs_control)
        self.hangman = HangmanTab(self.tabs_control)
        self.ball8 = Ball8Tab(self.tabs_control)
        self.password = PasswordGenerationTab(self.tabs_control)
        self.caesar = CaesarCipherTab(self.tabs_control)
        self.convertor = NumberConverterTab(self.tabs_control)

    def draw_tabs_bar(self):
        self.tabs_control.pack()

    # FUNCTION TO CHANGE TAB STYLE WHEN TAB CHANGE
    def tab_change(self, event):
        self.idx_tab = self.tabs_control.index(self.tabs_control.select())

        self.style.change_style(idx=self.idx_tab)

        self.tabs_control.focus()
