import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# --- الربط عبر الـ Secrets (أكثر طريقة مضمونة في العالم) ---
if not firebase_admin._apps:
    fb_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(fb_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- تصميم SYKO المتطور ---
st.markdown("<h1 style='text-align:center; color:#ff00ff;'>🌌 SYKO UNIVERSE</h1>", unsafe_allow_html=True)

if "page" not in st.session_state: st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    st.markdown("<div style='width:150px; height:150px; background:radial-gradient(circle, #000, #ff00ff); border-radius:50%; margin:auto; box-shadow:0 0 50px #ff00ff;'></div>", unsafe_allow_html=True)
    if st.button("🚀 سحب إلى الثقب الأسود", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

elif st.session_state.page == "main":
    st.write("### 🎬 فيديو SYKO المختار")
    st.video("https://www.youtube.com/watch?v=7pabvtEY-io")
    
    st.write("---")
    st.write("### 💬 دردشة SYKO")
    
    # فورم بسيط للإرسال
    with st.form("chat"):
        name = st.text_input("إسمك")
        msg = st.text_input("رسالتك")
        if st.form_submit_button("إرسال"):
            db.collection('chat').add({'user': name, 'text': msg, 'timestamp': firestore.SERVER_TIMESTAMP})
            st.rerun()
