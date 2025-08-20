import json
from GUI import PDFCounterApp

with open("config.json", "r") as f:
    config = json.load(f)

a4_format = config["A4_WIDTH_MM"] * config["A4_HEIGHT_MM"]

if __name__ == "__main__":
    app = PDFCounterApp(config)
