import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from analyzers import PDFBatchAnalyzer


class StartAnalyzing(ttk.Frame):
    def __init__(self, parent, output_frame, file_select_frame, config_data):
        super().__init__(parent, padding=10)
        self.pack(side="left", fill="both", expand=True)
        self.output_frame = output_frame
        self.file_select_frame = file_select_frame
        self.config_data = config_data

        self.create_widgets()

    def create_widgets(self):
        self.progress_bar = ttk.Progressbar(
            self, length=400, mode="determinate"
        )
        self.progress_bar.pack(side="left", fill="both", padx=(0, 10))

        analyze_button = ttk.Button(
            self, text="Analyze", command=self.changeProgress
        )
        analyze_button.pack(side="left")

    def changeProgress(self):
        self.progress_bar['value'] = 0
        self.output_frame.results_box.config(state=tk.NORMAL)
        self.output_frame.results_box.delete("1.0", "end")

        folder = self.file_select_frame.selected_folder
        if not folder:
            messagebox.showwarning(
                "Warning", "Please select a folder before proceeding")
            self.output_frame.results_box.config(state=tk.DISABLED)
            return

        pdf_files = [f for f in os.listdir(
            folder) if f.lower().endswith(".pdf")]
        amount_of_files = len(pdf_files)
        if amount_of_files == 0:
            messagebox.showwarning(
                "Warning", "No PDF files found in this folder")
            self.output_frame.results_box.config(state=tk.DISABLED)
            return

        progress_step = 100 / amount_of_files

        self.analyzer = PDFBatchAnalyzer(
            folder_path=folder,
            price_bw=self.config_data["PRICE_FOR_BW"],
            price_color=self.config_data["PRICE_FOR_COLOR"],
            pixel_to_mm=self.config_data["PIXEL_TO_MM"],
            a4_format=self.config_data["A4_WIDTH_MM"] *
            self.config_data["A4_HEIGHT_MM"]
        )

        for result in self.analyzer.analyze_all():
            if isinstance(result, tuple):
                filename, msg, bw, color, blank, cost = result
                self.output_frame.results_box.insert("end", msg + "\n")
            else:
                self.output_frame.results_box.insert("end", result + "\n")

            self.progress_bar['value'] += progress_step
            self.update_idletasks()
        self.output_frame.results_box.config(state=tk.DISABLED)
        messagebox.showinfo(
            "Analysis completed", "Analysis of selected files has been completed successfully"
        )
