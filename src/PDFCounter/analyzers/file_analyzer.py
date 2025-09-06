import fitz
from .page_analyzer import PDFPageAnalyzer


class PDFFileAnalyzer:
    def __init__(self, filepath, price_bw,
                 price_color, pixel_to_mm, a4_format):
        self.filepath = filepath
        self.filename = filepath.split("/")[-1]
        self.price_bw = price_bw
        self.price_color = price_color
        self.pixel_to_mm = pixel_to_mm
        self.a4_format = a4_format
        self.pages_bw = 0
        self.pages_color = 0
        self.pages_blank = 0
        self.cost = 0.0
        self.output_lines = []

    def analyze(self):
        try:
            doc = fitz.open(self.filepath)
            file_cost = 0.0
            for page in doc.pages():
                analyzer = PDFPageAnalyzer(
                    page, self.pixel_to_mm, self.a4_format)
                format_ratio = analyzer.get_format_ratio()
                is_color = analyzer.is_color()
                is_blank = analyzer.is_white_or_empty()

                if not is_blank:

                    page_cost = format_ratio * \
                        self.price_color if is_color else format_ratio * self.price_bw
                    if is_color:
                        self.pages_color += 1
                    else:
                        self.pages_bw += 1

                    self.cost += page_cost
                    file_cost += page_cost

                else:
                    self.pages_blank += 1

            return True, None

        except Exception as e:
            return False, str(e)

    def get_summary(self):
        return self.pages_bw, self.pages_color, round(self.cost, 2), self.pages_blank
