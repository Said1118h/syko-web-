import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide")

# --- تصميم النيون ---
st.markdown("""
<style>
    .stApp { background-color: #000; color: #ff00ff; }
    .video-frame { border: 2px solid #ff00ff; border-radius: 15px; box-shadow: 0 0 20px #ff00ff; }
    .chat-area { background-color: #111; border-radius: 10px; padding: 10px; height: 350px; overflow-y: auto; border: 1px solid #00ffff; }
</style>
""", unsafe_allow_html=True)

# --- نظام الشات (ذاكرة الجلسة) ---
if "syko_chat" not in st.session_state:
    st.session_state.syko_chat = []

# --- الواجهة ---
st.markdown("<h1 style='text-align:center; color:#ff00ff;'>🌌 SYKO UNIVERSE</h1>", unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📺 البث المباشر")
    st.markdown("<div class='video-frame'>", unsafe_allow_html=True)
    # الفيديو المختار مثبت هنا
    st.video("https://www.youtube.com/watch?v=7pabvtEY-io")
    st.markdown("</div>", unsafe_allow_html=True)
    st.caption("🔴 SYKO LIVE STREAM")

with col_right:
    st.subheader("💬 الدردشة")
    
    # عرض الرسائل داخل حاوية
    with st.container():
        st.markdown("<div class='chat-area'>", unsafe_allow_html=True)
        for m in st.session_state.syko_chat:
            st.write(f"**{m['name']}**: {m['text']}")
        st.markdown("</div>", unsafe_allow_html=True)

    # إدخال الرسالة
    with st.form("msg_form", clear_on_submit=True):
        name = st.text_input("الأسم", value="Guest")
        text = st.text_input("اكتب رسالتك...")
        if st.form_submit_button("إرسال 🔥"):
            if text:
                st.session_state.syko_chat.append({"name": name, "text": text})
                st.rerun()
