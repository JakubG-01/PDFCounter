import os
from .file_analyzer import PDFFileAnalyzer


class PDFBatchAnalyzer:
    def __init__(self, folder_path, price_bw,
                 price_color, pixel_to_mm, a4_format):
        self.folder_path = folder_path
        self.price_bw = price_bw
        self.price_color = price_color
        self.pixel_to_mm = pixel_to_mm
        self.a4_format = a4_format
        self.total_bw = 0
        self.total_color = 0
        self.total_cost = 0.0

    def analyze_all(self):
        self.result = ""
        for filename in os.listdir(self.folder_path):
            filepath = os.path.join(self.folder_path, filename)
            if os.path.isfile(filepath) and filename.lower().endswith(".pdf"):
                file_analyzer = PDFFileAnalyzer(
                    filepath=filepath,
                    price_bw=self.price_bw,
                    price_color=self.price_color,
                    pixel_to_mm=self.pixel_to_mm,
                    a4_format=self.a4_format
                )
                self.result += file_analyzer.analyze() + "\n"
                bw, color, cost = file_analyzer.get_summary()
                self.total_bw += bw
                self.total_color += color
                self.total_cost += cost
            self.result += "\n"

        return self.print_summary()

    def print_summary(self):
        summary_text = self.result + \
            f"📊 SUMMARY: \nBW PAGES: {self.total_bw} \nCOLOR PAGES: {self.total_color} \nTOTAL COST: {round(self.total_cost, 2)} PLN"
        return summary_text
