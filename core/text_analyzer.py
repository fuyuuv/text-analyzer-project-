from pyvi import ViTokenizer
import re
from collections import Counter
from exceptions.custom_exceptions import EmptyTextException

def analyze(text, top_n=5):
    if not text.strip():
        raise EmptyTextException("Văn bản đang trống, không thể tiến hành phân tích.")

    # Đếm ký tự
    char_count = len("".join(text.split()))

    # Đếm câu (Dùng Regex tách theo dấu câu)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)

    # Tách từ tiếng Việt bằng pyvi (nối từ ghép bằng dấu _)
    tokenized_text = ViTokenizer.tokenize(text)
    words = [w for w in tokenized_text.split() if any(c.isalnum() for c in w)]
    word_count = len(words)

    # Tìm Top N từ xuất hiện nhiều nhất
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