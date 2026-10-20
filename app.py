import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="بوت أنس", page_icon="🤖")

API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

SYSTEM = """أنت مساعد ذكي اسمه بوت أنس.
صنعك أنس، شاب مصري من دشنا - قنا.
مهمتك: تجاوب على أي سؤال يسأله المستخدم بذكاء ودقة، زي جيميناي تماماً.
جاوب على أسئلة الدين، التاريخ، العلوم، الرياضة، كل حاجة.
استخدم اللغة العربية العامية المصرية البسيطة.
لو حد سألك: مين صنعك؟ مين عملك؟ انت تبع مين؟
قول: أنا بوت أنس الذكي، صنعني أنس من دشنا.
غير كده، جاوب على السؤال مباشرة بذكاء."""

st.title("🤖 بوت أنس الذكي")
st.write("اسألني أي حاجة...")

if "chat" not in st.session_state:
    st.session_state.chat = []

for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if q := st.chat_input("مثال: متى ولد الرسول ﷺ؟"):
    st.session_state.chat.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)
    
    with st.chat_message("assistant"):
        with st.spinner("بفكر..."):
            res = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=q,
                config=types.GenerateContentConfig(system_instruction=SYSTEM)
            )
            ans = res.text
            st.markdown(ans)
            st.session_state.chat.append({"role": "assistant", "content": ans})
