from pyvi import ViTokenizer
import re
from collections import Counter
from exceptions.custom_exceptions import EmptyTextException
from config.settings import VIETNAMESE_STOP_WORDS

def analyze(text, top_n=5):
    if not text.strip():
        raise EmptyTextException("Văn bản đang trống, không thể tiến hành phân tích.")

    # Đếm ký tự (tính cả khoảng trắng)
    char_count = len(text)

    # Đếm câu (Dùng Regex tách theo dấu câu kết thúc câu)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)

    # ĐẾM CHÍNH XÁC TỔNG SỐ TỪ (Dựa trên văn bản gốc tách bằng khoảng trắng)
    raw_words = [w for w in text.split() if any(c.isalnum() for c in w)]
    word_count = len(raw_words)
    
    # PHÂN TÍCH TOP N TỪ (Dùng pyvi để giữ nguyên cấu trúc từ ghép)
    tokenized_text = ViTokenizer.tokenize(text)
    analyzer_words = [w for w in tokenized_text.split() if any(c.isalnum() for c in w)]
    
    # Lọc stop words và chuyển chữ thường để tìm Top N từ giá trị nhất
    filtered_words = [
        w.lower() for w in analyzer_words 
        if w.lower() not in VIETNAMESE_STOP_WORDS
    ]
    
    if filtered_words:
        word_freq = Counter(filtered_words)
        top_n_words = word_freq.most_common(top_n)
        most_frequent = top_n_words[0][0]
    else:
        top_n_words = []
        most_frequent = "--"

    return {
        "char_count": char_count,
        "sentence_count": sentence_count,
        "word_count": word_count, # Kết quả đếm từ chính xác theo khoảng trắng
        "most_frequent": most_frequent,
        "top_n_words": top_n_words # Danh sách giữ nguyên từ ghép tiếng Việt có dấu _
    }