from underthesea import word_tokenize, sent_tokenize
from collections import Counter
from exceptions.custom_exceptions import EmptyTextException

def analyze(text, top_n=5):
    """
    Thực hiện phân tích ngôn ngữ tiếng Việt.
    Nhận vào chuỗi văn bản và số lượng Top N từ cần lấy.
    Trả về một Dictionary chứa các số liệu đã thống kê.
    """
    if not text.strip():
        raise EmptyTextException("Văn bản đang trống, không thể tiến hành phân tích.")

    # 1. Tổng số ký tự (đếm toàn bộ độ dài chuỗi)
    char_count = len(text)

    # 2. Đếm số câu bằng AI của undertsea (giải quyết được lỗi viết tắt như TP.HCM)
    sentences = sent_tokenize(text)
    sentence_count = len(sentences)

    # 3. Tách từ tiếng Việt theo ngữ nghĩa (format="text" sẽ nối từ ghép bằng dấu _)
    words = word_tokenize(text, format="text").split()
    word_count = len(words)

    # 4. Tìm Top N từ xuất hiện nhiều nhất
    if word_count > 0:
        word_freq = Counter(words)
        top_n_words = word_freq.most_common(top_n) # Trả về list tuple: [('từ', số_lần)]
        most_frequent = top_n_words[0][0] # Lấy phần tử text của từ đứng đầu
    else:
        top_n_words = []
        most_frequent = "--"

    return {
        "char_count": char_count,
        "sentence_count": sentence_count,
        "word_count": word_count,
        "most_frequent": most_frequent,
        "top_n_words": top_n_words
    }