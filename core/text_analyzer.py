from pyvi import ViTokenizer
import re
from collections import Counter
from exceptions.custom_exceptions import EmptyTextException

def analyze(text, top_n=5):
    if not text.strip():
        raise EmptyTextException("Văn bản đang trống, không thể tiến hành phân tích.")

    # 1. Đếm ký tự
    char_count = len(text)

    # 2. Đếm câu (Dùng Regex tách theo dấu câu thay vì dùng AI)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)

    # 3. Tách từ tiếng Việt bằng pyvi (nối từ ghép bằng dấu _)
    tokenized_text = ViTokenizer.tokenize(text)
    words = tokenized_text.split()
    word_count = len(words)

    # 4. Tìm Top N từ xuất hiện nhiều nhất
    if word_count > 0:
        word_freq = Counter(words)
        top_n_words = word_freq.most_common(top_n)
        most_frequent = top_n_words[0][0]
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