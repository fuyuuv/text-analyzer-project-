import os
from exceptions.custom_exceptions import InvalidFileException

# --- HÀM XỬ LÝ ĐỌC/GHI LÕI ---
def _read_txt(file_path):
    """Mở và đọc nội dung file .txt với chuẩn mã hóa UTF-8"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def _write_txt(file_path, content):
    """Ghi nội dung ra file .txt"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- MAPPING ĐỊNH DẠNG FILE ---
FILE_HANDLERS = {
    '.txt': {
        'read': _read_txt,
        'write': _write_txt
    }
}

def read_file(file_path):
    """Kiểm tra đuôi file và gọi hàm đọc tương ứng từ FILE_HANDLERS"""
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in FILE_HANDLERS:
        raise InvalidFileException(f"Hệ thống chưa hỗ trợ đọc định dạng {ext}.")
    return FILE_HANDLERS[ext.lower()]['read'](file_path)

def save_file(file_path, content):
    """Kiểm tra đuôi file và gọi hàm ghi tương ứng từ FILE_HANDLERS"""
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in FILE_HANDLERS:
        raise InvalidFileException(f"Hệ thống chưa hỗ trợ xuất định dạng {ext}.")
    FILE_HANDLERS[ext.lower()]['write'](file_path, content)