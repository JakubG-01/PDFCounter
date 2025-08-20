import tkinter as tk
from tkinter import ttk

# Pole tekstowe jako output - wyświetlenie wyników


class FileAnalyticsOutput(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.pack(side="top", fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.results_box = tk.Text(self, height=8)
        self.results_box.pack(fill="both", expand=True)
