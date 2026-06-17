import customtkinter as ctk
from config.settings import COLOR_BG_SECONDARY, COLOR_BTN_PRIMARY, COLOR_BTN_HOVER, COLOR_TEXT_MAIN

class ProcessorPanel(ctk.CTkFrame):
    def __init__(self, master, apply_callback):
        super().__init__(master, fg_color=COLOR_BG_SECONDARY)
        self.apply_callback = apply_callback 
        
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.chk_lower_var = ctk.BooleanVar()
        self.chk_upper_var = ctk.BooleanVar()
        self.chk_no_punct_var = ctk.BooleanVar()

        # Thêm command=self.toggle_lower
        self.chk_lower = ctk.CTkCheckBox(self, text="Chuyển về chữ thường", variable=self.chk_lower_var, text_color=COLOR_TEXT_MAIN, command=self.toggle_lower)
        self.chk_lower.grid(row=0, column=0, padx=20, pady=5, sticky="w")

        # Thêm command=self.toggle_upper
        self.chk_upper = ctk.CTkCheckBox(self, text="Chuyển về CHỮ HOA", variable=self.chk_upper_var, text_color=COLOR_TEXT_MAIN, command=self.toggle_upper)
        self.chk_upper.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.chk_no_punct = ctk.CTkCheckBox(self, text="Xóa dấu câu & Ký tự đặc biệt", variable=self.chk_no_punct_var, text_color=COLOR_TEXT_MAIN)
        self.chk_no_punct.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        self.btn_apply = ctk.CTkButton(self, text="Apply", fg_color=COLOR_BTN_PRIMARY, hover_color=COLOR_BTN_HOVER, command=self.on_apply)
        self.btn_apply.grid(row=1, column=1, padx=20, pady=10, sticky="e")

    # --- HÀM KIỂM TRA CHÉO TRẠNG THÁI ---
    def toggle_lower(self):
        """Nếu tick vào chữ thường, tự động bỏ tick chữ hoa"""
        if self.chk_lower_var.get():
            self.chk_upper_var.set(False)

    def toggle_upper(self):
        """Nếu tick vào chữ hoa, tự động bỏ tick chữ thường"""
        if self.chk_upper_var.get():
            self.chk_lower_var.set(False)

    def on_apply(self):
        options = {
            "lower": self.chk_lower_var.get(),
            "upper": self.chk_upper_var.get(),
            "no_punct": self.chk_no_punct_var.get()
        }
        self.apply_callback(options)