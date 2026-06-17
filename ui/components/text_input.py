import customtkinter as ctk
from config.settings import COLOR_BG_SECONDARY, COLOR_BG_DARK, COLOR_TEXT_MAIN

class TextInput(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COLOR_BG_SECONDARY)
        # Giúp Textbox tự động co giãn theo frame
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Văn bản đầu vào (Input)", text_color=COLOR_TEXT_MAIN, font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.textbox = ctk.CTkTextbox(self, fg_color=COLOR_BG_DARK, text_color=COLOR_TEXT_MAIN, wrap="word")
        self.textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def get_text(self):
        """Trích xuất chuỗi văn bản từ dòng 1 tới cuối"""
        return self.textbox.get("1.0", "end-1c")
    
    def set_text(self, text):
        """Ghi đè nội dung mới vào ô nhập (Thường dùng khi import file)"""
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)