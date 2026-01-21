import streamlit as st
import requests

# إعدادات الواجهة
st.set_page_config(page_title="SYKO MARKET", layout="centered")

# رابط قاعدة بياناتك
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("<h1 style='text-align: center; color: #0ff;'>SYKO FOLLOW MARKET</h1>", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- تسجيل الدخول ---
if not st.session_state.logged_in:
    u_input = st.text_input("أدخل يوزرك للدخول:", key="login")
    if st.button("دخول"):
        if u_input:
            u = u_input.lower().strip().replace("@", "")
            res = requests.get(f"{DB_URL}users/{u}.json")
            data = res.json()
            if data is None:
                requests.put(f"{DB_URL}users/{u}.json", json={"coins": 0})
                st.session_state.coins = 0
            else:
                st.session_state.coins = data.get("coins", 0)
            st.session_state.username = u
            st.session_state.logged_in = True
            st.rerun()
else:
    st.sidebar.markdown(f"### 🪙 رصيدك: {st.session_state.coins}")
    
    tab1, tab2 = st.tabs(["🛒 قائمة الحسابات المتاحة", "➕ أضف حسابك للقائمة"])

    # --- القسم 1: عرض كل الحسابات المطلوبة ---
    with tab1:
        st.subheader("إختر حساباً لمتابعته واربح 10 كوينز")
        
        # جلب كل الطلبات من قاعدة البيانات
        orders_res = requests.get(f"{DB_URL}active_tasks.json")
        tasks = orders_res.json()

        if tasks:
            for task_id, task_data in tasks.items():
                target = task_data['user']
                
                # تصميم كرت لكل حساب
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**حساب مطلوب متابعته:** @{target}")
                        st.markdown(f"[🔗 افتح الحساب في إنستقرام](https://www.instagram.com/{target})")
                    with col2:
                        if st.button(f"تأكيد ✔️", key=task_id):
                            # زيادة الكوينز
                            new_balance = st.session_state.coins + 10
                            requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_balance})
                            st.session_state.coins = new_balance
                            st.success(f"تمت إضافة 10 كوينز!")
                            st.rerun()
                    st.divider()
        else:
            st.info("القائمة فارغة حالياً. كن أول من يضيف حسابه!")

    # --- القسم 2: إضافة حساب جديد ---
    with tab2:
        st.subheader("أضف حسابك ليراه الجميع")
        target_to_add = st.text_input("أدخل اليوزر الذي تريد ظهوره في القائمة:")
        
        if st.button("إضافة الآن (100 كوينز)"):
            if target_to_add and st.session_state.coins >= 100:
                # خصم الكوينز
                new_balance = st.session_state.coins - 100
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_balance})
                st.session_state.coins = new_balance
                
                # إضافة الحساب لقائمة المهام لكي يظهر في Tab 1
                new_task = {"user": target_to_add.lower().strip().replace("@", "")}
                requests.post(f"{DB_URL}active_tasks.json", json=new_task)
                
                st.success("تم إضافة الحساب بنجاح ويظهر الآن للجميع!")
                st.balloons()
                st.rerun()
            else:
                st.error("تأكد من كتابة اليوزر أو شحن رصيدك!")

    if st.sidebar.button("خروج"):
        st.session_state.logged_in = False
        st.rerun()
