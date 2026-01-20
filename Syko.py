import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# 1. إعداد الاتصال بـ Firebase
if not firebase_admin._apps:
    # تقسيم المفتاح لأسطر صغيرة لمنع خطأ السطر 110
    pk = (
        "-----BEGIN PRIVATE KEY-----\n"
        "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz\n"
        "z7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+\n"
        "BpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O\n"
        "fJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps\n"
        "dtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty\n"
        "X8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw\n"
        "RTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+\n"
        "ceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1\n"
        "aSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE\n"
        "yCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN\n"
        "0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9\n"
        "OMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku\n"
        "431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m\n"
        "lpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR\n"
        "SV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1\n"
        "rWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH\n"
        "EHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx\n"
        "EmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t\n"
        "72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y\n"
        "GRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS\n"
        "nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O\n"
        "ZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ\n"
        "Y30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW\n"
        "0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r\n"
        "G8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk\n"
        "2vkAD6dxTiUFdinjgn1+QA==\n"
        "-----END PRIVATE KEY-----\n"
    )
    
    config = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key": pk.replace("\\n", "\n"),
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com",
        "token_uri": "https://oauth2.googleapis.com/token"
    }
    cred = credentials.Certificate(config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. واجهة SYKO UNIVERSE
st.title("🌌 SYKO UNIVERSE")

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    st.info("مرحباً بك في عالم SYKO الخاص")
    if st.button("🚀 دخول البوابة"):
        st.session_state.page = "main"
        st.rerun()

elif st.session_state.page == "main":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🎬 السينما")
        url = st.text_input("رابط الفيديو:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(url)
    with col2:
        st.subheader("💬 الدردشة")
        # محاولة جلب الرسائل
        try:
            msgs = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).stream()
            for m in msgs:
                d = m.to_dict()
                st.markdown(f"**{d.get('user')}**: {d.get('text')}")
        except:
            st.write("بدء الدردشة...")
        
        with st.form("chat", clear_on_submit=True):
            u = st.text_input("الأسم")
            t = st.text_input("الرسالة")
            if st.form_submit_button("إرسال"):
                db.collection('chat').add({'user':u, 'text':t, 'timestamp':firestore.SERVER_TIMESTAMP})
                st.rerun()
