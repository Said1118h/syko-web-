import streamlit as st

# إعدادات الصفحة لتختفي كل عناصر ستريمليت المزعجة
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* إخفاء القوائم ليكون التصميم كامل الشاشة */
    header, footer, #MainMenu {visibility: hidden;}
    .stApp { background-color: #000; overflow: hidden; }

    /* تأثير التشويش الرقمي (Glitch 01) */
    .syko-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 10;
        pointer-events: none; /* عشان ما يمنع تفاعل الماوس مع الخلفية */
    }

    .glitch {
        font-size: 150px;
        font-weight: 900;
        text-transform: uppercase;
        position: relative;
        color: white;
        font-family: 'Arial Black', sans-serif;
    }

    .glitch::before, .glitch::after {
        content: 'SYKO';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: black;
    }

    .glitch::before {
        left: 3px;
        text-shadow: -3px 0 #ff00ff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim 2s infinite linear alternate-reverse;
    }

    .glitch::after {
        left: -3px;
        text-shadow: -3px 0 #00ffff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim2 3s infinite linear alternate-reverse;
    }

    @keyframes glitch-anim {
        0% { clip: rect(10px, 9999px, 30px, 0); }
        100% { clip: rect(80px, 9999px, 100px, 0); }
    }
    @keyframes glitch-anim2 {
        0% { clip: rect(60px, 9999px, 80px, 0); }
        100% { clip: rect(0px, 9999px, 40px, 0); }
    }

    /* تأثير التفاعل C (Canvas) */
    #bg-canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1;
    }
</style>

<div class="syko-container">
    <div class="glitch">SYKO</div>
</div>

<canvas id="bg-canvas"></canvas>

<script>
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];
    const mouse = { x: null, y: null };

    window.addEventListener('mousemove', function(event) {
        mouse.x = event.x;
        mouse.y = event.y;
        for (let i = 0; i < 3; i++) {
            particles.push(new Particle());
        }
    });

    class Particle {
        constructor() {
            this.x = mouse.x;
            this.y = mouse.y;
            this.size = Math.random() * 8 + 1;
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
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; // تأثير مسح تدريجي عشان يترك "أثر" (Trail)
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
""", unsafe_allow_html=True)
