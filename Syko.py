import streamlit as st

# --- إعدادات النظام العالمي ---
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide", initial_sidebar_state="collapsed")

# --- دمج التصاميم (01 + A + C) عبر CSS و JavaScript ---
st.markdown("""
<style>
    /* الأساسيات */
    body, .stApp {
        background-color: #000;
        margin: 0;
        overflow: hidden;
        color: #fff;
        cursor: crosshair;
    }

    /* تأثير التشويش الرقمي 01 */
    .glitch-header {
        position: relative;
        font-size: 12vw;
        font-weight: 900;
        text-transform: uppercase;
        text-align: center;
        z-index: 10;
        color: #fff;
        pointer-events: none;
    }

    .glitch-header::before, .glitch-header::after {
        content: 'SYKO';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: black;
    }

    .glitch-header::before {
        left: 4px;
        text-shadow: -4px 0 #ff00ff;
        animation: glitch-v1 2s infinite linear alternate-reverse;
    }

    .glitch-header::after {
        left: -4px;
        text-shadow: -4px 0 #00ffff;
        animation: glitch-v2 3s infinite linear alternate-reverse;
    }

    /* التفاعل البصري C و البوابة A */
    canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 5;
    }

    @keyframes glitch-v1 {
        0% { clip: rect(10px, 9999px, 30px, 0); }
        100% { clip: rect(70px, 9999px, 80px, 0); }
    }
    @keyframes glitch-v2 {
        0% { clip: rect(80px, 9999px, 90px, 0); }
        100% { clip: rect(10px, 9999px, 50px, 0); }
    }

    /* إخفاء واجهة ستريمليت ليكون التصميم نظيفاً */
    header, footer, #MainMenu {visibility: hidden;}
</style>

<div class="glitch-wrapper">
    <div class="glitch-header">SYKO</div>
</div>

<canvas id="canvas"></canvas>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];
const mouse = { x: null, y: null };

window.addEventListener('mousemove', (e) => {
    mouse.x = e.x;
    mouse.y = e.y;
    // إضافة "غبار رقمي" عند تحريك الماوس (تأثير C)
    for (let i = 0; i < 5; i++) {
        particles.push(new Particle());
    }
});

class Particle {
    constructor() {
        this.x = mouse.x;
        this.y = mouse.y;
        this.size = Math.random() * 5 + 1;
        this.speedX = Math.random() * 3 - 1.5;
        this.speedY = Math.random() * 3 - 1.5;
        this.color = Math.random() > 0.5 ? '#ff00ff' : '#00ffff';
    }
    update() {
        this.x += this.speedX;
        this.y += this.speedY;
        if (this.size > 0.2) this.size -= 0.1;
    }
    draw() {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
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
""", unsafe_allow_html=True)
