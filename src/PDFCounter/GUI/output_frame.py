from tkinter import ttk


class FileAnalyticsOutput(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.pack(side="top", fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.results_box = ttk.Treeview(self, columns=(
            "filename", "bw", "color", "blank", "cost"),
            show="headings",
            height=8
        )
        self.results_box.pack(fill="both", expand=True)
