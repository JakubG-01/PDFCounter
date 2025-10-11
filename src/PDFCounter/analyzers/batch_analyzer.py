from .file_analyzer import PDFFileAnalyzer
import os


class PDFBatchAnalyzer:
    def __init__(self, folder_path, price_bw, price_color, files_list):
        self.folder_path = folder_path
        self.files_list = files_list
        self.price_bw = price_bw
        self.price_color = price_color
        self.total_bw = 0
        self.total_color = 0
        self.total_blank = 0
        self.total_cost = 0.0
        self.total_format_ratios = 0.0

    def analyze_file(self, filepath):
        file_analyzer = PDFFileAnalyzer(
            filepath=filepath,
            price_bw=self.price_bw,
            price_color=self.price_color,
        )
        ok_msg, error_msg = file_analyzer.analyze()
        bw, color, ratio, cost, blank = file_analyzer.get_summary()

        if ok_msg:
            return filepath.split("/")[-1], bw, color, blank, ratio, cost, "OK"
        else:
            return filepath.split("/")[-1], None, None, None, None, None, f"Error: {error_msg}"

    def analyze_folder(self):
        for filename in os.listdir(self.folder_path):
            filepath = os.path.join(self.folder_path, filename)

            if os.path.isfile(filepath) and filename.lower().endswith(".pdf"):
                filename, bw, color, blank, ratio, cost, status = self.analyze_file(
                    filepath)
                if status == "OK":
                    if bw is not None:
                        self.total_bw += bw
                    if color is not None:
                        self.total_color += color
                    if blank is not None:
                        self.total_blank += blank
                    if ratio is not None:
                        self.total_format_ratios += ratio
                    if cost is not None:
                        self.total_cost += cost

                yield (filename, bw, color, blank, ratio, cost, status)

        yield ("TOTAL", self.total_bw, self.total_color, self.total_blank, self.total_format_ratios, self.total_cost, "COMPLETED")

    def analyze_list(self):
        for filename in (self.files_list):
            filename, bw, color, blank, ratio, cost, status = self.analyze_file(
                filename)
            if status == "OK":
                if bw is not None:
                    self.total_bw += bw
                if color is not None:
                    self.total_color += color
                if blank is not None:
                    self.total_blank += blank
                if ratio is not None:
                    self.total_format_ratios += ratio
                if cost is not None:
                    self.total_cost += cost

            yield (filename, bw, color, blank, ratio, cost, status)

        yield ("TOTAL", self.total_bw, self.total_color, self.total_blank, self.total_format_ratios, self.total_cost, "COMPLETED")
