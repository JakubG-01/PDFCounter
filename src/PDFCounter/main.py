import os
import json
from GUI import PDFCounterApp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(BASE_DIR, "config", "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

if __name__ == "__main__":
    app = PDFCounterApp(config)
