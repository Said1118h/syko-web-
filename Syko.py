import streamlit as st
import time

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide")

# --- تصميم SYKO (بدون أخطاء) ---
st.markdown("""
<style>
    .stApp { background-color: #000; color: #ff00ff; }
    .syko-title { text-align: center; font-size: 60px; text-shadow: 0 0 20px #ff00ff; }
    .black-hole { 
        width: 150px; height: 150px; background: radial-gradient(circle, #000, #ff00ff);
        border-radius: 50%; margin: auto; animation: spin 3s linear infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
</style>
""", unsafe_allow_html=True)

# --- إدارة الصفحات ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- الصفحة الأولى: الترحيب ---
if st.session_state.page == "welcome":
    st.markdown("<div class='syko-title'>SYKO UNIVERSE</div>", unsafe_allow_html=True)
    st.markdown("<div class='black-hole'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 ENTER THE VOID", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()

# --- الصفحة الثانية: المحتوى ---
elif st.session_state.page == "main":
    st.markdown("<h2 style='text-align:center;'>🎬 SYKO PRIVATE ROOM</h2>", unsafe_allow_html=True)
    
    col_main, col_chat = st.columns([2, 1])
    
    with col_main:
        video_url = st.text_input("YouTube Link:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(video_url)
        
    with col_chat:
        st.subheader("💬 Chat")
        st.text_area("الرسائل", value="SYKO: Welcome to my world!\nGuest: Interface is clean!", height=300, disabled=True)
        
        with st.form("chat_input", clear_on_submit=True):
            msg = st.text_input("اكتب رسالتك هنا...")
            submit = st.form_submit_button("إرسال")
