from tkinter import ttk
from tkinterdnd2 import DND_FILES
import os


class FileAnalyticsOutput(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.pack(side="top", fill="both", expand=True)
        self.files_list = []
        self.row_count = 0

        self.create_widgets()

    def create_widgets(self):
        self.results_box = ttk.Treeview(self, columns=(
            "filename", "bw", "color", "blank", "ratio", "cost", "status"),
            show="headings",
            height=8
        )
        self.results_box.pack(fill="both", expand=True)
        self.results_box.heading("filename", text="File Name")
        self.results_box.heading("bw", text="B/W Pages")
        self.results_box.heading("color", text="Color Pages")
        self.results_box.heading("blank", text="Blank Pages")
        self.results_box.heading("ratio", text="Format Ratio")
        self.results_box.heading("cost", text="Cost (zł)")
        self.results_box.heading("status", text="Status")

        self.results_box.column("filename", width=150, anchor="center")
        self.results_box.column("bw", width=30, anchor="center")
        self.results_box.column("color", width=30, anchor="center")
        self.results_box.column("blank", width=30, anchor="center")
        self.results_box.column("ratio", width=30, anchor="center")
        self.results_box.column("cost", width=30, anchor="center")
        self.results_box.column("status", width=20, anchor="center")

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

        style = ttk.Style(self.results_box)
        style.configure("Treeview.Heading", foreground="black",
                        font=("TkDefaultFont", 10, "bold"))

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.on_drop)

    def on_drop(self, event):
        if not self.files_list:
            self.clearTree()
        files = self.tk.splitlist(event.data)

        for f in files:
            if f.lower().endswith(".pdf"):
                self.parent = os.path.basename(os.path.dirname(f))
                self.name = os.path.basename(f)
                if f not in self.files_list:
                    self.files_list.append(f)
                    self.add_records()

    def add_records(self):
        row_tag = "even" if self.row_count % 2 == 0 else "odd"
        self.results_box.insert("", "end",
                                values=(os.path.join(self.parent, self.name), "-", "-",
                                        "-", "-", "-", "PENDING"),
                                tags=(row_tag,)
                                )
        self.results_box.tag_configure("odd", background="white")
        self.results_box.tag_configure("even", background="#cce6ff")
        self.row_count += 1

    def clearTree(self):
        for item in self.results_box.get_children():
            self.results_box.delete(item)
