# Dự Án Nhận Diện Khuôn Mặt

## Mô Tả

Dự án này sử dụng mô hình VGGNet để nhận diện khuôn mặt. Các bước chính bao gồm tạo thư mục với ảnh của từng người, chạy tệp `prepare.py` để chuẩn bị dữ liệu, và sau đó chạy tệp `main.py` để thực hiện nhận diện.

## Hướng Dẫn Sử Dụng

### 1. Cấu Trúc Thư Mục

- Tạo một thư mục chứa các ảnh của từng người.
- Đặt tên thư mục theo mã số sinh viên (MSV) của mỗi người.
- Ví dụ cấu trúc thư mục:

### 2. Chuẩn Bị Dữ Liệu

Chạy tệp `prepare.py` để chuẩn bị dữ liệu. Tệp này sẽ xử lý các ảnh và tạo ra các tệp cần thiết cho quá trình nhận diện.
python prepare.py
3. Chạy Ứng Dụng Chính
Sau khi dữ liệu đã được chuẩn bị, bạn có thể chạy tệp main.py để thực hiện nhận diện khuôn mặt.
python main.py
```bash
Chay file requiewment.txt de dowload cac thu vien can thiet
pip install -r requirements.txt


