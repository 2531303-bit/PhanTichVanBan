# PhanTichVanBan
🇻🇳 Công cụ phân tích văn bản Tiếng Việt
📌 Giới thiệu

Dự án xây dựng một ứng dụng phân tích văn bản tiếng Việt dựa trên Streamlit + VnCoreNLP/spaCy, cho phép người dùng nhập vào một đoạn văn bản và nhận kết quả phân tích ngôn ngữ tự nhiên (NLP) trực quan.

🚀 Chức năng chính

Tách từ (Tokenization): chia văn bản thành các đơn vị từ/cụm từ.

Gán nhãn từ loại (POS Tagging): xác định vai trò ngữ pháp của từng từ.

Nhận diện thực thể (NER): phát hiện các thực thể như Tên người (PER), Địa điểm (LOC), Tổ chức (ORG), Thời gian (TIME)…

Giao diện web trực quan bằng Streamlit.

🛠️ Công nghệ sử dụng

Python

Streamlit
 – xây dựng giao diện web

VnCoreNLP
 hoặc spaCy
 – xử lý ngôn ngữ tự nhiên

Tuỳ chọn: Fine-tuning mô hình NER (PhoBERT, spaCy) để bổ sung nhãn thực thể TIME/DATE
