import customtkinter as ctk
from tkinter import messagebox, filedialog

from config.settings import APP_TITLE, APP_GEOMETRY, APPEARANCE_MODE, COLOR_BG_MAIN
from ui.components.text_input import TextInput
from ui.components.result_view import ResultView
from ui.components.processor_panel import ProcessorPanel
from ui.components.analyzer_panel import AnalyzerPanel

from core import text_processor, text_analyzer
from utils.file_manager import read_file
from exceptions.custom_exceptions import EmptyTextException, InvalidFileException

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 1. Khởi tạo thuộc tính cửa sổ dựa trên settings
        self.title(APP_TITLE)
        self.geometry(APP_GEOMETRY)
        ctk.set_appearance_mode(APPEARANCE_MODE)
        self.configure(fg_color=COLOR_BG_MAIN)

        # 2. Cấu hình lưới (Grid Layout) theo tỷ lệ 3:1 (Text chiếm 75%, Control chiếm 25%)
        self.grid_rowconfigure(0, weight=3) 
        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure((0, 1), weight=1)

        # 3. Gắn các Component giao diện vào lưới
        self.text_input = TextInput(self)
        self.text_input.grid(row=0, column=0, padx=(15, 7.5), pady=(15, 7.5), sticky="nsew")

        self.result_view = ResultView(self)
        self.result_view.grid(row=0, column=1, padx=(7.5, 15), pady=(15, 7.5), sticky="nsew")

        self.processor_panel = ProcessorPanel(self, apply_callback=self.handle_process_text)
        self.processor_panel.grid(row=1, column=0, padx=(15, 7.5), pady=(7.5, 15), sticky="nsew")

        self.analyzer_panel = AnalyzerPanel(self, analyze_callback=self.handle_analyze_text)
        self.analyzer_panel.grid(row=1, column=1, padx=(7.5, 15), pady=(7.5, 15), sticky="nsew")

        # 4. Tích hợp nút Import File vào khung TextInput
        self.btn_import = ctk.CTkButton(self.text_input, text="Import .txt", width=80, command=self.import_file)
        self.btn_import.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    # --- CÁC HÀM ĐIỀU PHỐI (CONTROLLER) ---
    def import_file(self):
        """Mở hộp thoại chọn file và truyền dữ liệu vào Tầng Utils"""
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filepath:
            try:
                content = read_file(filepath)
                self.text_input.set_text(content)
            except Exception as e:
                messagebox.showerror("Lỗi Import", str(e))

    def handle_process_text(self, options):
        """Hứng sự kiện từ ProcessorPanel, gọi Core xử lý chuỗi và in ra ResultView"""
        text = self.text_input.get_text()
        if not text.strip():
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản vào khung Input!")
            return
        
        if options["lower"]:
            text = text_processor.to_lower_case(text)
        elif options["upper"]:
            text = text_processor.to_upper_case(text)
        
        if options["no_punct"]:
            text = text_processor.remove_special_characters(text)

        self.result_view.set_text(text)

    def handle_analyze_text(self, top_n):
        """Hứng sự kiện từ AnalyzerPanel, ném dữ liệu cho Core thống kê"""
        text = self.text_input.get_text()
        try:
            results = text_analyzer.analyze(text, top_n)
            self.analyzer_panel.update_results(results)
        except EmptyTextException as e:
            messagebox.showwarning("Cảnh báo", str(e))
        except Exception as e:
            messagebox.showerror("Lỗi Phân Tích", f"Đã xảy ra lỗi: {str(e)}")