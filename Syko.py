import streamlit as st
import streamlit.components.v1 as components
import time

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="SYKO & YOUSRA | COMMAND CENTER", layout="wide", initial_sidebar_state="collapsed")

# --- 2. محرك التفاعل الخلفي (Touch & Mouse Particles) ---
# هذا الكود يضمن بقاء ميزة التفاعل التي تعشقها مع كل لمسة
visual_engine = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; }
        canvas { position: fixed; top: 0; left: 0; z-index: -1; }
        .top-brand {
            position: absolute; top: 10px; width: 100%; text-align: center;
            color: #fff; font-family: 'Courier New'; letter-spacing: 10px;
            font-size: 40px; font-weight: bold; text-shadow: 0 0 10px #00ffff;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="top-brand">SYKO <span style="color:#ff00ff">✕</span> YOUSRA</div>
    <canvas id="canvas"></canvas>
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth; canvas.height = window.innerHeight;
        let particles = [];
        function createP(x, y) { for (let i = 0; i < 5; i++) particles.push(new P(x, y)); }
        window.addEventListener('mousemove', (e) => createP(e.x, e.y));
        window.addEventListener('touchmove', (e) => createP(e.touches[0].clientX, e.touches[0].clientY));
        class P {
            constructor(x, y) {
                this.x = x; this.y = y;
                this.size = Math.random() * 5 + 1;
                this.spX = Math.random() * 3 - 1.5; this.spY = Math.random() * 3 - 1.5;
                this.color = Math.random() > 0.5 ? '#ff00ff' : '#00ffff';
            }
            update() { this.x += this.spX; this.y += this.spY; if(this.size > 0.1) this.size -= 0.1; }
            draw() { ctx.fillStyle = this.color; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill(); }
        }
        function anim() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            particles.forEach((p, i) => { p.update(); p.draw(); if(p.size <= 0.1) particles.splice(i, 1); });
            requestAnimationFrame(anim);
        }
        anim();
    </script>
</body>
</html>
"""
components.html(visual_engine, height=150)

# --- 3. الأدوات الوظيفية (Functional Tools) ---
st.markdown("""
<style>
    .stApp { background: transparent; }
    .console-card {
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid #ff00ff;
        border-radius: 10px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

col_tools, col_status = st.columns([2, 1])

with col_tools:
    st.markdown('<div class="console-card">', unsafe_allow_html=True)
    st.subheader("🖥️ SYKO TERMINAL")
    command = st.text_input("ENTER COMMAND:", placeholder="e.g., /encrypt, /status, /bypass")
    
    if command:
        if "/encrypt" in command:
            text = command.replace("/encrypt ", "")
            st.code(f"ENCRYPTING: {text} ...\nRESULT: 0x{text.encode().hex()}", language="bash")
        elif "/status" in command:
            st.success("ALL SYSTEMS OPERATIONAL. CONNECTION SECURE.")
        else:
            st.error("UNKNOWN COMMAND. ACCESS DENIED.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_status:
    st.markdown('<div class="console-card" style="border-color:#00ffff;">', unsafe_allow_html=True)
    st.subheader("📊 LIVE STATS")
    st.write("CORE INTEGRITY")
    st.progress(92)
    st.write("ENCRYPTION LEVEL")
    st.progress(100)
    st.markdown('<p style="color:#00ffff; font-size:12px;">LATENCY: 12ms<br>LOCATION: ENCRYPTED</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. الهدف الفعال: Encryptor Tool ---
st.write("---")
st.subheader("🔐 SYKO & YOUSRA ENCRYPTION TOOL")
input_data = st.text_area("أدخل رسالة سرية لتشفيرها:")
if st.button("توليد كود التشفير"):
    if input_data:
        st.warning(f"تم التشفير بنجاح: SYKO-SEC-{int(time.time())}")
        st.code(input_data[::-1].upper(), language="text") # مثال بسيط لوظيفة حقيقية

# إخفاء عناصر Streamlit
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)
