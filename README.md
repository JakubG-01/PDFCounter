# PDFCounter 📄

PDFCounter is a lightweight tool for analyzing PDF files to count A4 page formats, estimate printing costs, and detect page types (color, black-and-white, or blank).

## Features 📌
- Select and analyze multiple PDF files from a folder
  
- Calculate the number of A4 pages for each page, regardless of its size **(refers to technical drawings)**

- Detect whether each page is **color** or **black-and-white**

- Identify **blank** or **white pages**

- Calculate total printing cost based on:
  
  - Price per **black-and-white** page

  - Price per **color** page

- Provide a detailed summary per file and overall totals

- GUI with file selection

## Configuration ⚙️

Configuration values such as prices, A4 format dimensions are stored in *config.json*:

```json
{
  "PIXEL_TO_MM": 0.3528,
  "A4_WIDTH_MM": 210,
  "A4_HEIGHT_MM": 297,
  "PRICE_FOR_BW": 1.2,
  "PRICE_FOR_COLOR": 2.3
}
```

## Usage 🚀

1. Download and unpack the program.

2. Run the program:

```
python main.py
```
3. Choose any directory by pressing '**Browse**' and analyze all the .pdf files inside by pressing '**Analyze**' button

### Example output

<img width="1002" height="332" alt="image" src="https://github.com/user-attachments/assets/11a8599f-033e-4bfe-b5a0-62da6ad14345" />

## Requirements
- Python 3.8+

- Libraries:

  - pymupdf (fitz)

  - Pillow
 
## License

MIT License – free to use and modify.
