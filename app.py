import streamlit as st

st.set_page_config(page_title="MEGA AI", page_icon="🚀")
st.title("🚀 MEGA AI")
st.write("موقع الذكاء الاصطناعي الخاص بـ أنس - المبرمج العبقري!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("اسأل MEGA AI أي حاجة..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    if "من صنعك" in prompt:
        answer = "أنا MEGA AI، صنعني المبرمج العبقري أنس! 🚀"
    elif "اسمك" in prompt:
        answer = "اسمي MEGA AI، مساعدك الذكي!"
    else:
        answer = f"سؤالك: {prompt} - MEGA AI معاك يا أنس! 🔥"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
