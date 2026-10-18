import streamlit as stimport streamlit as st

st.set_page_config(page_title="MEGA AI", page_icon="🚀")
st.title("🚀 MEGA AI")
st.write("موقع الذكاء الاصطناعي الخاص بـ أنس - المبرمج العبقري!")

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# اعرض الرسايل القديمة
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# مكان الكتابة الجديد
if prompt := st.chat_input("اسأل MEGA AI أي حاجة..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # رد ذكي
    if "من صنعك" in prompt or "مين عملك" in prompt:
        answer = "أنا MEGA AI، صنعني المبرمج العبقري أنس! 🚀"
    elif "السلام" in prompt or "ازيك" in prompt:
        answer = "وعليكم السلام يا أنس! عامل ايه؟ جاهز أساعدك! 😎"
    elif "اسمك" in prompt:
        answer = "اسمي MEGA AI، مساعدك الذكي الخاص!"
    else:
        answer = f"سؤال جامد! '{prompt}' - أنا MEGA AI هساعدك في أي حاجة تطلبها يا أنس! 🔥"
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)

st.set_page_config(page_title="MEGA AI", page_icon="🚀")

st.title("🚀 MEGA AI")
st.write("موقع الذكاء الاصطناعي الخاص بـ أنس")

prompt = st.text_input("اسأل أي حاجة:")
st.session_state.messages
if st.button("اسأل"):
    if prompt:
        st.success(f"سؤالك: {prompt} - MEGA AI شغال 100% 🔥")
    else:
        st.warning("اكتب سؤال الاول!")
    
