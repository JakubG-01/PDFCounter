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

Configuration values such as prices are stored in *config.json*:

```json
{
  "PRICE_FOR_BW": 1.2,
  "PRICE_FOR_COLOR": 2.3
}
```

## Usage 🚀

You can run the program in two ways:

### 1. Run from source (using Python)
1. Download and unpack the program.
   
2. Open a terminal in the program folder.
   
3. Run:
   ```bash
   python main.py

4. Choose any directory by pressing Browse and analyze all the .pdf files inside by pressing Analyze.

### 2. Run the prebuilt binary

1. Go to the Releases section of this repository.

2. Download the binary file for your system.

3. Unpack it and run the executable directly (no Python required).

4. Use the Browse and Analyze buttons as above.

### Example output

<img width="802" height="432" alt="image" src="https://github.com/user-attachments/assets/d46943aa-e5f5-45c0-a5e6-7e285c2a768f" />

## Requirements
- Python 3.8+

- Libraries:

  - pymupdf (fitz)

  - Pillow
 
## License

MIT License – free to use and modify.
