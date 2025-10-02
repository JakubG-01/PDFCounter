import fitz
from .page_analyzer import PDFPageAnalyzer


class PDFFileAnalyzer:
    def __init__(self, filepath, price_bw,
                 price_color):
        self.filepath = filepath
        self.price_bw = price_bw
        self.price_color = price_color
        self.pages_bw = 0
        self.pages_color = 0
        self.pages_blank = 0
        self.cost = 0.0
        self.format_ratio = 0.0

    def analyze(self):
        try:
            doc = fitz.open(self.filepath)
            for page in doc.pages():
                analyzer = PDFPageAnalyzer(page)
                self.page_format_ratio = analyzer.get_format_ratio()
                is_color = analyzer.is_color()
                is_blank = analyzer.is_white_or_empty()

                if not is_blank:

                    page_cost = self.page_format_ratio * \
                        self.price_color if is_color else self.page_format_ratio * self.price_bw
                    if is_color:
                        self.pages_color += 1
                    else:
                        self.pages_bw += 1

                    self.cost += page_cost
                    self.format_ratio += self.page_format_ratio

                else:
                    self.pages_blank += 1

            return True, None

        except Exception as e:
            return False, str(e)

    def get_summary(self):
        return self.pages_bw, self.pages_color, self.format_ratio, round(self.cost, 2), self.pages_blank
