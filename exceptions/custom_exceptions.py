class InvalidFileException(Exception):
    """Ném ra khi định dạng file import/export không nằm trong danh sách hỗ trợ"""
    pass

class EmptyTextException(Exception):
    """Ném ra khi người dùng yêu cầu xử lý/phân tích nhưng ô nhập liệu không có dữ liệu"""
    pass