import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | THE VOID", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس الفائق: شيدرز + جزيئات فيزيائية مع توهج نيون
super_pro_vortex = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; cursor: none; }
        canvas { display: block; }
        .ui-layer {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 1000; pointer-events: none; opacity: 0;
            transition: opacity 2s ease-in-out, transform 2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .name {
            font-family: 'Arial Black', sans-serif; font-size: clamp(40px, 10vw, 90px);
            font-weight: 900; letter-spacing: 15px; color: #fff;
            text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff;
        }
        .inf-symbol {
            font-size: clamp(60px, 15vw, 130px); color: #00ffff; margin: 10px 0;
            filter: drop-shadow(0 0 30px #00ffff); animation: pulse 2s infinite ease-in-out;
        }
        @keyframes pulse { 0%, 100% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } }
        .active { opacity: 1; transform: translate(-50%, -50%) scale(1); }
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
        let isActive = false;

        function setup() {
            createCanvas(windowWidth, windowHeight);
            // بناء "نسيج الفضاء" بـ 3000 جزيء ضوئي
            for (let i = 0; i < 3000; i++) particles.push(new Particle());
        }

        function draw() {
            // تأثير "Motion Blur" سينمائي لتعميق الحركة
            background(0, 45); 
            
            let tx = isActive ? width/2 : mouseX;
            let ty = isActive ? height/2 : mouseY;

            for (let p of particles) {
                p.behavior(tx, ty, isActive);
                p.update();
                p.show();
            }
        }

        class Particle {
            constructor() {
                this.pos = createVector(random(width), random(height));
                this.vel = p5.Vector.random2D();
                this.acc = createVector();
                this.maxSpeed = random(3, 12);
                this.color = random() > 0.5 ? color(0, 255, 255, 180) : color(255, 0, 255, 180);
                this.size = random(1, 4);
            }

            behavior(tx, ty, active) {
                let target = createVector(tx, ty);
                let force = p5.Vector.sub(target, this.pos);
                let d = force.mag();

                if (active) {
                    // دوامة الثقب الأسود الحقيقية
                    force.setMag(1.5);
                    let steering = createVector(-force.y, force.x).mult(3); 
                    this.acc.add(steering);
                    this.acc.add(force);
                    if (d < 30) this.pos = createVector(random(width), random(height));
                } else {
                    // تفاعل اللمس (الهروب ثم العودة)
                    if (d < 150) {
                        force.setMag(-2);
                        this.acc.add(force);
                    } else {
                        let wander = p5.Vector.random2D().mult(0.2);
                        this.acc.add(wander);
                    }
                }
            }

            update() {
                this.vel.add(this.acc);
                this.vel.limit(this.maxSpeed);
                this.pos.add(this.vel);
                this.acc.mult(0);
            }

            show() {
                stroke(this.color);
                strokeWeight(this.size);
                point(this.pos.x, this.pos.y);
            }
        }

        function mousePressed() {
            isActive = !isActive;
            const ui = document.getElementById('ui');
            if(isActive) ui.classList.add('active');
            else ui.classList.remove('active');
        }

        function windowResized() {
            resizeCanvas(windowWidth, windowHeight);
        }
    </script>
</body>
</html>
"""

components.html(super_pro_vortex, height=900, scrolling=False)

# تصفير واجهة ستريمليت ليكون التركيز 100% على الجرافيكس
st.markdown("""
<style>
    header, footer, #MainMenu {visibility: hidden;}
    .stApp {background: black;}
    * { overflow: hidden; }
</style>
""", unsafe_allow_html=True)
