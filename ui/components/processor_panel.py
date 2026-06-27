import customtkinter as ctk
from config.settings import COLOR_BG_SECONDARY, COLOR_BTN_PRIMARY, COLOR_BTN_HOVER, COLOR_TEXT_MAIN

class ProcessorPanel(ctk.CTkFrame):
    def __init__(self, master, apply_callback):
        super().__init__(master, fg_color=COLOR_BG_SECONDARY)
        self.apply_callback = apply_callback 
        
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.chk_lower_var = ctk.BooleanVar()
        self.chk_upper_var = ctk.BooleanVar()
        self.chk_title_var = ctk.BooleanVar()
        self.chk_sentence_var = ctk.BooleanVar()
        self.chk_whitespace_var = ctk.BooleanVar()
        self.chk_expand_var = ctk.BooleanVar()

        self.chk_lower = ctk.CTkCheckBox(self, text="Chuyển về chữ thường", variable=self.chk_lower_var, text_color=COLOR_TEXT_MAIN, command=lambda: self.toggle_case("lower"))
        self.chk_lower.grid(row=0, column=0, padx=20, pady=5, sticky="w")

        self.chk_upper = ctk.CTkCheckBox(self, text="Chuyển về CHỮ HOA", variable=self.chk_upper_var, text_color=COLOR_TEXT_MAIN, command=lambda: self.toggle_case("upper"))
        self.chk_upper.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        
        self.chk_title = ctk.CTkCheckBox(self, text="Viết hoa chữ đầu mỗi từ", variable=self.chk_title_var, text_color=COLOR_TEXT_MAIN, command=lambda: self.toggle_case("title"))
        self.chk_title.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        
        self.chk_sentence = ctk.CTkCheckBox(self, text="Viết hoa chữ đầu mỗi câu", variable=self.chk_sentence_var, text_color=COLOR_TEXT_MAIN, command=lambda: self.toggle_case("sentence"))
        self.chk_sentence.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        self.chk_whitespace = ctk.CTkCheckBox(self, text="Xóa khoảng trắng thừa", variable=self.chk_whitespace_var, text_color=COLOR_TEXT_MAIN)
        self.chk_whitespace.grid(row=4, column=0, padx=20, pady=5, sticky="w")

        self.chk_expand = ctk.CTkCheckBox(self, text="Mở rộng từ viết tắt", variable=self.chk_expand_var, text_color=COLOR_TEXT_MAIN)
        self.chk_expand.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        self.btn_apply = ctk.CTkButton(self, text="Apply", fg_color=COLOR_BTN_PRIMARY, hover_color=COLOR_BTN_HOVER, command=self.on_apply)
        self.btn_apply.grid(row=2, column=1, padx=20, pady=10, sticky="e")

    def toggle_case(self, active_mode):
        if active_mode != "lower": self.chk_lower_var.set(False)
        if active_mode != "upper": self.chk_upper_var.set(False)
        if active_mode != "title": self.chk_title_var.set(False)
        if active_mode != "sentence": self.chk_sentence_var.set(False)

    def on_apply(self):
        options = {
            "lower": self.chk_lower_var.get(),
            "upper": self.chk_upper_var.get(),
            "title": self.chk_title_var.get(),
            "sentence": self.chk_sentence_var.get(),
            "whitespace": self.chk_whitespace_var.get(),
            "expand_abbr": self.chk_expand_var.get()
        }
        self.apply_callback(options)