import streamlit as st
import requests
import time

# إعدادات الواجهة
st.set_page_config(page_title="SYKO 1K GOAL", layout="wide")
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .progress-text { color: #00f2ff; font-family: 'Courier New'; font-size: 20px; text-align: center; }
    .locked-feature {
        filter: blur(4px);
        pointer-events: none;
        opacity: 0.5;
    }
    .soon-overlay {
        position: absolute; color: #ff0000; font-weight: bold;
        transform: rotate(-20deg); border: 2px solid #ff0000;
        padding: 5px; z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. جلب عدد المستخدمين الحاليين
def get_user_count():
    users = requests.get(f"{DB_URL}users.json").json()
    if users:
        return len(users)
    return 0

user_count = get_user_count()
target = 1000
progress = min(user_count / target, 1.0)

# --- واجهة العداد (الهدف 1000) ---
st.markdown("<h1 style='text-align:center; color:white;'>SYKO EXPANSION PHASE</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='progress-text'>Global Users: {user_count} / {target}</p>", unsafe_allow_html=True)

# شريط التقدم النيوني
st.progress(progress)

if user_count < target:
    st.warning(f"⚠️ النظام يعمل بطاقة جزئية. سيتم فتح 'البوابة الكبرى' عند الوصول لـ 1000 مستخدم. متبقي {target - user_count} مستخدم.")

# --- توزيع الميزات (مفتوح vs مقفول) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎡 الدوامة")
    st.write("الحالة: **ACTIVE** ✅")
    if st.button("دخول للجمع"):
        # كود الجمع العادي
        pass

with col2:
    st.markdown("### 💎 رشق المتابعين")
    if user_count < target:
        st.markdown("<div class='soon-overlay'>SOON (Locked)</div>", unsafe_allow_html=True)
        st.markdown("<div class='locked-feature'>", unsafe_allow_html=True)
        st.button("اطلب متابعين (قريباً)", disabled=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        if st.button("افتح المتجر الآن!"):
            pass

with col3:
    st.markdown("### 🎁 كود الهدية")
    if user_count < target:
         st.markdown("<div class='soon-overlay'>SOON</div>", unsafe_allow_html=True)
         st.markdown("<div class='locked-feature'>", unsafe_allow_html=True)
         st.button("ادخل الكود (قريباً)", disabled=True)
         st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.button("استلم هديتك 🎁")

# سجلات "Soon" التلقائية في الأسفل
st.markdown("---")
st.markdown("### 📜 System Transmission")
st.code(f"""
[LOG]: User @{st.session_state.get('username', 'Guest')} connected.
[LOG]: Data Verification: Pending...
[LOG]: 1K Target Status: {(progress*100):.2f}%
[LOG]: Advanced Features: SOON
""", language="bash")
