import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# --- 1. الربط التلقائي بقاعدة البيانات (بياناتك جاهزة) ---
if not firebase_admin._apps:
    syko_credentials = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key_id": "365af5afd5e40bdd6de2771c87528626941eebfc",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz\nz7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+\nBpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O\nfJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps\ndtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty\nX8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw\nRTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+\nceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1\naSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE\nyCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN\n0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9\nOMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku\n431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m\nlpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR\nSV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1\nrWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH\ EHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx\nEmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t\n72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y\nGRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS\ nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O\nZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ\nY30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW\n0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r\nG8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk\n2vkAD6dxTiUFdinjgn1+QA==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com",
        "client_id": "115802279140927891294",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-v2v4v%40syko-world.iam.gserviceaccount.com"
    }
    # تنظيف المفتاح ليعمل على السيرفر
    syko_credentials["private_key"] = syko_credentials["private_key"].replace("\\n", "\n")
    cred = credentials.Certificate(syko_credentials)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- 2. استعادة التصميم النيون الوردي (SYKO STYLE) ---
st.set_page_config(page_title="SYKO WORLD", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ff00ff; }
    .neon-title { text-align: center; color: #ff00ff; text-shadow: 0 0 20px #ff00ff; font-size: 50px; font-weight: bold; padding: 20px; }
    .chat-area { height: 400px; overflow-y: auto; background: rgba(0,0,0,0.8); border: 2px solid #00ff41; padding: 15px; border-radius: 15px; box-shadow: 0 0 10px #00ff41; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='neon-title'>🎬 SYKO PRIVATE ROOM</div>", unsafe_allow_html=True)

# --- 3. السينما والدردشة ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 🍿 شاشة العرض")
    video_url = st.text_input("صق رابط الفيديو هنا:", "https://www.youtube.com/watch?v=7pabvtEY-io")
    st.video(video_url)

with col_right:
    st.subheader("💬 الدردشة الحية")
    
    # عرض الرسائل من Firebase
    try:
        messages = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(15).stream()
        chat_html = "<div class='chat-area'>"
        for m in messages:
            d = m.to_dict()
            name = d.get('user', 'Unknown')
            text = d.get('text', '')
            chat_html += f"<p><b style='color:#00ff41'>{name}:</b> <span style='color:white'>{text}</span></p>"
        chat_html += "</div>"
        st.markdown(chat_html, unsafe_allow_html=True)
    except:
        st.info("اكتب رسالة لبدء الدردشة!")

    # نموذج إرسال الرسائل
    with st.form("chat_form", clear_on_submit=True):
        u_name = st.text_input("اسمك:")
        u_msg = st.text_input("الرسالة:")
        if st.form_submit_button("إرسال 🔥"):
            if u_name and u_msg:
                db.collection('chat').add({
                    'user': u_name, 
                    'text': u_msg, 
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
                st.rerun()
