import tkinter as tk
from tkinter import ttk
from analyzers import PDFBatchAnalyzer

# Progress bar + przycisk Analizuj - rozpoczęcie analizy plików


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
            self, length=400, mode="determinate")
        self.progress_bar.pack(side="left", fill="both", padx=(0, 10))
        analyze_button = ttk.Button(
            self, text="Analyze", command=self.changeProgress)
        analyze_button.pack(side="left")

    def changeProgress(self):
        self.output_frame.results_box.config(state=tk.NORMAL)
        self.output_frame.results_box.delete("1.0", "end")
        self.progress_bar['value'] += 5
        self.analyzer = PDFBatchAnalyzer(folder_path=self.file_select_frame.selected_folder,
                                         price_bw=self.config_data["PRICE_FOR_BW"],
                                         price_color=self.config_data["PRICE_FOR_COLOR"],
                                         pixel_to_mm=self.config_data["PIXEL_TO_MM"],
                                         a4_format=self.config_data["A4_WIDTH_MM"] *
                                         self.config_data["A4_HEIGHT_MM"]
                                         )
        result = self.analyzer.analyze_all()
        self.output_frame.results_box.insert("end", result)
        self.output_frame.results_box.config(state=tk.DISABLED)
