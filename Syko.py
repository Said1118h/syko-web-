import streamlit as st
import requests
import random

# إعدادات واجهة المستخدم
st.set_page_config(page_title="SYKO EXCHANGE", layout="centered")

# رابط قاعدة بياناتك (من الصور التي أرسلتها)
DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

st.markdown("<h1 style='text-align: center; color: #0ff;'>SYKO EXCHANGE SYSTEM</h1>", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- تسجيل الدخول ---
if not st.session_state.logged_in:
    st.info("سجل دخولك بيوزر إنستقرام لتبدأ التبادل")
    u_input = st.text_input("اسم المستخدم (Username):", key="login_field")
    if st.button("دخول"):
        if len(u_input) > 2:
            u = u_input.lower().strip().replace("@", "")
            # جلب البيانات من Firebase
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
    # --- لوحة التحكم ---
    st.sidebar.title(f"👤 {st.session_state.username}")
    st.sidebar.subheader(f"🪙 رصيدك: {st.session_state.coins}")
    
    tab1, tab2 = st.tabs(["💰 جمع الكوينز", "📢 أضف حسابك"])

    # --- القسم 1: جمع الكوينز (متابعة الآخرين) ---
    with tab1:
        st.write("تابع المستخدمين أدناه لتربح 10 كوينز عن كل متابعة")
        
        # جلب قائمة الأشخاص الذين طلبوا متابعين
        orders_res = requests.get(f"{DB_URL}active_tasks.json")
        tasks = orders_res.json()

        if tasks:
            # فلترة القائمة لاستبعاد حساب المستخدم الحالي
            other_users = {k: v for k, v in tasks.items() if v['user'] != st.session_state.username}
            
            if other_users:
                task_id, task_data = random.choice(list(other_users.items()))
                target = task_data['user']
                
                st.warning(f"المهمة الحالية: متابعة @{target}")
                st.markdown(f"[🔗 اضغط هنا لفتح الحساب ومتابعته](https://www.instagram.com/{target})")
                
                if st.button("تأكيد المتابعة (+10 كوينز)"):
                    # زيادة رصيد المستخدم
                    new_coins = st.session_state.coins + 10
                    requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_coins})
                    st.session_state.coins = new_coins
                    st.success("تمت إضافة الكوينز بنجاح!")
                    st.rerun()
            else:
                st.write("لا يوجد مستخدمون حالياً في قائمة الانتظار. جرب لاحقاً!")
        else:
            st.write("قائمة المهام فارغة. كن أول من يضيف حسابه!")

    # --- القسم 2: إضافة الاسم للقائمة (صرف الكوينز) ---
    with tab2:
        st.subheader("اجعل الآخرين يتابعونك")
        st.write("تكلفة إضافة اسمك للقائمة هي 100 كوينز.")
        
        if st.button("إضافة اسمي للقائمة (خصم 100 كوينز)"):
            if st.session_state.coins >= 100:
                # خصم الكوينز
                new_coins = st.session_state.coins - 100
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_coins})
                st.session_state.coins = new_coins
                
                # إضافة الاسم لقائمة المهام لكي يراه المستخدمون الآخرون في Tab 1
                task_data = {"user": st.session_state.username}
                requests.post(f"{DB_URL}active_tasks.json", json=task_data)
                
                st.balloons()
                st.success("تم إدراج اسمك! سيقوم المستخدمون بمتابعتك الآن.")
                st.rerun()
            else:
                st.error("رصيدك لا يكفي! اذهب لجمع الكوينز أولاً.")
    
    if st.sidebar.button("تسجيل خروج"):
        st.session_state.logged_in = False
        st.rerun()
