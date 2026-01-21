import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | THE VOID", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس المتقدم - شيدرز وتفاعل فيزيائي
supreme_vortex = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; cursor: crosshair; }
        canvas { display: block; filter: contrast(120%) brightness(110%); }
        
        .ui-layer {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 1000; pointer-events: none; opacity: 0; transition: 3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .name {
            font-family: 'Arial Black', sans-serif; font-size: 85px; font-weight: 900;
            letter-spacing: 20px; color: #fff; line-height: 0.8;
            text-shadow: 0 0 20px #ff00ff, 0 0 50px #00ffff;
        }
        .inf-symbol {
            font-size: 140px; color: #00ffff; display: block; margin: 20px 0;
            filter: drop-shadow(0 0 30px #00ffff); animation: float 3s infinite ease-in-out;
        }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
        .active { opacity: 1; }
    </style>
</head>
<body>
    <div class="ui-layer" id="ui">
        <div class="name">SYKO</div>
        <div class="inf-symbol">∞</div>
        <div class="name">YOUSRA</div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
    <script>
        let particles = [];
        let vortex = false;

        function setup() {
            createCanvas(windowWidth, windowHeight);
            for (let i = 0; i < 2500; i++) particles.push(new Particle());
        }

        function draw() {
            background(0, 30); // أثر الدخان الرقمي
            let centerX = width / 2;
            let centerY = height / 2;

            for (let p of particles) {
                p.attract(centerX, centerY, vortex);
                p.update();
                p.show();
            }
        }

        class Particle {
            constructor() {
                this.pos = createVector(random(width), random(height));
                this.vel = p5.Vector.random2D().mult(random(2, 5));
                this.acc = createVector();
                this.color = random() > 0.5 ? color(255, 0, 255, 150) : color(0, 255, 255, 150);
                this.maxSpeed = random(4, 10);
            }

            attract(tx, ty, isVortex) {
                let force = createVector(tx - this.pos.x, ty - this.pos.y);
                let d = force.mag();
                if (isVortex) {
                    force.setMag(1.2);
                    let rotate = createVector(-force.y, force.x).mult(2.5); // قوة الدوران
                    this.acc.add(rotate);
                    if (d < 50) this.pos = createVector(random(width), random(height)); // إعادة تدوير الجزيئات
                } else {
                    force.setMag(0.1);
                }
                this.acc.add(force);
            }

            update() {
                this.vel.add(this.acc);
                this.vel.limit(this.maxSpeed);
                this.pos.add(this.vel);
                this.acc.mult(0);
            }

            show() {
                stroke(this.color);
                strokeWeight(random(1, 3));
                point(this.pos.x, this.pos.y);
            }
        }

        function mousePressed() {
            vortex = true;
            document.getElementById('ui').classList.add('active');
        }
    </script>
</body>
</html>
"""

components.html(supreme_vortex, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
