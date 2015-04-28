#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
" Python version of Memorise SDL game (except that this version uses Tkinter and not SDL like the c++ version)
"""

from tkinter import Tk, Menu
from ttk import Frame, Button, Style

class MemoriseFrontend(Frame):
    version = "0.1-py"
    padding = 10

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.style = Style()
        self.style.theme_use("default")

        self._initUI()

    def _initUI(self):
        self.parent.title("Memorise v" + self.version)

        self.columnconfigure(0, pad=self.padding)
        self.columnconfigure(1, pad=self.padding)
        self.columnconfigure(2, pad=self.padding)
        self.columnconfigure(3, pad=self.padding)
        self.columnconfigure(4, pad=self.padding)

        self.rowconfigure(0, pad=self.padding)
        self.rowconfigure(1, pad=self.padding)
        self.rowconfigure(2, pad=self.padding)
        self.rowconfigure(3, pad=self.padding)
        self.rowconfigure(4, pad=self.padding)

        # Row 1
        btnUp = Button(self, text="Up", command=self._onUpBtn)
        btnUp.grid(row=1, column=2)

        # Row 2
        btnLeft = Button(self, text="Left", command=self._onLeftBtn)
        btnLeft.grid(row=2, column=1)

        # Row 2
        btnRight = Button(self, text="Right", command=self._onRightBtn)
        btnRight.grid(row=2, column=3)

        # Row 3
        btnDown = Button(self, text="Down", command=self._onDownBtn)
        btnDown.grid(row=3, column=2)

        self.pack()

    def _onUpBtn(self):
        pass

    def _onLeftBtn(self):
        pass

    def _onRightBtn(self):
        pass

    def _onDownBtn(self):
        pass


def main():
    root = Tk()
    app = MemoriseFrontend(root)
    root.mainloop()

main()
