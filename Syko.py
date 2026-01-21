import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتكون شاشة عرض سينمائية
st.set_page_config(page_title="SYKO & YOUSRA | THE ULTIMATE", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس الفائق (Particle Physics Engine)
ultra_vortex_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Montserrat', sans-serif; cursor: none; }
        #canvas-container { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; }
        
        .content {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 100; opacity: 0; transition: all 2s ease-in-out;
            pointer-events: none;
        }

        .name {
            font-size: 100px; font-weight: 900; letter-spacing: 25px; color: #fff;
            text-shadow: 0 0 30px #00ffff, 0 0 60px #ff00ff;
            margin: 0;
        }

        .infinity-symbol {
            font-size: 150px; color: #ff00ff; line-height: 1;
            filter: drop-shadow(0 0 40px #ff00ff);
            margin: -20px 0;
        }

        .show { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
        
        #instruction {
            position: fixed; bottom: 30px; width: 100%; text-align: center;
            color: rgba(0, 255, 255, 0.5); font-size: 12px; letter-spacing: 5px;
            text-transform: uppercase; z-index: 10;
        }
    </style>
</head>
<body>
    <div id="instruction">HOLD MOUSE OR TOUCH TO ACTIVATE BLACK HOLE</div>
    <div id="canvas-container"></div>
    
    <div class="content" id="final-ui">
        <div class="name">SYKO</div>
        <div class="infinity-symbol">∞</div>
        <div class="name">YOUSRA</div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
    <script>
        let particles = [];
        let numParticles = 1200;
        let vortexActive = false;

        function setup() {
            let canvas = createCanvas(windowWidth, windowHeight);
            canvas.parent('canvas-container');
            for (let i = 0; i < numParticles; i++) {
                particles.push(new Particle());
            }
        }

        function draw() {
            background(0, 0, 0, 25); // أثر حركة (Motion Blur)
            
            let center = createVector(width / 2, height / 2);
            let target = vortexActive ? center : createVector(mouseX, mouseY);

            for (let p of particles) {
                p.update(target, vortexActive);
                p.show();
            }

            if (vortexActive) {
                // تقليل عدد الجسيمات لزيادة التركيز في المركز
                if (particles.length > 100) particles.splice(0, 5);
            }
        }

        class Particle {
            constructor() {
                this.pos = createVector(random(width), random(height));
                this.vel = p5.Vector.random2D();
                this.acc = createVector();
                this.maxSpeed = random(3, 8);
                this.color = random() > 0.5 ? color(255, 0, 255) : color(0, 255, 255);
            }

            update(target, isVortex) {
                let force = p5.Vector.sub(target, this.pos);
                let d = force.mag();
                if (isVortex) {
                    force.setMag(1.5);
                    let rotateForce = force.copy().rotate(HALF_PI); // دوران حول الثقب
                    this.acc.add(rotateForce);
                } else {
                    force.setMag(0.5);
                }
                this.acc.add(force);
                this.vel.add(this.acc);
                this.vel.limit(this.maxSpeed);
                this.pos.add(this.vel);
                this.acc.mult(0);
            }

            show() {
                stroke(this.color);
                strokeWeight(random(1, 4));
                point(this.pos.x, this.pos.y);
            }
        }

        function mousePressed() {
            vortexActive = true;
            document.getElementById('instruction').style.opacity = 0;
            setTimeout(() => {
                document.getElementById('final-ui').classList.add('show');
            }, 1500);
        }

        function windowResized() {
            resizeCanvas(windowWidth, windowHeight);
        }
    </script>
</body>
</html>
"""

components.html(ultra_vortex_code, height=900, scrolling=False)

# إخفاء واجهة ستريمليت بالكامل
st.markdown("""
<style>
    header, footer, #MainMenu {visibility: hidden;}
    .stApp {background: black;}
</style>
""", unsafe_allow_html=True)
