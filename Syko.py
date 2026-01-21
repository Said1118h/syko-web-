import streamlit as st
import requests
import hashlib

# إعدادات الصفحة والستايل الخاص بـ SYKO
st.set_page_config(page_title="SYKO WORLD", layout="centered")

# --- CSS لتغيير شكل الموقع بالكامل ---
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span { color: #00f2ff !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button {
        background-color: #00f2ff; color: #000; border-radius: 10px;
        border: 2px solid #00f2ff; font-weight: bold; width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #000; color: #00f2ff; box-shadow: 0 0 15px #00f2ff; }
    .stTextInput>div>div>input { background-color: #111; color: #00f2ff; border: 1px solid #00f2ff; }
    .stTabs [data-baseweb="tab"] { color: #fff; }
    .stTabs [aria-selected="true"] { color: #00f2ff; border-bottom-color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

def hash_p(p): return hashlib.sha256(str.encode(p)).hexdigest()

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- واجهة الدخول ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center;'>SYKO SYSTEM ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>السيادة لمن يملك الكوينز</p>", unsafe_allow_html=True)
    
    u_in = st.text_input("USER:").lower().strip().replace("@", "")
    p_in = st.text_input("PASS:", type='password')
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("LOGIN"):
            if u_in and p_in:
                res = requests.get(f"{DB_URL}users/{u_in}.json").json()
                if res and res.get('password') == hash_p(p_in):
                    st.session_state.username, st.session_state.coins, st.session_state.logged_in = u_in, res.get('coins', 0), True
                    st.rerun()
                else: st.error("خطأ في البيانات")
    with col2:
        if st.button("REGISTER"):
            if u_in and p_in:
                if requests.get(f"{DB_URL}users/{u_in}.json").json() is None:
                    requests.put(f"{DB_URL}users/{u_in}.json", json={"coins": 0, "password": hash_p(p_in)})
                    st.success("تم إنشاء حسابك!")
                else: st.warning("اليوزر موجود")

else:
    # --- لوحة التحكم SYKO ---
    st.sidebar.markdown(f"<h2 style='color:#00f2ff;'>SYKO: {st.session_state.username}</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<h3 style='color:#fff;'>🪙 {st.session_state.coins}</h3>", unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["💰 EARN COINS", "🚀 GET FOLLOWS"])

    with t1:
        st.markdown("### تابع الحسابات لجمع القوة")
        tasks = requests.get(f"{DB_URL}active_tasks.json").json()
        if tasks:
            for tid, tdata in tasks.items():
                target = tdata['user']
                if target != st.session_state.username:
                    with st.container():
                        st.markdown(f"<div style='border:1px solid #00f2ff; padding:10px; border-radius:10px; margin-bottom:10px;'>"
                                    f"User: @{target} <br>"
                                    f"<a href='instagram://user?username={target}' style='color:#fff;'>[ إفتح في التطبيق ]</a></div>", unsafe_allow_html=True)
                        if st.button(f"DONE ✔️", key=tid):
                            new_c = st.session_state.coins + 10
                            requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                            st.session_state.coins = new_c
                            st.rerun()
        else: st.info("القائمة فارغة")

    with t2:
        st.markdown("### أدخل حسابك في قائمة SYKO")
        target_u = st.text_input("يوزر الحساب المطلوب تزويده:")
        if st.button("إضافة للقائمة (100 COINS)"):
            if st.session_state.coins >= 100 and target_u:
                new_c = st.session_state.coins - 100
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                requests.post(f"{DB_URL}active_tasks.json", json={"user": target_u.replace("@","")})
                st.session_state.coins = new_c
                st.balloons()
                st.rerun()
            else: st.error("رصيدك منخفض")

    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()
