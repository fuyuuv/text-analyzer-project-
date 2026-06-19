# Text Analyzer (Phân Tích Văn Bản)

Ứng dụng Desktop hỗ trợ chuẩn hóa và phân tích thống kê cấu trúc văn bản tiếng Việt, được xây dựng dựa trên kiến trúc phân lớp.

## Tính năng chính

* **Chuẩn hóa văn bản (Processor):** * Chuyển đổi chữ hoa / chữ thường.
    * Loại bỏ dấu câu và ký tự đặc biệt (giữ nguyên bảng chữ cái tiếng Việt).
* **Phân tích ngôn ngữ (Analyzer):**
    * Đếm tổng số ký tự, số từ và số câu.
    * Sử dụng AI (`pyvi`) để tách từ ghép tiếng Việt chính xác theo ngữ nghĩa.
    * Trích xuất từ xuất hiện nhiều nhất.
    * Hiển thị danh sách Top N từ vựng có tần suất cao nhất trên bảng cuộn độc lập.
* **Quản lý File:** Hỗ trợ import dữ liệu trực tiếp từ file `.txt`.
* **Giao diện:** Dark Theme, thiết kế dạng Split View bằng `CustomTkinter`.

## Kiến trúc hệ thống

Dự án áp dụng mô hình phân tách trách nhiệm rõ ràng:
* `config/`: Chứa hằng số giao diện, bảng màu, pattern regex tĩnh.
* `core/`: Xử lý logic làm sạch chuỗi và thuật toán phân tích NLP, hoàn toàn độc lập với UI.
* `utils/`: Quản lý đọc/ghi file với cơ chế mapping dễ mở rộng đuôi file (`.txt`, `.csv`...).
* `ui/`: Tầng giao tiếp người dùng chia thành các components nhỏ gọn.

## Cài đặt và Khởi chạy

**1. Yêu cầu hệ thống:**
* Python 3.8+

**2. Khởi tạo môi trường và cài đặt thư viện:**
```bash
python -m venv venv
```
   Kích hoạt môi trường (Windows):

```DOS
venv\Scripts\activate
```
   Kích hoạt môi trường (macOS/Linux):

```bash
source venv/bin/activate
```
   Cài đặt dependencies:

```bash
pip install -r requirements.txt
```
**3. Chạy ứng dụng:

```bash
python main.py
```
