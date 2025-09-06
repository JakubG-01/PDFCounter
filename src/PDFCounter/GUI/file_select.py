from tkinter import ttk
from tkinter import filedialog


class FileSelect(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)

        self.label = ttk.Label(self, text="Select folder:").pack(
            side="left", padx=(0, 10))
        self.pack(side='top', fill='x')

        self.selected_folder = ""

        self.create_widgets()

    def create_widgets(self):
        button = ttk.Button(self, text="Browse")
        self.chosen_directory = ttk.Label(
            self, text="Folder was not selected")
        self.chosen_directory.pack(side="right")
        button.pack(side="left")
        button.config(command=self.chooseDirectory)

    def chooseDirectory(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder == "":
            self.chosen_directory.config(text="Folder was not selected")
        else:
            self.chosen_directory.config(
                text=f"Selected folder: {self.selected_folder}")
