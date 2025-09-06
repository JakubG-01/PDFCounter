from PIL import Image
import io


class PDFPageAnalyzer:
    def __init__(self, page, pixel_to_mm, a4_format):
        self.page = page
        self.pixel_to_mm = pixel_to_mm
        self.a4_format = a4_format
        self.width_pt, self.height_pt = self.page.mediabox_size
        self.width_mm = round(self.width_pt * self.pixel_to_mm)
        self.height_mm = round(self.height_pt * self.pixel_to_mm)

    def get_format_ratio(self):
        return (self.width_mm * self.height_mm) / self.a4_format

    def is_color(self):
        pix = self.page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("ppm")))
        gray = img.convert("L").convert("RGB")
        original = img.convert("RGB")
        return gray.tobytes() != original.tobytes()

    def is_white_or_empty(self, tolerance=2):
        if not self.page.get_text().strip() and not self.page.get_images() and not self.page.get_drawings():
            return True  # brak tekstu, obrazów i rysunków – raczej pusta

        pix = self.page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("ppm"))).convert("RGB")

        white_pixel = (255, 255, 255)
        for pixel in img.getdata():
            if any(channel < white_pixel[i] - tolerance for i, channel in enumerate(pixel)):
                return False

        return True
