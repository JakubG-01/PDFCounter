from math import ceil, floor
from PIL import Image
import io

A4_WIDTH_MM = 210
A4_HEIGHT_MM = 297
A4_FORMAT = A4_HEIGHT_MM * A4_WIDTH_MM
PIXEL_TO_MM = 0.352778


class PDFPageAnalyzer:
    def __init__(self, page):
        self.page = page
        self.pixel_to_mm = PIXEL_TO_MM
        self.a4_format = A4_FORMAT

        mediabox = self.page.mediabox
        self.width_pt = mediabox.x1 - mediabox.x0
        self.height_pt = mediabox.y1 - mediabox.y0

        self.width_mm = round(self.width_pt * self.pixel_to_mm)
        self.height_mm = round(self.height_pt * self.pixel_to_mm)

    def get_format_ratio(self):
        area_ratio = (self.width_mm * self.height_mm) / self.a4_format
        if (area_ratio * 100) % 100 <= 9:
            rounded_to_half = floor(area_ratio * 2) / 2
            return rounded_to_half
        else:
            rounded_to_half = ceil(area_ratio * 2) / 2
            return rounded_to_half

    def is_color(self):
        pix = self.page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("ppm")))
        gray = img.convert("L").convert("RGB")
        original = img.convert("RGB")
        return gray.tobytes() != original.tobytes()

    def is_white_or_empty(self, tolerance=2):
        if not self.page.get_text().strip() and not self.page.get_images() and not self.page.get_drawings():
            return True

        pix = self.page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("ppm"))).convert("RGB")

        white_pixel = (255, 255, 255)
        for pixel in img.getdata():
            if any(channel < white_pixel[i] - tolerance for i, channel in enumerate(pixel)):
                return False

        return True
