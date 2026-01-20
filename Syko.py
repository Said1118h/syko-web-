import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# 1. إعداد الاتصال بـ Firebase (SYKO DATABASE)
if not firebase_admin._apps:
    # قمت بتجميع البيانات من صورك السابقة ووضعها هنا
    firebase_dict = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key_id": "365af5afd5e40bdd6de2771c87528626941eebfc",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz\nz7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+\nBpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O\nfJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps\ndtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty\nX8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw\nRTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+\nceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1\naSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE\nyCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN\n0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9\nOMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku\n431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m\nlpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR\nSV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1\nrWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH\nEHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx\nEmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t\n72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y\nGRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS\nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O\nZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ\nY30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW\n0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r\nG8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk\n2vkAD6dxTiUFdinjgn1+QA==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com",
        "client_id": "115802279140927891294",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-v2v4v%40syko-world.iam.gserviceaccount.com"
    }
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. واجهة SYKO التفاعلية
st.set_page_config(page_title="SYKO WORLD", layout="wide")
st.markdown("<h1 style='text-align:center; color:#ff00ff;'>🎬 SYKO PRIVATE ROOM</h1>", unsafe_allow_html=True)

col_vid, col_chat = st.columns([2, 1])

with col_vid:
    video_url = st.text_input("🔗 صق رابط الفيلم (YouTube):", "https://www.youtube.com/watch?v=QdBZY2fkU-0")
    st.video(video_url)

with col_chat:
    st.subheader("💬 الدردشة الحية")
    
    # جلب الرسائل من الداتابيز
    try:
        messages = db.collection(u'chat').order_by(u'timestamp', direction=firestore.Query.DESCENDING).limit(12).stream()
        for m in messages:
            d = m.to_dict()
            st.markdown(f"**{d.get('user', 'Guest')}**: {d.get('text', '')}")
    except:
        st.write("اكتب رسالة لبدء الدردشة!")

    with st.form("chat_form", clear_on_submit=True):
        name = st.text_input("اسمك:")
        msg = st.text_input("الرسالة:")
        if st.form_submit_button("إرسال 🔥"):
            if name and msg:
                db.collection(u'chat').add({
                    'user': name,
                    'text': msg,
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
                st.rerun()
