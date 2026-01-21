import streamlit as st
import requests
import hashlib

# --- دالة لتشفير كلمة السر (لحمايتها في قاعدة البيانات) ---
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# إعدادات الواجهة
st.set_page_config(page_title="SYKO SECURE SYSTEM", layout="centered")
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("<h1 style='text-align: center; color: #0ff;'>SYKO SYSTEM 🔒</h1>", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- 1. واجهة تسجيل الدخول وإنشاء الحساب ---
if not st.session_state.logged_in:
    st.subheader("تسجيل الدخول / إنشاء حساب جديد")
    
    u_input = st.text_input("يوزر إنستقرام الخاص بك:", placeholder="مثال: s1x.9s").lower().strip().replace("@", "")
    p_input = st.text_input("كلمة سر الحساب (خاصة بالموقع):", type='password')
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("دخول 🔓"):
            if u_input and p_input:
                res = requests.get(f"{DB_URL}users/{u_input}.json")
                user_data = res.json()
                
                if user_data and user_data.get('password') == hash_password(p_input):
                    st.session_state.username = u_input
                    st.session_state.coins = user_data.get('coins', 0)
                    st.session_state.logged_in = True
                    st.success(f"أهلاً بك مجدداً يا {u_input}!")
                    st.rerun()
                else:
                    st.error("اليوزر أو كلمة السر غير صحيحة!")
            else:
                st.warning("يرجى ملء جميع الخانات.")

    with col2:
        if st.button("إنشاء حساب جديد ✨"):
            if u_input and p_input:
                res = requests.get(f"{DB_URL}users/{u_input}.json")
                if res.json() is None:
                    hashed_p = hash_password(p_input)
                    requests.put(f"{DB_URL}users/{u_input}.json", json={"coins": 0, "password": hashed_p})
                    st.success("تم إنشاء الحساب بنجاح! يمكنك الآن الضغط على 'دخول'.")
                else:
                    st.warning("هذا اليوزر مسجل مسبقاً، يرجى تسجيل الدخول.")
            else:
                st.warning("يرجى اختيار يوزر وكلمة سر.")

else:
    # --- 2. لوحة التحكم بعد الدخول الآمن ---
    st.sidebar.markdown(f"### 👤 الحساب: {st.session_state.username}")
    st.sidebar.markdown(f"### 🪙 الرصيد: {st.session_state.coins}")
    
    tab1, tab2 = st.tabs(["🛒 قائمة التبادل", "🚀 اطلب متابعين"])

    with tab1:
        st.subheader("تابع واربح الكوينز")
        # جلب المهام
        tasks_res = requests.get(f"{DB_URL}active_tasks.json")
        tasks = tasks_res.json()

        if tasks:
            for tid, tdata in tasks.items():
                target = tdata['user']
                if target != st.session_state.username:
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        st.write(f"تابع الحساب: **@{target}**")
                        st.markdown(f"[🔗 افتح إنستقرام](https://www.instagram.com/{target})")
                    with col_b:
                        if st.button("تأكيد ✔️", key=tid):
                            new_c = st.session_state.coins + 10
                            requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                            st.session_state.coins = new_c
                            st.success("+10")
                            st.rerun()
                    st.divider()
        else:
            st.info("لا توجد طلبات حالياً.")

    with tab2:
        st.subheader("أضف حسابك للقائمة")
        target_user = st.text_input("اليوزر المراد دعمه:")
        if st.button("إضافة (100 كوينز)"):
            if st.session_state.coins >= 100 and target_user:
                # خصم الكوينز
                new_c = st.session_state.coins - 100
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_c})
                st.session_state.coins = new_c
                # إضافة المهمة
                requests.post(f"{DB_URL}active_tasks.json", json={"user": target_user.replace("@","")})
                st.success("تمت الإضافة!")
                st.rerun()
            else:
                st.error("رصيدك غير كافٍ أو اليوزر فارغ.")

    if st.sidebar.button("تسجيل خروج"):
        st.session_state.logged_in = False
        st.rerun()
