import re
from config.settings import ABBREVIATIONS_DICT

def to_lower_case(text):
    return text.lower()

def to_upper_case(text):
    return text.upper()

def to_title_case(text):
    return text.title()

def to_sentence_case(text):
    def capitalize_match(match):
        return match.group(1) + match.group(2).upper()
    return re.sub(r'(^|[\.\!\?]\s+)([^\W\d_])', capitalize_match, text)

def remove_extra_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def expand_abbreviations(text):
    """Thay thế các từ viết tắt thành từ hoàn chỉnh"""
    sorted_abbr = sorted(ABBREVIATIONS_DICT.keys(), key=len, reverse=True)
    
    for abbr in sorted_abbr:
        pattern = r'(?<!\w)' + re.escape(abbr) + r'(?!\w)'
        text = re.sub(pattern, ABBREVIATIONS_DICT[abbr], text, flags=re.IGNORECASE)
        
    return text

