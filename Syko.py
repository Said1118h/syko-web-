import streamlit as st
import requests
import hashlib
import time
import random

# إعدادات SYKO - نظام الدوامة الاحترافي
st.set_page_config(page_title="SYKO WHEEL", layout="wide")

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

# تصميم SYKO المظلم (Neon Style)
st.markdown("""
    <style>
    .main { background-color: #000; }
    .stApp { background-color: #000; }
    .insta-card {
        border: 2px solid #00f2ff; border-radius: 20px;
        padding: 20px; background: #0a0a0a; text-align: center;
        box-shadow: 0 0 15px #00f2ff55;
    }
    iframe { border-radius: 15px; width: 100%; height: 500px; background: white; }
    .coins-text { font-size: 24px; color: #00f2ff; font-weight: bold; text-shadow: 0 0 10px #00f2ff; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; border-radius: 12px; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

if 'user_logged' not in st.session_state: st.session_state.user_logged = False

# --- 1. واجهة الربط المباشر (مثل Top Follow) ---
if not st.session_state.user_logged:
    st.markdown("<h1 style='text-align:center; color:#00f2ff;'>SYKO SYSTEM ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>سجل دخولك في إنستقرام ليتم تفعيل حسابك في الدوامة تلقائياً</p>", unsafe_allow_html=True)
    
    col_log, col_info = st.columns([1.5, 1])
    
    with col_log:
        # هنا يفتح إنستقرام مباشرة للربط
        st.markdown('<iframe src="https://www.instagram.com/accounts/login/"></iframe>', unsafe_allow_html=True)
    
    with col_info:
        st.markdown("<br><br>", unsafe_allow_html=True)
        u_name = st.text_input("أدخل يوزرك للتأكيد دخول الدوامة:")
        if st.button("تفعيل الحساب الآن ✅"):
            if u_name:
                u = u_name.lower().strip().replace("@","")
                # فحص الحساب في قاعدة البيانات أو إنشاؤه
                res = requests.get(f"{DB_URL}users/{u}.json").json()
                if res is None:
                    # مستخدم جديد (نعطيه 50 كوينز هدية)
                    requests.put(f"{DB_URL}users/{u}.json", json={"coins": 50})
                    st.session_state.coins = 50
                else:
                    st.session_state.coins = res.get("coins", 0)
                
                # إضافة الحساب للدوامة تلقائياً ليراه الآخرون
                requests.post(f"{DB_URL}active_tasks.json", json={"user": u})
                
                st.session_state.username = u
                st.session_state.user_logged = True
                st.success("تم الربط! جاري الدخول للدوامة...")
                time.sleep(1)
                st.rerun()

else:
    # --- 2. محرك الدوامة (حيث يتم التبادل التلقائي) ---
    st.markdown(f"""
        <div style='display:flex; justify-content:space-around; align-items:center; background:#111; padding:15px; border-radius:50px; border:1px solid #00f2ff;'>
            <div class='coins-text'>🪙 {st.session_state.coins}</div>
            <div style='color:#fff; font-size:18px;'>المستخدم النشط: <span style='color:#00f2ff;'>@{st.session_state.username}</span></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # جلب الحسابات المتاحة في الدوامة حالياً
    all_data = requests.get(f"{DB_URL}active_tasks.json").json()
    
    if all_data:
        # نظام الدوران: اختيار حساب عشوائي من الدوامة ليتابعه المستخدم
        task_id, task_info = random.choice(list(all_data.items()))
        target = task_info['user']

        col_frame, col_action = st.columns([2, 1])

        with col_frame:
            # عرض الحساب المطلوب متابعته
            st.markdown(f'<iframe src="https://www.instagram.com/{target}/"></iframe>', unsafe_allow_html=True)
        
        with col_action:
            st.markdown(f"""
                <div class="insta-card">
                    <h3 style="color:#fff;">فرصة ربح كوينز</h3>
                    <p style="color:#00f2ff; font-size:20px;">@{target}</p>
                    <p style="color:#888; font-size:12px;">تابع الحساب أعلاه ثم اضغط تأكيد للحصول على +10 كوينز وانتقال الدوامة للحساب التالي</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✅ تأكيد المتابعة (التالي)"):
                # تحديث الرصيد في Firebase والحفظ
                new_balance = st.session_state.coins + 10
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_balance})
                st.session_state.coins = new_balance
                st.success("تم الحفظ! جاري تدوير الحسابات...")
                time.sleep(0.5)
                st.rerun() # إعادة التشغيل تجلب حساباً عشوائياً جديداً

            if st.button("⏭️ تخطي هذا الحساب"):
                st.rerun()
    else:
        st.info("الدوامة فارغة، جاري انتظار مستخدمين جدد...")

    # خيار الخروج
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.user_logged = False
        st.rerun()
