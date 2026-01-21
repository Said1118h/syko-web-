import streamlit as st
import requests
import hashlib

# إعدادات SYKO STYLE
st.set_page_config(page_title="SYKO TOP FOLLOW", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #000; }
    h1, h2, h3, p { color: #00f2ff !important; text-align: center; }
    .stButton>button { background-color: #00f2ff; color: #000; font-weight: bold; border-radius: 20px; }
    .stTextInput>div>div>input { background-color: #111; color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

def hash_p(p): return hashlib.sha256(str.encode(p)).hexdigest()

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- نظام الدخول ---
if not st.session_state.logged_in:
    st.markdown("<h1>SYKO LOGIN ⚡</h1>", unsafe_allow_html=True)
    u_in = st.text_input("Username:").lower().strip()
    p_in = st.text_input("Password:", type='password')
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("LOGIN"):
            res = requests.get(f"{DB_URL}users/{u_in}.json").json()
            if res and res.get('password') == hash_p(p_in):
                st.session_state.username, st.session_state.coins, st.session_state.logged_in = u_in, res.get('coins', 0), True
                st.rerun()
            else: st.error("Error")
    with c2:
        if st.button("SIGN UP"):
            if u_in and p_in:
                requests.put(f"{DB_URL}users/{u_in}.json", json={"coins": 0, "password": hash_p(p_in)})
                st.success("Created!")

else:
    # --- نظام TOP FOLLOW (التبادل والطلبات) ---
    st.sidebar.title(f"🪙 {st.session_state.coins}")
    
    t1, t2 = st.tabs(["💰 EARN", "🚀 ORDERS"])

    with t1:
        st.subheader("جمع الكوينز")
        tasks = requests.get(f"{DB_URL}active_tasks.json").json()
        if tasks:
            for tid, tdata in tasks.items():
                target = tdata['user']
                req = tdata.get('required', 10)
                done = tdata.get('done', 0)
                
                if target != st.session_state.username and done < req:
                    with st.container():
                        st.write(f"تابع @{target} ({done}/{req})")
                        st.markdown(f"[إفتح إنستقرام](instagram://user?username={target})")
                        if st.button(f"تأكيد المتابعة", key=tid):
                            # تحديث حساب المستخدم (زيادة)
                            new_c = st.session_state.coins + 10
                            requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                            # تحديث المهمة (زيادة المتابعات المستلمة)
                            requests.patch(f"{DB_URL}active_tasks/{tid}.json", json={"done": done + 1})
                            st.session_state.coins = new_c
                            st.rerun()
        else: st.write("لا يوجد طلبات")

    with t2:
        st.subheader("اطلب متابعين (مثل Top Follow)")
        target_u = st.text_input("الحساب المستهدف:")
        count = st.number_input("كم متابع تريد؟", min_value=10, step=10)
        cost = count * 10 # كل متابع بـ 10 كوينز
        
        st.write(f"التكلفة: {cost} كوينز")
        
        if st.button("تأكيد الطلب 🚀"):
            if st.session_state.coins >= cost and target_u:
                # خصم الكوينز
                new_c = st.session_state.coins - cost
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                st.session_state.coins = new_c
                # إضافة المهمة بنظام العداد
                requests.post(f"{DB_URL}active_tasks.json", json={
                    "user": target_u.replace("@",""),
                    "required": count,
                    "done": 0
                })
                st.success("تم بدء الحملة!")
                st.rerun()
            else: st.error("الرصيد غير كافٍ")
