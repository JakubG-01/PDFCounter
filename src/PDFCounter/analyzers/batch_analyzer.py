from .file_analyzer import PDFFileAnalyzer
import os


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
        self.total_blank = 0
        self.total_cost = 0.0

    def analyze_file(self, filepath):
        file_analyzer = PDFFileAnalyzer(
            filepath=filepath,
            price_bw=self.price_bw,
            price_color=self.price_color,
            pixel_to_mm=self.pixel_to_mm,
            a4_format=self.a4_format
        )
        msg = file_analyzer.analyze()
        bw, color, cost, blank = file_analyzer.get_summary()

        return msg, bw, color, blank, cost

    def analyze_all(self):
        self.total_bw = 0
        self.total_color = 0
        self.total_blank = 0
        self.total_cost = 0.0

        for filename in os.listdir(self.folder_path):
            filepath = os.path.join(self.folder_path, filename)

            if os.path.isfile(filepath) and filename.lower().endswith(".pdf"):
                msg, bw, color, blank, cost = self.analyze_file(filepath)
                self.total_bw += bw
                self.total_color += color
                self.total_blank += blank
                self.total_cost += cost

                yield (filename, msg, bw, color, blank, cost)

        yield self.print_summary()

    def print_summary(self):
        return (
            f"📊 SUMMARY:\n"
            f"  BW PAGES: {self.total_bw}\n"
            f"  COLOR PAGES: {self.total_color}\n"
            f"  BLANK PAGES: {self.total_blank}\n"
            f"  TOTAL COST: {round(self.total_cost, 2)} zł\n"
        )
