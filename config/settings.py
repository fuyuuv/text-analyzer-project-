# --- CẤU HÌNH THÔNG SỐ ỨNG DỤNG ---
APP_TITLE = "TEXT ANALYZER"
APP_GEOMETRY = "1280x960"
APPEARANCE_MODE = "dark"  # Bắt buộc chế độ tối
DEFAULT_TOP_N = 5         # Giá trị mặc định cho top N từ

# --- BẢNG MÀU ---
COLOR_BG_MAIN = "#36393f"      # Màu nền cửa sổ chính
COLOR_BG_SECONDARY = "#2f3136" # Màu nền các Component
COLOR_BG_DARK = "#202225"      # Màu nền ô Text
COLOR_BTN_PRIMARY = "#5865F2"  # Màu Blurple
COLOR_BTN_HOVER = "#4752C4"    # Màu khi di chuột vào nút
COLOR_TEXT_MAIN = "#dcddde"    # Màu chữ mặc định

# --- DANH SÁCH STOP WORDS TIẾNG VIỆT ---
VIETNAMESE_STOP_WORDS = {
    "là", "của", "và", "thì", "mà", "ở", "có", "cho", "được", "với", "một", "các",
    "những", "để", "như", "trên", "tại", "này", "khi", "đã", "sẽ", "đang", "từ",
    "đến", "trong", "ra", "vào", "về", "cũng", "nhưng", "lại", "rằng", "nếu", "bởi"
}

# --- TỪ ĐIỂN VIẾT TẮT THÔNG DỤNG ---
ABBREVIATIONS_DICT = {
    "ko": "không",
    "k": "không", 
    "hong": "không", 
    "hông": "không",
    "dc": "được", 
    "đc": "được", 
    "vs": "với", 
    "bn": "bạn", 
    "r": "rồi", 
    "rùi": "rồi",
    "đg": "đang", 
    "thik": "thích", 
    "cx": "cũng"
}