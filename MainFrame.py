from tkinter import Frame

from Stage import Stage


class MainFrame(Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stage = Stage()
        self.stage.pack()
        self.pack()