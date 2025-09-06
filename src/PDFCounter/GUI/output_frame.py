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
        self.results_box.heading("filename", text="File Name")
        self.results_box.heading("bw", text="B/W Pages")
        self.results_box.heading("color", text="Color Pages")
        self.results_box.heading("blank", text="Blank Pages")
        self.results_box.heading("cost", text="Cost (zł)")

        self.results_box.column("filename", width=100, anchor="center")
        self.results_box.column("bw", width=100, anchor="center")
        self.results_box.column("color", width=100, anchor="center")
        self.results_box.column("blank", width=100, anchor="center")
        self.results_box.column("cost", width=100, anchor="center")

        y_scroll = ttk.Scrollbar(
            self, orient="vertical", command=self.results_box.yview)
        x_scroll = ttk.Scrollbar(
            self, orient="horizontal", command=self.results_box.xview)
        self.results_box.configure(
            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.results_box.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
