import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الكاملة
st.set_page_config(page_title="SYKO & YOUSRA | THE TRANSITION", layout="wide", initial_sidebar_state="collapsed")

# كود الأنيميشن المتقدم: الانتقال من الدوامة إلى الصفحة الثانية
vortex_transition_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Orbitron', sans-serif; }
        canvas { display: block; }

        /* حاوية الصفحة الثانية (تكون مخفية في البداية) */
        #second-page {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            background: radial-gradient(circle, #050505 0%, #000 100%);
            z-index: 2000; opacity: 0; visibility: hidden;
            transition: opacity 3s ease-in;
        }

        .name-reveal {
            font-size: 100px; color: #fff; letter-spacing: 20px;
            text-shadow: 0 0 20px #00ffff, 0 0 50px #ff00ff;
            transform: translateY(30px); transition: 2s ease-out;
        }

        .inf-symbol {
            font-size: 120px; color: #ff00ff; margin: 20px 0;
            filter: drop-shadow(0 0 30px #ff00ff);
            opacity: 0; transition: 4s ease-in;
        }

        .active-page { opacity: 1 !important; visibility: visible !important; }
        .active-page .name-reveal { transform: translateY(0); }
        .active-page .inf-symbol { opacity: 1; }

        #instruction {
            position: fixed; bottom: 40px; width: 100%; text-align: center;
            color: #00ffff; letter-spacing: 8px; font-size: 12px; z-index: 100;
            text-transform: uppercase; cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="instruction">HOLD TO CONSUME THE UNIVERSE</div>
    <canvas id="vortexCanvas"></canvas>

    <div id="second-page">
        <div class="name-reveal">SYKO</div>
        <div class="inf-symbol">∞</div>
        <div class="name-reveal">YOUSRA</div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
    <script>
        let particles = [];
        let consuming = false;
        let transitionStarted = false;

        function setup() {
            let cnv = createCanvas(windowWidth, windowHeight);
            cnv.parent('vortexCanvas');
            for (let i = 0; i < 2000; i++) particles.push(new Particle());
        }

        function draw() {
            background(0, consuming ? 50 : 30);
            let tx = width/2;
            let ty = height/2;

            for (let p of particles) {
                p.update(tx, ty, consuming);
                p.show();
            }

            if (consuming && !transitionStarted) {
                // فحص إذا كانت الجزيئات اقتربت كفاية من المركز
                let allIn = particles.every(p => p.dist < 50);
                if (particles.length < 50) {
                    startTransition();
                }
            }
        }

        class Particle {
            constructor() {
                this.pos = createVector(random(width), random(height));
                this.vel = p5.Vector.random2D().mult(random(1, 5));
                this.color = random() > 0.5 ? color(0, 255, 255) : color(255, 0, 255);
                this.dist = 1000;
            }

            update(tx, ty, isConsuming) {
                let target = createVector(tx, ty);
                let force = p5.Vector.sub(target, this.pos);
                this.dist = force.mag();

                if (isConsuming) {
                    force.setMag(2.5);
                    let spin = createVector(-force.y, force.x).mult(4);
                    this.pos.add(spin);
                    this.pos.add(force);
                    if (this.dist < 10) particles.splice(particles.indexOf(this), 1);
                } else {
                    // حركة عشوائية جميلة قبل الضغط
                    let noiseForce = p5.Vector.random2D().mult(0.1);
                    this.pos.add(this.vel);
                    this.pos.add(noiseForce);
                    if (this.pos.x < 0 || this.pos.x > width) this.vel.x *= -1;
                    if (this.pos.y < 0 || this.pos.y > height) this.vel.y *= -1;
                }
            }

            show() {
                stroke(this.color);
                strokeWeight(2);
                point(this.pos.x, this.pos.y);
            }
        }

        function mousePressed() {
            consuming = true;
            document.getElementById('instruction').style.opacity = '0';
        }

        function startTransition() {
            transitionStarted = true;
            document.getElementById('second-page').classList.add('active-page');
        }

        function windowResized() { resizeCanvas(windowWidth, windowHeight); }
    </script>
</body>
</html>
"""

components.html(vortex_transition_code, height=900, scrolling=False)

# مسح أي زوائد من ستريمليت لضمان النقاء البصري
st.markdown("""
<style>
    header, footer, #MainMenu {visibility: hidden;}
    .stApp {background: black;}
</style>
""", unsafe_allow_html=True)
