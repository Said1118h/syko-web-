import streamlit as st
import requests
import instaloader
import time

# --- الإعدادات الأساسية ---
st.set_page_config(page_title="SYKO BLACK HOLE", layout="wide")
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
    
    /* زر المتابعة والجمع الفخم */
    .follow-collect-btn {
        background: linear-gradient(90deg, #00f2ff, #0044ff);
        color: white !important; font-weight: bold; border-radius: 15px;
        padding: 20px; text-decoration: none; display: block; text-align: center;
        box-shadow: 0 0 15px #00f2ff; transition: 0.3s;
    }
    .follow-collect-btn:hover { transform: scale(1.02); box-shadow: 0 0 25px #00f2ff; }
    
    .locked-market { filter: blur(10px); opacity: 0.2; pointer-events: none; }
    </style>
    """, unsafe_allow_html=True)

# دالة لجلب عدد المستخدمين من Firebase
def get_user_count():
    try:
        users = requests.get(f"{DB_URL}users.json").json()
        return len(users) if users else 0
    except: return 0

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- 1. واجهة تسجيل الدخول بالتحقق ---
if not st.session_state.logged_in:
    st.markdown("<span class='black-hole-s'>S</span>", unsafe_allow_html=True)
    u = st.text_input("Username").strip().lower()
    p = st.text_input("Password", type="password")
    
    if st.button("VERIFY & ENTER"):
        if u and p:
            # هنا نضع نظام التحقق الحقيقي instaloader
            st.session_state.username = u.replace("@","")
            st.session_state.logged_in = True
            # إنشاء سجل للمستخدم الجديد
            requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": 0})
            st.rerun()

# --- 2. واجهة العمل ---
else:
    user_count = get_user_count()
    target = 1000
    
    with st.sidebar:
        st.markdown(f"### 🛡️ @{st.session_state.username}")
        # جلب الكوينز الحالية
        user_data = requests.get(f"{DB_URL}users/{st.session_state.username}.json").json()
        current_coins = user_data.get('coins', 0) if user_data else 0
        st.markdown(f"<h1 style='color:#00f2ff;'>🪙 {current_coins}</h1>", unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    tab1, tab2 = st.tabs(["🎡 Gathering", "🛒 Market"])

    with tab1:
        st.markdown("<h2 style='text-align:center;'>GATHERING NODE</h2>", unsafe_allow_html=True)
        
        # اختيار مستخدم عشوائي ليتم متابعته (تأتي من active_tasks)
        target_user = "syko_official" # مثال
        
        st.markdown(f"### Next Task: Follow @{target_user}")
        
        # زر المتابعة والجمع في آن واحد
        # المبدأ: عند الضغط يفتح الرابط، وعند العودة يضغط المستخدم "تأكيد الجمع"
        st.markdown(f"""
            <a href="https://www.instagram.com/{target_user}/" target="_blank" class="follow-collect-btn">
                FOLLOW & PREPARE COINS 🚀
            </a>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ CONFIRM FOLLOW (GET 10 COINS)"):
            with st.spinner('Verifying Node...'):
                time.sleep(1) # محاكاة التحقق
                new_balance = current_coins + 10
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_balance})
                st.success(f"Success! +10 Coins Added to @{st.session_state.username}")
                time.sleep(0.5)
                st.rerun()

    with tab2:
        st.markdown(f"### 📊 Expansion Progress: {user_count}/{target}")
        st.progress(min(user_count/target, 1.0))
        
        st.markdown("<h2 style='text-align:center; color:red;'>MARKET IS LOCKED</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>SOON... REACH 1000 USERS TO UNLOCK</p>", unsafe_allow_html=True)
        
        st.markdown("<div class='locked-market'>", unsafe_allow_html=True)
        st.columns(2)[0].metric("100 Followers", "Soon")
        st.columns(2)[1].metric("500 Followers", "Soon")
        st.markdown("</div>", unsafe_allow_html=True)
