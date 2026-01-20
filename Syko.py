import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# --- 1. الربط الأكيد بـ Firebase (حل مشكلة PEM نهائياً) ---
if not firebase_admin._apps:
    # وضعنا المفتاح بين """ لضمان قراءته كسطور حقيقية
    private_key_clean = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz
z7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+
BpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O
fJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps
dtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty
X8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw
RTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+
ceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1
aSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE
yCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN
0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9
OMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku
431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m
lpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR
SV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1
rWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH
EHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx
EmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t
72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y
GRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS
nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O
ZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ
Y30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW
0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r
G8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk
2vkAD6dxTiUFdinjgn1+QA==
-----END PRIVATE KEY-----"""

    syko_info = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key": private_key_clean,
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com",
    }
    
    cred = credentials.Certificate(syko_info)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- 2. إدارة الصفحات والتنقل ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- 3. التصميم العالمي لـ SYKO ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    .syko-title { text-align: center; font-size: 70px; font-weight: 900; color: #ff00ff; 
                  text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff; margin-top: 50px; }
    .black-hole {
        width: 200px; height: 200px;
        background: radial-gradient(circle, #000 20%, #ff00ff 50%, #00ffff 100%);
        border-radius: 50%; margin: 40px auto;
        box-shadow: 0 0 50px #ff00ff, 0 0 100px #00ffff;
        animation: spin 4s linear infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
</style>
""", unsafe_allow_html=True)

# --- 4. صفحة الترحيب ---
if st.session_state.page == "welcome":
    st.markdown("<div class='syko-title'>SYKO WORLD</div>", unsafe_allow_html=True)
    st.markdown("<div class='black-hole'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 ENTER THE VOID", use_container_width=True):
            # تشغيل صوت الثقب الأسود
            st.components.v1.html('<audio autoplay><source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3"></audio>', height=0)
            with st.spinner("سحبك إلى بُعد SYKO..."):
                time.sleep(2)
                st.session_state.page = "main"
                st.rerun()

# --- 5. الصفحة الأساسية ---
elif st.session_state.page == "main":
    st.markdown("<h2 style='text-align:center; color:#ff00ff;'>🎬 SYKO PRIVATE ROOM</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        v = st.text_input("صق رابط الفيديو:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(v)
    with c2:
        st.subheader("💬 Chat")
        try:
            msgs = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).stream()
            for m in msgs:
                d = m.to_dict()
                st.write(f"**{d.get('user')}:** {d.get('text')}")
        except: st.write("لا توجد رسائل بعد.")
        with st.form("chat", clear_on_submit=True):
            u, t = st.text_input("الاسم"), st.text_input("الرسالة")
            if st.form_submit_button("إرسال"):
                db.collection('chat').add({'user':u, 'text':t, 'timestamp':firestore.SERVER_TIMESTAMP})
                st.rerun()
