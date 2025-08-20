import os
import tkinter as tk
from tkinter import PhotoImage
from .file_select import FileSelect
from .output_frame import FileAnalyticsOutput
from .start_analyzing import StartAnalyzing


class PDFCounterApp(tk.Tk):
    def __init__(self, config):
        super().__init__()
        self.config_data = config

        # Tytuł i rozmiar okna
        self.title("PDFCounter")
        self.geometry("1000x300")
        self.minsize(width=800, height=250)
        self.selected_folder = None

        # Wgranie ikonki
        icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'pdfcounter.png')
        self.icon_img = PhotoImage(file=icon_path)
        self.iconphoto(True, self.icon_img)

        # Inicjalizacja frame'ów
        self.file_select_frame = FileSelect(self)
        self.output_frame = FileAnalyticsOutput(self)
        StartAnalyzing(self, self.output_frame,
                       self.file_select_frame, self.config_data)

        self.mainloop()
