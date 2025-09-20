import streamlit as st
from underthesea import word_tokenize, pos_tag, ner

st.title("Công cụ phân tích văn bản Tiếng Việt")

# Nhập văn bản
text_input = st.text_area("Nhập đoạn văn bản:", "Hà Nội là thủ đô của Việt Nam.")

if st.button("Phân tích"):
    if text_input.strip():
        # Tokenization
        st.subheader("🔹 Tách từ (Tokenization)")
        tokens = word_tokenize(text_input)
        st.write(tokens)

        # POS Tagging
        st.subheader("🔹 Gán nhãn từ loại (POS Tagging)")
        pos_tags = pos_tag(text_input)
        st.write(pos_tags)

        # Named Entity Recognition
        st.subheader("🔹 Nhận diện thực thể (NER)")
        entities = ner(text_input)
        st.write(entities)
    else:
        st.warning("⚠️ Vui lòng nhập văn bản để phân tích.")