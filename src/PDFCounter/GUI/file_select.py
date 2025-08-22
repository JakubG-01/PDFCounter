from pydoc import text
from tkinter import ttk
from tkinter import filedialog

# Label + przycisk "Wybierz folder:" - wybranie i wyświetlenie danej scieżki


class FileSelect(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)

        self.label = ttk.Label(self, text="Select folder:").pack(
            side="left", padx=(0, 10))
        self.pack(side='top', fill='x')

        self.create_widgets()

    def create_widgets(self):
        button = ttk.Button(self, text="Browse")
        self.chosen_directory = ttk.Label(
            self, text=f"Folder was not selected")
        self.chosen_directory.pack(side="right")
        button.pack(side="left")
        button.config(command=self.chooseDirectory)

    def chooseDirectory(self):
        self.selected_folder = filedialog.askdirectory()
        self.chosen_directory.config(
            text=f"Selected folder: {self.selected_folder}")
