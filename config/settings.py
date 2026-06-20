# --- CẤU HÌNH THÔNG SỐ ỨNG DỤNG ---
APP_TITLE = "TEXT ANALYZER"
APP_GEOMETRY = "1280x960"
APPEARANCE_MODE = "dark"  # Bắt buộc chế độ tối
DEFAULT_TOP_N = 5         # Giá trị mặc định cho top N từ

# --- BẢNG MÀU DISCORD THEME ---
COLOR_BG_MAIN = "#36393f"      # Màu nền cửa sổ chính
COLOR_BG_SECONDARY = "#2f3136" # Màu nền các Component
COLOR_BG_DARK = "#202225"      # Màu nền ô Text
COLOR_BTN_PRIMARY = "#5865F2"  # Màu Blurple
COLOR_BTN_HOVER = "#4752C4"    # Màu khi di chuột vào nút
COLOR_TEXT_MAIN = "#dcddde"    # Màu chữ mặc định

# --- CẤU HÌNH XỬ LÝ NGÔN NGỮ ---
# Pattern loại bỏ ký tự đặc biệt, chỉ giữ lại chữ cái (gồm tiếng Việt), số và khoảng trắng
VIET_CHAR_PATTERN = (
    r'[^a-zA-Z0-9\s'
    r'àáạảãâầấậẩẫăằắặẳẵ'
    r'èéẹẻẽêềếệểễ'
    r'ìíịỉĩ'
    r'òóọỏõôồốộổỗơờớợởỡ'
    r'ùúụủũưừứựửữ'
    r'ỳýỵỷỹđ'
    r'ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ'
    r'ÈÉẸẺẼÊỀẾỆỂỄ'
    r'ÌÍỊỈĨ'
    r'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ'
    r'ÙÚỤỦŨƯỪỨỰỬỮ'
    r'ỲÝỴỶỸĐ]'
)