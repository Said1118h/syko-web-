import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات النظام العالمي
st.set_page_config(page_title="SYKO & YOUSRA PRO", layout="wide", initial_sidebar_state="collapsed")

# إدارة الصفحات
if "page" not in st.session_state:
    st.session_state.page = "HOME"

# 2. كود "الروح والتفاعل" (HTML/JS/CSS) - يغطي الشاشة بالكامل
# ملاحظة: هذا الجزء هو المسؤول عن ميزة التفاعل مع اللمس والماوس
pro_background = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; color: #fff; font-family: 'Arial Black', sans-serif; overflow: hidden; }
        canvas { position: fixed; top: 0; left: 0; z-index: -1; width: 100vw; height: 100vh; }
        
        .main-header {
            position: relative;
            z-index: 10;
            text-align: center;
            padding-top: 5vh;
            pointer-events: none; /* عشان ما يمنع التفاعل مع الخلفية */
        }

        .glitch-title {
            font-size: 80px;
            font-weight: 900;
            text-transform: uppercase;
            position: relative;
            text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff;
            animation: glitch 500ms infinite;
            letter-spacing: 10px;
        }

        @keyframes glitch {
            0% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff; }
            50% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff; }
            100% { text-shadow: -0.025em 0.05em 0 #00fffc, 0.05em 0 0 #fc00ff; }
        }

        .subtitle {
            color: #00ffff;
            letter-spacing: 5px;
            font-size: 14px;
            margin-top: -10px;
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
    <div class="main-header">
        <div class="glitch-title">SYKO <span style="color:#ff00ff">✕</span> YOUSRA</div>
        <div class="subtitle">NEURAL INTERFACE v2.0</div>
    </div>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particles = [];
        const mouse = { x: undefined, y: undefined };

        // دعم الماوس واللمس (عشان التفاعل اللي طلبته)
        function addParticles(x, y) {
            for (let i = 0; i < 5; i++) {
                particles.push(new Particle(x, y));
            }
        }

        window.addEventListener('mousemove', (e) => {
            mouse.x = e.x; mouse.y = e.y;
            addParticles(e.x, e.y);
        });

        window.addEventListener('touchmove', (e) => {
            mouse.x = e.touches[0].clientX;
            mouse.y = e.touches[0].clientY;
            addParticles(mouse.x, mouse.y);
        });

        class Particle {
            constructor(x, y) {
                this.x = x; this.y = y;
                this.size = Math.random() * 8 + 2;
                this.speedX = Math.random() * 4 - 2;
                this.speedY = Math.random() * 4 - 2;
                this.color = Math.random() > 0.5 ? '#ff00ff' : '#00ffff';
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.size > 0.2) this.size -= 0.15;
            }
            draw() {
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].size <= 0.2) {
                    particles.splice(i, 1);
                    i--;
                }
            }
            requestAnimationFrame(animate);
        }
        animate();
    </script>
</body>
</html>
"""

# عرض الخلفية التفاعلية مع الهيدر
components.html(pro_background, height=320)

# 3. نظام الملاحة (Navigation) بتصميم زجاجي
st.markdown("""
<style>
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #ff00ff !important;
        color: #fff !important;
        border-radius: 10px !important;
        transition: 0.4s;
        height: 50px;
        width: 100%;
        font-weight: bold;
    }
    .stButton > button:hover {
        background: #ff00ff !important;
        box-shadow: 0 0 25px #ff00ff;
        transform: translateY(-3px);
    }
    .pro-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

nav_cols = st.columns(3)
with nav_cols[0]:
    if st.button("🌌 THE CORE"): st.session_state.page = "HOME"
with nav_cols[1]:
    if st.button("📂 ARCHIVES"): st.session_state.page = "VAULT"
with nav_cols[2]:
    if st.button("📡 NEURAL LINK"): st.session_state.page = "LINK"

st.markdown("<br>", unsafe_allow_html=True)

# 4. محتوى الصفحات الـ PRO
if st.session_state.page == "HOME":
    st.markdown("""
    <div class="pro-card">
        <h2 style="color:#00ffff; letter-spacing:3px;">SYSTEM: ONLINE</h2>
        <p style="color:#ccc; font-size:18px; line-height:1.6;">
            مرحباً بك في المنطقة المركزية لـ <b>SYKO & YOUSRA</b>. <br>
            هنا تبدأ التجربة الرقمية المتطورة. استمتع بالتفاعل مع الذرات في الخلفية.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "VAULT":
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#ff00ff;'>📂 DATABASE</h2>", unsafe_allow_html=True)
    v_cols = st.columns(2)
    with v_cols[0]:
        st.info("Project: Cypher-X (Active)")
        st.info("Project: Ghost Protocol (Encrypted)")
    with v_cols[1]:
        st.info("User: SYKO [Admin]")
        st.info("User: YOUSRA [Co-Founder]")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "LINK":
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#00ffff;'>📡 NEURAL STATUS</h2>", unsafe_allow_html=True)
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.write("Sync Rate")
        st.progress(99)
    with col_stat2:
        st.write("Encryption Level")
        st.progress(100)
    st.code("Connecting to Syko-Network... [SUCCESS]", language="bash")
    st.markdown('</div>', unsafe_allow_html=True)

# إخفاء عناصر ستريمليت الزائدة
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)
