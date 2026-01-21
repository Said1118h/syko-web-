import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="SYKO & YOUSRA | INFINITY", layout="wide", initial_sidebar_state="collapsed")

# إدارة الحالة (البوابة أم العالم الداخلي)
if "portal_opened" not in st.session_state:
    st.session_state.portal_opened = False

# --- كود الجرافيكس (HTML + CSS + JS) ---
portal_and_infinity_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Arial Black', sans-serif; cursor: crosshair; }
        canvas { position: fixed; top: 0; left: 0; z-index: 1; }
        
        /* تأثير الثقب الأسود */
        #black-hole {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 250px; height: 250px; background: #000; border-radius: 50%;
            box-shadow: 0 0 60px 30px #ff00ff, 0 0 100px 60px #00ffff, inset 0 0 50px #fff;
            z-index: 100; cursor: pointer; transition: 1s;
        }
        #black-hole:hover { box-shadow: 0 0 120px 80px #ff00ff, inset 0 0 80px #00ffff; transform: translate(-50%, -50%) scale(1.1); }
        
        /* نص الدعوة */
        .portal-text {
            position: absolute; bottom: 20%; width: 100%; text-align: center;
            color: #fff; letter-spacing: 5px; font-size: 14px; z-index: 101; pointer-events: none;
        }

        /* شعار الانفينيتي المتوهج */
        .infinity-container {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 50; display: none;
        }
        .names {
            font-size: 60px; color: #fff; text-transform: uppercase; letter-spacing: 10px;
            text-shadow: 0 0 20px #00ffff;
        }
        .infinity-symbol {
            font-size: 100px; color: #ff00ff; text-shadow: 0 0 30px #ff00ff;
            display: inline-block; animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.2); opacity: 1; text-shadow: 0 0 50px #ff00ff; }
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
    
    <div id="black-hole" onclick="enterVoid()"></div>
    <div class="portal-text" id="p-text">TOUCH THE VOID TO ENTER</div>

    <div class="infinity-container" id="infinity-ui">
        <div class="names">SYKO</div>
        <div class="infinity-symbol">∞</div>
        <div class="names">YOUSRA</div>
    </div>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let particles = [];
        let vortexMode = false;

        function enterVoid() {
            vortexMode = true;
            document.getElementById('black-hole').style.transform = 'translate(-50%, -50%) scale(0)';
            document.getElementById('p-text').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('infinity-ui').style.display = 'block';
                vortexMode = false;
            }, 2000);
        }

        window.addEventListener('mousemove', (e) => {
            if(!vortexMode) for(let i=0; i<3; i++) particles.push(new P(e.x, e.y));
        });

        class P {
            constructor(x, y) {
                this.x = x; this.y = y;
                this.size = Math.random() * 5 + 1;
                this.spX = Math.random() * 6 - 3;
                this.spY = Math.random() * 6 - 3;
                this.color = Math.random() > 0.5 ? '#ff00ff' : '#00ffff';
            }
            update() {
                if(vortexMode) {
                    let dx = window.innerWidth/2 - this.x;
                    let dy = window.innerHeight/2 - this.y;
                    this.x += dx * 0.05; this.y += dy * 0.05;
                    this.size *= 0.95;
                } else {
                    this.x += this.spX; this.y += this.spY;
                    if(this.size > 0.1) this.size -= 0.1;
                }
            }
            draw() {
                ctx.fillStyle = this.color; ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill();
            }
        }

        function anim() {
            ctx.fillStyle = 'rgba(0,0,0,0.15)'; ctx.fillRect(0,0,canvas.width,canvas.height);
            particles.forEach((p, i) => {
                p.update(); p.draw();
                if(p.size <= 0.1) particles.splice(i, 1);
            });
            requestAnimationFrame(anim);
        }
        anim();
    </script>
</body>
</html>
"""

# عرض البوابة في الموقع
components.html(portal_and_infinity_code, height=800, scrolling=False)

# إخفاء عناصر Streamlit
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)
