import fitz
from .page_analyzer import PDFPageAnalyzer
import time


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
        self.cost = 0.0
        self.output_lines = []

    def analyze(self):
        self.output_lines.append(f"🔍 Analyzing file: {self.filename}")
        t0 = time.perf_counter()
        try:
            doc = fitz.open(self.filepath)
            file_cost = 0.0
            for page in doc.pages():
                analyzer = PDFPageAnalyzer(
                    page, self.pixel_to_mm, self.a4_format)
                format_ratio = analyzer.get_format_ratio()
                is_color = analyzer.is_color()
                is_blank = analyzer.is_white_or_empty()

                # if is_blank:
                #     # print(f"  Strona {page_number} jest pusta")
                #     # print()
                #     pass

                if not is_blank:

                    page_cost = format_ratio * \
                        self.price_color if is_color else format_ratio * self.price_bw
                    if is_color:
                        self.pages_color += 1
                    else:
                        self.pages_bw += 1

                    self.cost += page_cost
                    file_cost += page_cost

                    # print(f"  Strona {page_number}")
                    # print(
                    #     f"    Format: {analyzer.width_mm}x{analyzer.height_mm} mm")
                    # print(f"    Ilosc formatek A4: {format_ratio:.2f}")
                    # print(
                    #     f"    Typ: {'Kolorowa' if is_color else 'Czarno-biała'}")
                    # print(f"    Koszt: {page_cost:.2f} zł")
                    # print()

            t1 = time.perf_counter()
            time_of_operation = t1 - t0
            self.output_lines.append(
                f"Price of printing: {self.filename} is equal {round(file_cost, 2)} PLN \n⌛ Time of operation: {time_of_operation}")

            # print(
            #     f"    Cena wydruku pliku {self.filename} wynosi {round(file_cost, 2)} zł")
            # print(f"  ⌛ Czas operacji: {time_of_operation}")

        except Exception as e:
            self.output_lines.append(
                f"  ❌ Error in file: {self.filename}: {e}")
            # print(f"  ❌ Błąd w pliku {self.filename}: {e}")

        return "\n".join(self.output_lines)

    def get_summary(self):
        return self.pages_bw, self.pages_color, round(self.cost, 2)
