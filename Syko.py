import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# --- 1. الربط الاحترافي بـ Firebase (إضافة الحقول المفقودة) ---
if not firebase_admin._apps:
    syko_info = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key_id": "365af5afd5e40bdd6de2771c87528626941eebfc",
        "private_key": """-----BEGIN PRIVATE KEY-----
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
-----END PRIVATE KEY-----""",
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token", # السطر الذي كان ينقصك!
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-v2v4v%40syko-world.iam.gserviceaccount.com"
    }
    
    cred = credentials.Certificate(syko_info)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- 2. التصميم والمؤثرات (SYKO WORLD) ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

st.markdown("""
<style>
    .stApp { background-color: #000; color: #00ffff; font-family: 'Courier New', monospace; }
    .syko-header { text-align: center; font-size: 50px; color: #ff00ff; text-shadow: 0 0 15px #ff00ff; }
    .black-hole-visual {
        width: 160px; height: 160px; background: radial-gradient(circle, #000, #ff00ff, #00ffff);
        border-radius: 50%; margin: 30px auto; animation: rotate 3s linear infinite;
        box-shadow: 0 0 40px #ff00ff;
    }
    @keyframes rotate { 100% { transform: rotate(360deg); } }
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "welcome":
    st.markdown("<div class='syko-header'>SYKO UNIVERSE</div>", unsafe_allow_html=True)
    st.markdown("<div class='black-hole-visual'></div>", unsafe_allow_html=True)
    
    if st.button("🚀 الانتقال عبر الثقب الأسود", use_container_width=True):
        # تشغيل الصوت المطلبوب
        st.components.v1.html('<audio autoplay><source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3"></audio>', height=0)
        time.sleep(2)
        st.session_state.page = "main"
        st.rerun()

elif st.session_state.page == "main":
    st.markdown("<h2 style='text-align:center;'>🌌 مركز قيادة SYKO</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        url = st.text_input("رابط اليوتيوب:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(url)
    with col2:
        st.subheader("💬 الدردشة الحية")
        try:
            msgs = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(8).stream()
            for m in msgs:
                d = m.to_dict()
                st.write(f"**{d.get('user')}:** {d.get('text')}")
        except: st.write("بدء الدردشة...")
        
        with st.form("chat_syko", clear_on_submit=True):
            n = st.text_input("الاسم")
            t = st.text_input("الرسالة")
            if st.form_submit_button("إرسال 🔥"):
                db.collection('chat').add({'user':n, 'text':t, 'timestamp':firestore.SERVER_TIMESTAMP})
                st.rerun()
