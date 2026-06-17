import re
from config.settings import VIET_CHAR_PATTERN

def to_lower_case(text):
    """Chuyển toàn bộ chuỗi thành chữ thường"""
    return text.lower()

def to_upper_case(text):
    """Chuyển toàn bộ chuỗi thành CHỮ HOA"""
    return text.upper()

def remove_special_characters(text):
    """
    Sử dụng Regex kết hợp pattern đã cấu hình trong settings để 
    tìm và thay thế các ký tự không hợp lệ bằng chuỗi rỗng.
    """
    return re.sub(VIET_CHAR_PATTERN, '', text)