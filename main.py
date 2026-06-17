from ui.main_window import MainWindow

if __name__ == "__main__":
    # Khởi tạo instance của cửa sổ giao diện chính
    app = MainWindow()
    
    # Bắt đầu vòng lặp sự kiện (Event Loop) của ứng dụng
    app.mainloop()