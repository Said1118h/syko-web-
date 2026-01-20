import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# --- 1. الربط الأكيد بـ Firebase (حل مشكلة ValueError نهائياً) ---
if not firebase_admin._apps:
    # البيانات مأخوذة من صورك مع معالجة المفتاح السري
    syko_credentials = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key_id": "365af5afd5e40bdd6de2771c87528626941eebfc",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz\nz7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+\nBpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O\nfJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps\ndtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty\nX8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw\nRTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+\nceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1\naSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE\nyCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN\n0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9\nOMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku\n431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m\nlpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR\nSV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1\ nrWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH\ EHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx\nEmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t\n72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y\ GRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS\ nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O\nZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ\nY30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW\n0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r\nG8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk\n2vkAD6dxTiUFdinjgn1+QA==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com"
    }
    # السطر السحري الذي سيصلح الخطأ الأحمر فوراً
    syko_credentials["private_key"] = syko_credentials["private_key"].replace("\\n", "\n")
    cred = credentials.Certificate(syko_credentials)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- 2. إدارة الحالة (Navigation) ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- 3. تصميم SYKO العالمي (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #000; color: #ff00ff; font-family: 'Orbitron', sans-serif; }
    
    .syko-title { text-align: center; font-size: 70px; font-weight: 900; 
                  text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff; margin-bottom: 0px; }
    
    .black-hole {
        width: 200px; height: 200px;
        background: radial-gradient(circle, #000 20%, #ff00ff 50%, #00ffff 100%);
        border-radius: 50%; margin: 40px auto;
        box-shadow: 0 0 50px #ff00ff, 0 0 100px #00ffff;
        animation: spin 4s linear infinite, pulse 2s ease-in-out infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
</style>
""", unsafe_allow_html=True)

# --- 4. صفحة الترحيب (الثقب الأسود) ---
if st.session_state.page == "welcome":
    st.markdown("<div class='syko-title'>SYKO WORLD</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00ffff; letter-spacing:3px;'>UNIVERSAL ENTRY</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='black-hole'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 ENTER THE VOID", use_container_width=True):
            # تشغيل صوت الثقب الأسود (Warp Sound)
            st.components.v1.html("""
                <audio autoplay>
                    <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mp3">
                </audio>
            """, height=0)
            
            with st.spinner("سحبك إلى بُعد SYKO..."):
                time.sleep(2.5)
                st.session_state.page = "main"
                st.rerun()

# --- 5. صفحة السينما والشات ---
elif st.session_state.page == "main":
    st.markdown("<h2 style='text-align:center; color:#ff00ff; text-shadow: 0 0 10px #ff00ff;'>🎬 SYKO PRIVATE ROOM</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        v_url = st.text_input("🔗 رابط الفيديو:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(v_url)
        
    with c2:
        st.markdown("### 💬 SYKO CHAT")
        try:
            messages = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).stream()
            chat_box = "<div style='height:350px; overflow-y:auto; border:1px solid #00ffff; padding:10px; border-radius:10px; background:rgba(0,0,0,0.9);'>"
            for m in messages:
                d = m.to_dict()
                chat_box += f"<p><b style='color:#00ff41'>{d.get('user')}:</b> <span style='color:white'>{d.get('text')}</span></p>"
            chat_box += "</div>"
            st.markdown(chat_box, unsafe_allow_html=True)
        except:
            st.info("أرسل رسالة لتبدأ الدردشة!")

        with st.form("syko_chat", clear_on_submit=True):
            u = st.text_input("الاسم:")
            t = st.text_input("الرسالة:")
            if st.form_submit_button("إرسال 🔥"):
                if u and t:
                    db.collection('chat').add({'user':u, 'text':t, 'timestamp':firestore.SERVER_TIMESTAMP})
                    st.rerun()

    if st.button("⬅ العودة للمجرة"):
        st.session_state.page = "welcome"
        st.rerun()
