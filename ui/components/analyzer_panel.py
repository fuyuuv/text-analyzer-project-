import customtkinter as ctk
from config.settings import COLOR_BG_SECONDARY, COLOR_BTN_PRIMARY, COLOR_BTN_HOVER, COLOR_TEXT_MAIN, DEFAULT_TOP_N

class AnalyzerPanel(ctk.CTkFrame):
    def __init__(self, master, analyze_callback):
        super().__init__(master, fg_color=COLOR_BG_SECONDARY)
        self.analyze_callback = analyze_callback
        self.top_n_data = [] # Lưu dữ liệu để hiển thị trong popup

        self.grid_columnconfigure((0, 1), weight=1)

        # Khung nhập giá trị N
        self.frame_top_n = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_top_n.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        
        ctk.CTkLabel(self.frame_top_n, text="Tìm Top N từ:", text_color=COLOR_TEXT_MAIN).pack(side="left", padx=(0, 5))
        self.top_n_var = ctk.StringVar(value=str(DEFAULT_TOP_N))
        self.entry_top_n = ctk.CTkEntry(self.frame_top_n, textvariable=self.top_n_var, width=50)
        self.entry_top_n.pack(side="left")
        
        self.btn_analyze = ctk.CTkButton(self, text="Phân tích", font=("Arial", 14, "bold"), fg_color=COLOR_BTN_PRIMARY, hover_color=COLOR_BTN_HOVER, command=self.on_analyze)
        self.btn_analyze.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="e")

        font_stat = ("Arial", 13)
        self.lbl_chars = ctk.CTkLabel(self, text="Số ký tự: --", text_color=COLOR_TEXT_MAIN, font=font_stat)
        self.lbl_chars.grid(row=1, column=0, padx=20, pady=(15, 2), sticky="w")

        self.lbl_words = ctk.CTkLabel(self, text="Số từ: --", text_color=COLOR_TEXT_MAIN, font=font_stat)
        self.lbl_words.grid(row=2, column=0, padx=20, pady=2, sticky="w")

        self.lbl_sentences = ctk.CTkLabel(self, text="Số câu: --", text_color=COLOR_TEXT_MAIN, font=font_stat)
        self.lbl_sentences.grid(row=1, column=1, padx=20, pady=(15, 2), sticky="w")

        self.lbl_most_freq = ctk.CTkLabel(self, text="Từ xuất hiện nhiều nhất: --", text_color=COLOR_TEXT_MAIN, font=font_stat)
        self.lbl_most_freq.grid(row=2, column=1, padx=20, pady=2, sticky="w")

        self.btn_show_top_n = ctk.CTkButton(self, text="Xem chi tiết Top N từ", state="disabled", command=self.show_top_n_popup)
        self.btn_show_top_n.grid(row=3, column=0, columnspan=2, padx=20, pady=(15, 10), sticky="ew")

    def on_analyze(self):
        """Ép kiểu số N và kích hoạt hàm phân tích ở MainWindow"""
        try:
            n = int(self.top_n_var.get())
        except ValueError:
            n = DEFAULT_TOP_N
        self.analyze_callback(n)

    def update_results(self, data):
        """Hàm nhận kết quả từ Tầng Core và in ra màn hình"""
        self.lbl_chars.configure(text=f"Số ký tự: {data['char_count']}")
        self.lbl_words.configure(text=f"Số từ: {data['word_count']}")
        self.lbl_sentences.configure(text=f"Số câu: {data['sentence_count']}")
        self.lbl_most_freq.configure(text=f"Từ xuất hiện nhiều nhất: {data['most_frequent']}")
        
        self.top_n_data = data['top_n_words']
        # Mở khóa nút xem chi tiết Top N
        self.btn_show_top_n.configure(state="normal", fg_color=COLOR_BTN_PRIMARY)

    def show_top_n_popup(self):
        """Khởi tạo cửa sổ Toplevel nổi lên trên ứng dụng chính để xem danh sách"""
        popup = ctk.CTkToplevel(self)
        popup.title("Chi tiết tần suất từ vựng")
        popup.geometry("350x450")
        popup.attributes("-topmost", True) 

        scroll_frame = ctk.CTkScrollableFrame(popup)
        scroll_frame.pack(fill="both", expand=True, padx=15, pady=15)

        for idx, (word, count) in enumerate(self.top_n_data, 1):
            lbl = ctk.CTkLabel(scroll_frame, text=f"{idx}. {word}: {count} lần", text_color=COLOR_TEXT_MAIN, font=("Arial", 14))
            lbl.pack(anchor="w", pady=5)