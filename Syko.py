import streamlit as st
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="SYKO EMPIRE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. التصميم الإبداعي (CSS & JavaScript)
# دمجنا الجافاسكريبت مع التصميم ليعطيك حركة ناعمة جداً
st.markdown("""
    <style>
    /* استيراد الخطوط الفخمة */
    @import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Rajdhani:wght@600&display=swap');

    /* خلفية التطبيق كاملة - لون ليلي عميق */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #2b0035 0%, #050505 100%);
        color: white;
    }

    /* حاوية العنوان المتحرك */
    .tilt-wrapper {
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60vh; /* يأخذ 60% من ارتفاع الشاشة */
    }

    /* الكلمة نفسها */
    .syko-text {
        font-family: 'Permanent Marker', cursive;
        font-size: clamp(60px, 15vw, 150px); /* يتغير الحجم حسب الشاشة */
        background: linear-gradient(180deg, #fff 0%, #ff00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 25px rgba(255, 0, 255, 0.6));
        transform-style: preserve-3d;
        cursor: pointer;
    }

    /* النص الصغير تحت العنوان */
    .subtitle {
        font-family: 'Rajdhani', sans-serif;
        font-size: 20px;
        letter-spacing: 8px;
        color: #00d2ff;
        text-align: center;
        margin-top: -20px;
        text-shadow: 0 0 10px #00d2ff;
        animation: pulse 2s infinite;
    }

    /* تأثير النبض للنص الصغير */
    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }

    /* تصميم الأزرار */
    .stButton>button {
        background: transparent;
        border: 2px solid #ff00ff;
        color: #ff00ff;
        border-radius: 30px;
        padding: 10px 40px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        font-size: 20px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: #ff00ff;
        color: white;
        box-shadow: 0 0 20px #ff00ff;
        border-color: #ff00ff;
    }
    </style>

    <div class="tilt-wrapper" id="tiltbox">
        <div id="text-container">
            <h1 class="syko-text">SYKO</h1>
            <p class="subtitle">DIGITAL LEGEND</p>
        </div>
    </div>

    <script>
    const box = document.getElementById('tiltbox');
    const text = document.getElementById('text-container');

    function handleMove(event) {
        const xVal = event.pageX || event.touches[0].pageX;
        const yVal = event.pageY || event.touches[0].pageY;
        
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        const xOffset = (width / 2 - xVal) / 25; // التحكم في قوة الميلان
        const yOffset = (height / 2 - yVal) / 25;

        text.style.transform = `rotateY(${xOffset}deg) rotateX(${yOffset}deg)`;
    }

    document.addEventListener('mousemove', handleMove);
    document.addEventListener('touchmove', handleMove);
    </script>
    """, unsafe_allow_html=True)

# 3. محتوى الصفحة التفاعلي
st.write("---") 

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # زر تشغيل النظام
    if st.button("⚡ ACTIVATE SYSTEM ⚡"):
        with st.spinner("Connecting to SYKO Server..."):
            time.sleep(1.5) # تأثير انتظار وهمي
        st.balloons()
        st.success("WELCOME TO THE FUTURE, SYKO!")
        
        # رسالة ترحيبية خاصة
        st.markdown("""
        <div style="background: rgba(0, 255, 200, 0.1); padding: 15px; border-radius: 10px; border: 1px solid #00d2ff; text-align: center;">
            <h3 style="color: white; margin:0;">SYSTEM ONLINE</h3>
            <p style="color: #bbb; margin:0;">All systems are fully operational.</p>
        </div>
        """, unsafe_allow_html=True)

# 4. تذييل الصفحة (Footer)
st.markdown("""
    <div style="position: fixed; bottom: 10px; width: 100%; text-align: center; color: #555; font-size: 12px;">
        POWERED BY PYTHON & STREAMLIT
    </div>
    """, unsafe_allow_html=True)
