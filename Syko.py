import streamlit as st
import requests
import instaloader
import time

# --- إعدادات الهوية البصرية لـ SYKO ---
st.set_page_config(page_title="SYKO SAFE SYSTEM", layout="wide")
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .black-hole-s {
        font-family: 'Arial Black', sans-serif; font-size: 80px;
        background: radial-gradient(circle, #fff, #111, #000);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px #00f2ff; animation: pulse 2s infinite;
        text-align: center; display: block;
    }
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
    
    /* تنبيه الأمان */
    .safety-banner {
        background: rgba(255, 165, 0, 0.1);
        border: 1px solid orange;
        color: orange;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 14px;
        margin-bottom: 20px;
    }
    
    .follow-btn {
        background: linear-gradient(90deg, #00f2ff, #0044ff);
        color: white !important; font-weight: bold; border-radius: 10px;
        padding: 15px; text-decoration: none; display: block; text-align: center;
        box-shadow: 0 0 10px #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# دالة التحقق
def check_insta(u, p):
    L = instaloader.Instaloader()
    try:
        L.login(u, p)
        return True
    except: return False

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- 1. واجهة الدخول مع نصيحة الأمان ---
if not st.session_state.logged_in:
    st.markdown("<span class='black-hole-s'>S</span>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:white;'>SYKO LOGIN</h2>", unsafe_allow_html=True)
    
    # نصيحة الأمان المضافة لحمايتك
    st.markdown("""
        <div class='safety-banner'>
            ⚠️ <b>تنبيه SYKO للأمان:</b><br>
            للحفاظ على حسابك الأساسي من البند، ننصحك دائماً باستخدام <b>حساب وهمي</b> للجمع، ثم إرسال المتابعين لحسابك الأصلي.
        </div>
    """, unsafe_allow_html=True)
    
    u = st.text_input("Instagram Username").strip().lower()
    p = st.text_input("Instagram Password", type="password")
    
    if st.button("SECURE LOGIN 🔒"):
        if u and p:
            with st.spinner('Verifying...'):
                if check_insta(u, p):
                    st.session_state.username = u.replace("@","")
                    st.session_state.logged_in = True
                    requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": 0})
                    st.rerun()
                else: st.error("بيانات الحساب غير صحيحة")

# --- 2. واجهة العمل ---
else:
    # جلب عدد المستخدمين للعداد
    users = requests.get(f"{DB_URL}users.json").json()
    count = len(users) if users else 0
    
    with st.sidebar:
        st.markdown(f"### 🛡️ @{st.session_state.username}")
        user_data = requests.get(f"{DB_URL}users/{st.session_state.username}.json").json()
        current_coins = user_data.get('coins', 0) if user_data else 0
        st.markdown(f"<h1 style='color:#00f2ff;'>🪙 {current_coins}</h1>", unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown(f"### 📊 Expansion Progress: {count}/1000 Users")
    st.progress(min(count/1000, 1.0))

    tab1, tab2 = st.tabs(["🎡 Gathering", "🛒 Market (SOON)"])

    with tab1:
        st.info("Follow the target below to earn 10 Coins")
        target_user = "syko_official" # يوزر عشوائي من الداتابيس مستقبلاً
        
        st.markdown(f"""
            <a href="https://www.instagram.com/{target_user}/" target="_blank" class='follow-btn'>
                FOLLOW @{target_user}
            </a>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ CONFIRM & COLLECT"):
            # حماية إضافية: تأخير بسيط لمنع البوتات
            with st.spinner('Checking...'):
                time.sleep(1.5) 
                new_balance = current_coins + 10
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_balance})
                st.success("Success! +10 Coins Added.")
                time.sleep(0.5)
                st.rerun()

    with tab2:
        st.markdown("<h2 style='text-align:center; color:red;'>LOCKED UNTIL 1000 USERS</h2>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/800x400/000000/FF0000?text=SOON+BY+SYKO", use_container_width=True)
