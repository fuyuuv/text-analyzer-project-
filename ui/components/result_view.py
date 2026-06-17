import customtkinter as ctk
from config.settings import COLOR_BG_SECONDARY, COLOR_BG_DARK, COLOR_TEXT_MAIN

class ResultView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COLOR_BG_SECONDARY)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Văn bản đã xử lý (Output)", text_color=COLOR_TEXT_MAIN, font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Thiết lập state="disabled" để ngăn người dùng gõ vào khung kết quả
        self.textbox = ctk.CTkTextbox(self, fg_color=COLOR_BG_DARK, text_color=COLOR_TEXT_MAIN, state="disabled", wrap="word")
        self.textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def set_text(self, text):
        """Mở khóa textbox, cập nhật kết quả từ Tầng Core, sau đó khóa lại"""
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
        self.textbox.configure(state="disabled")