import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time
import base64

# --- 1. إعدادات الصفحة والربط الذكي ---
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide", initial_sidebar_state="collapsed")

if not firebase_admin._apps:
    syko_credentials = {
        "type": "service_account",
        "project_id": "syko-world",
        "private_key_id": "365af5afd5e40bdd6de2771c87528626941eebfc",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmEKxgyUvBELCz\nz7CcWOvyVFyPnKGUFx+Ch0iZ0ycZG80JlPztq/RtTtnxzwohJojFl3mtu2clphh+\nBpGYNKg1mGn6xYxcjksd4KUGAz05ZOSdTx2ybFkifzd37TubWkmEexXqjKYJy22O\nfJ6Bs9sMOZX1uX2rdiOjkGYwADlBhV6+ku3kIoadKdCvvQX8gD5+mKLkbiQL+0ps\ndtJj9wHRxzDGW01djVb5vuhZ3u9GlIB6K999WEWLYm8njqrEKKRTMP+AskXwLkty\nX8GJlp9tqBDz7icpRgBOs9XqKxHSfiygWf9yBpNAoomuIhM19G8ffb+YGMQwV2Fw\nRTMfmYPJAgMBAAECggEAAsHf0QP57ukjFwVF68/IhHsJ8MowU7uAYWKl8PsGAKU+\nceSUW0mzQvVImSnG3dgYgva9FXhrJMPpeVGH60PeoWV6MrBYAvAiesE7dRedmJt1\naSRpOenWGnrdbd1njcXOnwJQeaMge8+mzd1U6H92IFQXMHld8KvDLasLFdJGMrtE\nyCZC7bogIFur+3kEvq2d1Oa1H3uTznjc27AKu4GDYdEbC5CDZJH29EoYpvJuGLlN\n0HUmeFSFf92wUHw1+z1I/7TkqVhQq19SVRyrhB1fCnFWlhweu0JqMsx65GT3UTn9\nOMPZYNheu39/1GLpj9Qe8bx5xOsgNWFcEMsJJoamAQKBgQDzzhD4JdAS1fewk9Ku\n431H4Trm8EPFjv133J7joa1xzfFFfjmy96Taw2C1H3nlIjE9D5iHiJ9cE6d5Lq9m\nlpnga28ubtVpr9A0zOvRwnMYE4Q3LdwYDc1NIWfqd4WvKSmald7Xa+rKRVuWm2pR\nSV1jgKdb8FESVkh+h0/XlSu9yQKBgQDxkqsHMp5i1dw6fS0m1me9GMwXqqiZALD1\nrWm2+625yegUe58xZWXV/VeGLOH9gM5fE0swQP3Kt9XYWfZSoUFjo1khGgS6IZkH\ EHbCo76sHrY8TSBGXRV/MLcEyeP9KxWMUoOxOp+mh+fnVhrzUXjScK1nC1D2aodx\nEmY2tGqWAQKBgA5RluuMBPlmOaLUO7Zrw+rZzoTLrZ9Hs5k7itVhpHcfmkDzld3t\n72+ts9tPWvBbHrswVEv5eSqGOPrEBCcpRyZICQKYHc6UNc00D9GE8w+B7ezzs45y\ GRGjmZ/Knz5XU4sxrCHIw8RXaHai8A6QGX0DjFC4/3ntOVq9BbJqn2QJAoGAMDAS\ nn7fwMkT4zk4EALhKL0VQCPSI9yRVKFy0NsUTjXkCK3vRcJgKbVpA6EnxtpDIGd0O\nZYzBU3vCU4r2gNsb4RVHhTvcb4ieLvOQzRi+wzTJI1Q7OO3+iMWd7H2dVfYPMVOQ\nY30PNbfsgZAChkDdOhUx8dknCFCNvfdunkD09gECgYAF1Btx8PeHCJYKQjLCugYW\n0sgBAIRldtxAOpRRdDn93y60JywGhQaYx2DJzSbAoMpg9s+mNAaYZ55CLoZ6u49r\nG8JJKS0JcqjKcL0EDk/T6YyrAnFKE7R9Z1T1vyazJTkFoRjJ6U7YY/exEbDyLkfk\n2vkAD6dxTiUFdinjgn1+QA==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-v2v4v@syko-world.iam.gserviceaccount.com"
    }
    syko_credentials["private_key"] = syko_credentials["private_key"].replace("\\n", "\n")
    cred = credentials.Certificate(syko_credentials)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- 2. وظيفة الصوت (Black Hole Sound) ---
def play_sound():
    # هذا رابط لصوت فضائي حقيقي (Thrumming/Deep Space)
    sound_url = "https://www.soundjay.com/buttons/beep-01a.mp3" # يمكنك تغيير الرابط لأي صوت .mp3
    html_string = f"""
        <audio autoplay>
        <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mp3">
        </audio>
    """
    st.markdown(html_string, unsafe_allow_html=True)

# --- 3. إدارة الحالة (Navigation) ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- 4. تصميم SYKO العالمي (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    
    .black-hole-container { display: flex; justify-content: center; align-items: center; height: 300px; }
    .black-hole {
        width: 180px; height: 180px;
        background: radial-gradient(circle, #000 20%, #ff00ff 60%, #00ffff 100%);
        border-radius: 50%;
        box-shadow: 0 0 50px #ff00ff, 0 0 100px #00ffff;
        animation: spin 3s linear infinite, pulse 2s ease-in-out infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

    .syko-title { text-align: center; font-size: 70px; font-weight: 900; color: #ff00ff; 
                  text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff; margin-bottom: 0px; }
</style>
""", unsafe_allow_html=True)

# --- 5. صفحة الترحيب ---
if st.session_state.page == "welcome":
    st.markdown("<div class='syko-title'>SYKO WORLD</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:#00ffff; letter-spacing:5px;'>ENTER THE BLACK HOLE</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='black-hole-container'><div class='black-hole'></div></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        if st.button("🚀 INHALE INTO VOID", use_container_width=True):
            play_sound() # تشغيل الصوت فوراً
            with st.spinner("SYKO is pulling you..."):
                time.sleep(2)
                st.session_state.page = "main"
                st.rerun()

# --- 6. الصفحة الأساسية (SYKO Room) ---
elif st.session_state.page == "main":
    st.markdown("<h2 style='text-align:center; color:#ff00ff; text-shadow: 0 0 10px #ff00ff;'>🎬 SYKO PRIVATE CINEMA</h2>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([2, 1])
    with col_left:
        video_url = st.text_input("صق رابط الفيديو:", "https://www.youtube.com/watch?v=7pabvtEY-io")
        st.video(video_url)
        
    with col_right:
        st.markdown(f"### 💬 SYKO CHAT")
        try:
            messages = db.collection('chat').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).stream()
            chat_html = "<div style='height:350px; overflow-y:auto; background:rgba(255,0,255,0.05); border:1px solid #00ffff; padding:10px; border-radius:10px;'>"
            for msg in messages:
                d = msg.to_dict()
                chat_html += f"<p><b style='color:#00ff41'>{d.get('user')}:</b> {d.get('text')}</p>"
            chat_html += "</div>"
            st.markdown(chat_html, unsafe_allow_html=True)
        except: st.info("Say Hi to SYKO!")

        with st.form("syko_form", clear_on_submit=True):
            u = st.text_input("Name:")
            t = st.text_input("Message:")
            if st.form_submit_button("SEND 🔥"):
                if u and t:
                    db.collection('chat').add({'user':u, 'text':t, 'timestamp':firestore.SERVER_TIMESTAMP})
                    st.rerun()

    if st.button("⬅ EXIT VOID"):
        st.session_state.page = "welcome"
        st.rerun()
