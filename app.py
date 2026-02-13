import streamlit as st
import google.generativeai as genai

# إعداد الواجهة
st.set_page_config(page_title="مترجم العراق الذكي", page_icon="🇮🇶")
st.title("🇮🇶 مترجم اللهجة العراقية")

# أدخل مفتاحك هنا أو اجعله مدخلاً من المستخدم
api_key = st.sidebar.text_input("Google API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

    user_input = st.text_input("اكتب بالعراقي:")

    if st.button("ترجم"):
        if user_input:
            prompt = f"Translate the following Iraqi dialect to English: {user_input}"
            response = model.generate_content(prompt)
            st.success(response.text)
else:
    st.info("الرجاء إدخال الـ API Key في القائمة الجانبية")
