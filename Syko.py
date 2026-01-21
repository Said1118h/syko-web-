import streamlit as st
import requests
import hashlib
import time

# إعدادات SYKO - تجربة إنستقرام داخل الموقع
st.set_page_config(page_title="SYKO VIRTUAL INSTA", layout="wide")

# تصميم الواجهة لتكون "مظلمة" وفخمة
st.markdown("""
    <style>
    .main { background-color: #050505; }
    .insta-container {
        border: 2px solid #222;
        border-radius: 20px;
        overflow: hidden;
        background: #000;
        height: 600px;
        position: relative;
    }
    .insta-header {
        background: #111; padding: 10px; border-bottom: 1px solid #333;
        text-align: center; color: #00f2ff; font-weight: bold;
    }
    iframe { width: 100%; height: 100%; border: none; }
    .coins-badge {
        position: fixed; top: 20px; right: 20px;
        background: linear-gradient(90deg, #00f2ff, #0072ff);
        padding: 10px 20px; border-radius: 50px; color: black; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'task_index' not in st.session_state: st.session_state.task_index = 0

# --- الدخول إلى SYKO ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center; color:#00f2ff;'>SYKO LOGIN</h1>", unsafe_allow_html=True)
    u_in = st.text_input("User:").lower().strip()
    p_in = st.text_input("Pass:", type='password')
    if st.button("دخول"):
        res = requests.get(f"{DB_URL}users/{u_in}.json").json()
        if res and res.get('password') == hashlib.sha256(str.encode(p_in)).hexdigest():
            st.session_state.username, st.session_state.coins, st.session_state.logged_in = u_in, res.get('coins', 0), True
            st.rerun()

else:
    # عرض الكوينز بشكل عائم
    st.markdown(f'<div class="coins-badge">🪙 {st.session_state.coins}</div>', unsafe_allow_html=True)
    
    col_list, col_view = st.columns([1, 2])

    with col_list:
        st.markdown("### 📋 قائمة المهام")
        tasks = requests.get(f"{DB_URL}active_tasks.json").json()
        if tasks:
            task_list = list(tasks.items())
            current_tid, current_tdata = task_list[st.session_state.task_index]
            target = current_tdata['user']
            
            st.info(f"المهمة الحالية: متابعة @{target}")
            
            if st.button("✅ تأكيد العملية (+10 كوينز)"):
                new_c = st.session_state.coins + 10
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                st.session_state.coins = new_c
                st.session_state.task_index = (st.session_state.task_index + 1) % len(task_list)
                st.success("تم! جاري تحميل التالي...")
                st.rerun()
        else:
            st.write("لا يوجد حسابات حالياً.")

    with col_view:
        # هنا "نفتح الحساب" داخل الموقع
        if tasks:
            st.markdown(f'<div class="insta-header">عرض حساب: @{target}</div>', unsafe_allow_html=True)
            
            # نستخدم هذا الرابط لعرض الحساب بشكل مصغر (Widget)
            # هذا الرابط مخصص لعرض الحسابات داخل المواقع دون مغادرتها
            embed_url = f"https://www.instagram.com/{target}/embed/"
            
            st.markdown(f"""
                <div class="insta-container">
                    <iframe src="{embed_url}" scrolling="yes"></iframe>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="insta-container" style="display:flex; align-items:center; justify-content:center; color:#555;">انتظر إضافة حسابات جديدة</div>', unsafe_allow_html=True)

    # إضافة حساب جديد
    with st.sidebar:
        st.markdown("---")
        u_add = st.text_input("أضف يوزرك للظهور:")
        if st.button("بدء الحملة (100 كوينز)"):
            if st.session_state.coins >= 100:
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": st.session_state.coins - 100})
                requests.post(f"{DB_URL}active_tasks.json", json={"user": u_add.replace("@","")})
                st.rerun()
