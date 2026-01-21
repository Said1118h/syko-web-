import streamlit as st
import requests
import hashlib
import time

# إعدادات SYKO - نظام التحقق المتقدم
st.set_page_config(page_title="SYKO PRO SYSTEM", layout="wide")

# تصميم النيون الفخم الخاص بـ SYKO
st.markdown("""
    <style>
    .main { background-color: #000; color: #00f2ff; }
    .stApp { background-color: #000; }
    .insta-box { border: 2px solid #00f2ff; border-radius: 15px; width: 100%; height: 500px; background: #fff; }
    .status-card { background: #111; border: 1px solid #00f2ff; padding: 15px; border-radius: 10px; text-align: center; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; width: 100%; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

DB_URL = "https://syko-booster-default-rtdb.firebaseio.com/"

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- 1. واجهة تسجيل دخول إنستقرام (مثل Top Follow) ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;'>SYKO LOGIN GATE</h1>", unsafe_allow_html=True)
    st.info("قم بتسجيل الدخول في النافذة أدناه ثم اكتب يوزرك للتفعيل")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # نافذة تسجيل دخول إنستقرام الحقيقية
        st.markdown('<iframe src="https://www.instagram.com/accounts/login/" class="insta-box"></iframe>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        u_verify = st.text_input("Username:")
        p_verify = st.text_input("Password (للموقع):", type='password')
        
        if st.button("تفعيل الحساب والدخول"):
            if u_verify and p_verify:
                u = u_verify.lower().strip().replace("@","")
                # تشفير الباسورد لحفظها في Firebase
                hashed = hashlib.sha256(str.encode(p_verify)).hexdigest()
                
                # جلب البيانات أو إنشاء جديد
                res = requests.get(f"{DB_URL}users/{u}.json").json()
                if res is None:
                    requests.put(f"{DB_URL}users/{u}.json", json={"coins": 100, "password": hashed})
                    st.session_state.coins = 100
                else:
                    st.session_state.coins = res.get("coins", 0)
                
                st.session_state.username = u
                st.session_state.logged_in = True
                st.success("تم التوثيق!")
                st.rerun()

else:
    # --- 2. واجهة العمل والدوامة بعد التوثيق ---
    st.sidebar.markdown(f"<div class='status-card'>🪙 الرصيد: {st.session_state.coins}<br>👤 @{st.session_state.username}</div>", unsafe_allow_html=True)
    
    col_task, col_browser = st.columns([1, 2])
    
    with col_task:
        st.subheader("🎡 الدوامة النشطة")
        # جلب الحسابات من قاعدة البيانات
        tasks = requests.get(f"{DB_URL}active_tasks.json").json()
        
        if tasks:
            task_list = list(tasks.items())
            # نختار أول مهمة لم يقم بها المستخدم
            tid, tdata = task_list[0]
            target = tdata['user']
            
            st.markdown(f"<div style='background:#111; padding:15px; border-radius:10px; border-left:5px solid #00f2ff;'>المهمة: تابع @{target}</div>", unsafe_allow_html=True)
            
            if st.button("✅ لقد تابعت الحساب (تأكيد)"):
                # تحديث الكوينز في السيرفر
                new_coins = st.session_state.coins + 10
                requests.patch(f"{DB_URL}users/{st.session_state.username}.json", json={"coins": new_coins})
                st.session_state.coins = new_coins
                
                # إزالة المهمة أو الانتقال للتالي (هنا نجعلها دورية)
                st.success("تمت إضافة 10 كوينز بنجاح!")
                time.sleep(1)
                st.rerun()
        else:
            st.info("جاري البحث عن حسابات في الدوامة...")

    with col_browser:
        # فتح حساب الهدف داخل الموقع مباشرة
        if tasks:
            url = f"https://www.instagram.com/{target}/"
            st.markdown(f'<iframe src="{url}" class="insta-box"></iframe>', unsafe_allow_html=True)
        else:
            st.markdown('<iframe src="https://www.instagram.com/" class="insta-box"></iframe>', unsafe_allow_html=True)

    # زر إضافة الحساب للدوامة لزيادة المتابعين
    with st.sidebar:
        st.markdown("---")
        if st.button("🚀 اطلب 20,000 متابع (مسابقة)"):
            if st.session_state.coins >= 500:
                st.balloons()
                st.success("دخلت السحب الكوني!")
            else:
                st.error("تحتاج 500 كوينز للسحب")

    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()
