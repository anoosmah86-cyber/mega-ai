import streamlit as st

st.set_page_config(page_title="MEGA AI", page_icon="🚀")

st.title("🚀 MEGA AI")
st.write("موقع الذكاء الاصطناعي الخاص بـ أنس")

prompt = st.text_input("اسأل أي حاجة:")

if st.button("اسأل"):
    if prompt:
        st.success(f"سؤالك: {prompt} - MEGA AI شغال 100% 🔥")
    else:
        st.warning("اكتب سؤال الاول!")
    
