# Công cụ phân tích văn bản Tiếng Việt
## Giới thiệu
   Dự án xây dựng một ứng dụng phân tích văn bản tiếng Việt dựa trên Streamlit + VnCoreNLP cho phép người dùng nhập vào một đoạn văn bản và nhận kết quả phân tích ngôn ngữ tự nhiên (NLP) trực quan.
  

## Chức năng
- Tách từ (Tokenization): chia văn bản thành các đơn vị từ/cụm từ.
- Gán nhãn từ loại (POS Tagging): xác định vai trò ngữ pháp của từng từ.
- Nhận diện thực thể (NER): phát hiện các thực thể như Tên người (PER), Địa điểm (LOC), Tổ chức (ORG), Thời gian (TIME)…
- Giao diện web trực quan bằng Streamlit.

## Công nghệ
- Python
- Streamlit
– xây dựng giao diện web
- Dự án sử dụng VnCoreNLP làm công cụ chính để tách từ, gán nhãn từ loại và nhận diện thực thể tiếng Việt.
- 
## Cách chạy
```bash
pip install -r requirements.txt
streamlit run app.py

 Sau đó mở http://localhost:8501
## 🖼️ Giao diện minh họa
![Demo giao diện](images/demo.png)
