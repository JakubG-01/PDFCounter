import os
from tkinter import messagebox
from tkinter import ttk
from analyzers import PDFBatchAnalyzer


class StartAnalyzing(ttk.Frame):
    def __init__(self, parent, output_frame, file_select_frame, config_data):
        super().__init__(parent, padding=10)
        self.pack(side="left", fill="both", expand=True)
        self.output_frame = output_frame
        self.file_select_frame = file_select_frame
        self.config_data = config_data

        self.create_widgets()

    def create_widgets(self):
        self.progress_bar = ttk.Progressbar(
            self, length=400, mode="determinate"
        )
        self.progress_bar.pack(side="left", fill="both", padx=(0, 10))

        analyze_button = ttk.Button(
            self, text="Analyze", command=self.changeProgress
        )
        analyze_button.pack(side="left")

        analyze_button = ttk.Button(
            self, text="Clear", command=self.clearAll
        )
        analyze_button.pack(side="left")

    def clearTree(self):
        for item in self.output_frame.results_box.get_children():
            self.output_frame.results_box.delete(item)

    def colorRows(self):
        self.output_frame.results_box.tag_configure(
            "total", background="#e0e0e0", font=("TkDefaultFont", 10, "bold"))
        self.output_frame.results_box.tag_configure(
            "error", foreground="red"
        )
        self.output_frame.results_box.tag_configure(
            "odd", background="white")
        self.output_frame.results_box.tag_configure(
            "even", background="#cce6ff")

    def msgWarningNoFolderOrNoFiles(self):
        messagebox.showwarning(
            "Warning", "Please select a folder or drag and drop files before proceeding")
        return

    def msgWarningNoPDF(self):
        messagebox.showwarning(
            "Warning", "No PDF files found in this folder")
        return

    def msgSuccess(self):
        messagebox.showinfo(
            "Analysis completed", "Analysis of selected files has been completed successfully"
        )

    def changeProgress(self):
        row_count = 0
        self.progress_bar['value'] = 0
        self.clearTree()

        if not self.output_frame.files_list and not self.file_select_frame.selected_folder:
            self.msgWarningNoFolderOrNoFiles()

        else:
            if not self.output_frame.files_list:
                folder = self.file_select_frame.selected_folder
                pdf_files = [f for f in os.listdir(
                    folder) if f.lower().endswith(".pdf")]
                amount_of_files = len(pdf_files)
                if amount_of_files == 0:
                    self.msgWarningNoPDF()

                progress_step = 100 / amount_of_files

                self.analyzer = PDFBatchAnalyzer(
                    folder_path=folder,
                    price_bw=self.config_data["PRICE_FOR_BW"],
                    price_color=self.config_data["PRICE_FOR_COLOR"],
                    files_list=None
                )

                for filename, bw, color, blank, ratio, cost, status in self.analyzer.analyze_folder():
                    if filename == "TOTAL":
                        self.output_frame.results_box.insert("", "end",
                                                             values=("TOTAL",
                                                                     self.analyzer.total_bw,
                                                                     self.analyzer.total_color,
                                                                     self.analyzer.total_blank,
                                                                     self.analyzer.total_format_ratios,
                                                                     f"{self.analyzer.total_cost:.2f}",
                                                                     status),
                                                             tags=("total",)
                                                             )
                        self.update_idletasks()
                    elif status != "OK":
                        self.output_frame.results_box.insert(
                            "", "end",
                            values=(filename, "", "", "", "", "", status),
                            tags=("error",)
                        )

                    else:
                        row_tag = "even" if row_count % 2 == 0 else "odd"
                        self.output_frame.results_box.insert("", "end",
                                                             values=(
                                                                 filename,
                                                                 bw,
                                                                 color,
                                                                 blank,
                                                                 ratio,
                                                                 f"{cost:.2f}",
                                                                 status),
                                                             tags=(row_tag,))
                        self.progress_bar['value'] += progress_step

                        self.update_idletasks()
                        row_count += 1
                    self.colorRows()
                self.file_select_frame.selected_folder = ""

            else:

                amount_of_files = len(self.output_frame.files_list)
                if amount_of_files == 0:
                    self.msgWarningNoPDF()

                progress_step = 100 / amount_of_files

                self.analyzer = PDFBatchAnalyzer(
                    folder_path=None,
                    price_bw=self.config_data["PRICE_FOR_BW"],
                    price_color=self.config_data["PRICE_FOR_COLOR"],
                    files_list=self.output_frame.files_list
                )

                for filename, bw, color, blank, ratio, cost, status in self.analyzer.analyze_list():
                    if filename == "TOTAL":
                        self.output_frame.results_box.insert("", "end",
                                                             values=("TOTAL",
                                                                     self.analyzer.total_bw,
                                                                     self.analyzer.total_color,
                                                                     self.analyzer.total_blank,
                                                                     self.analyzer.total_format_ratios,
                                                                     f"{self.analyzer.total_cost:.2f}",
                                                                     status),
                                                             tags=("total",)
                                                             )
                        self.update_idletasks()
                    elif status != "OK":
                        self.output_frame.results_box.insert(
                            "", "end",
                            values=(filename, "", "", "", "", "", status),
                            tags=("error",)
                        )

                    else:
                        row_tag = "even" if row_count % 2 == 0 else "odd"
                        self.output_frame.results_box.insert("", "end",
                                                             values=(
                                                                 filename,
                                                                 bw,
                                                                 color,
                                                                 blank,
                                                                 ratio,
                                                                 f"{cost:.2f}",
                                                                 status),
                                                             tags=(row_tag,))
                        self.progress_bar['value'] += progress_step

                        self.update_idletasks()
                        row_count += 1
                    self.colorRows()
                self.output_frame.files_list.clear()
            self.msgSuccess()
            row_count = 0

    def clearAll(self):
        self.clearTree()
        self.progress_bar['value'] = 0
        self.output_frame.files_list.clear()
        self.file_select_frame.selected_folder = ""
        self.file_select_frame.chosen_directory.config(
            text="Folder was not selected")
