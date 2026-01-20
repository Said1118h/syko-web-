import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتكون نظيفة تماماً
st.set_page_config(page_title="SYKO UNIVERSE", layout="wide", initial_sidebar_state="collapsed")

# كود الـ HTML والـ CSS والـ JS في كتلة واحدة لضمان التفاعل
syko_world_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Arial Black', sans-serif; cursor: none; }
        canvas { display: block; }
        
        /* تأثير التشويش (Glitch) */
        .glitch-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 10;
            user-select: none;
        }
        .glitch {
            color: white;
            font-size: 10vw;
            font-weight: 900;
            position: relative;
            text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00;
            animation: glitch 500ms infinite;
        }
        @keyframes glitch {
            0% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00; }
            50% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff, -0.05em -0.05em 0 #fffc00; }
            100% { text-shadow: -0.025em 0.05em 0 #00fffc, 0.05em 0 0 #fc00ff, 0 -0.05em 0 #fffc00; }
        }
    </style>
</head>
<body>
    <div class="glitch-container">
        <div class="glitch">SYKO</div>
    </div>
    <canvas id="canvas"></canvas>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particles = [];
        const mouse = { x: undefined, y: undefined };

        // دعم الماوس واللمس للجوال
        function handleMove(e) {
            mouse.x = e.x || e.touches[0].clientX;
            mouse.y = e.y || e.touches[0].clientY;
            for (let i = 0; i < 5; i++) {
                particles.push(new Particle());
            }
        }

        window.addEventListener('mousemove', handleMove);
        window.addEventListener('touchmove', handleMove);

        class Particle {
            constructor() {
                this.x = mouse.x;
                this.y = mouse.y;
                this.size = Math.random() * 10 + 2;
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
                ctx.shadowBlur = 15;
                ctx.shadowColor = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
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

# تشغيل المكون بأقصى مساحة ممكنة
components.html(syko_world_code, height=800, scrolling=False)
