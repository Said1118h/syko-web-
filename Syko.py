import streamlit as st
import streamlit.components.v1 as components

# إعدادات الشاشة الكاملة
st.set_page_config(page_title="SYKO & YOUSRA | THE VOID", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس المتقدم (Three.js + Shaders)
black_hole_pro = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Orbitron', sans-serif; }
        #ui-layer {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 10; pointer-events: none; transition: 2s;
        }
        .glitch-text {
            font-size: 80px; color: #fff; font-weight: 900; letter-spacing: 15px;
            text-shadow: 0 0 20px #00ffff, 0 0 40px #ff00ff; opacity: 0; transform: scale(0.5);
            transition: all 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .infinity-icon {
            font-size: 100px; color: #ff00ff; opacity: 0;
            filter: drop-shadow(0 0 20px #ff00ff); transition: 2s;
        }
        #instruction {
            position: absolute; bottom: 50px; color: #00ffff; 
            letter-spacing: 5px; animation: blink 1s infinite;
        }
        @keyframes blink { 50% { opacity: 0.3; } }
    </style>
</head>
<body>
    <div id="ui-layer">
        <div id="syko" class="glitch-text">SYKO</div>
        <div id="inf" class="infinity-icon">∞</div>
        <div id="yousra" class="glitch-text">YOUSRA</div>
        <div id="instruction">TAP THE SINGULARITY</div>
    </div>

    <script>
        let scene, camera, renderer, particles, starGeo;
        let portalActive = false;

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
            camera.position.z = 1;
            camera.rotation.x = Math.PI / 2;

            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            starGeo = new THREE.BufferGeometry();
            let positions = [];
            let velocities = [];
            for (let i = 0; i < 8000; i++) {
                positions.push(Math.random() * 600 - 300, Math.random() * 600 - 300, Math.random() * 600 - 300);
                velocities.push(0);
            }
            starGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            
            let sprite = new THREE.TextureLoader().load('https://threejs.org/examples/textures/sprites/disc.png');
            let starMaterial = new THREE.PointsMaterial({
                color: 0x00ffff, size: 0.7, map: sprite, transparent: true, blending: THREE.AdditiveBlending
            });

            particles = new THREE.Points(starGeo, starMaterial);
            scene.add(particles);

            animate();
        }

        function animate() {
            let positions = starGeo.attributes.position.array;
            for (let i = 0; i < positions.length; i += 3) {
                if (portalActive) {
                    // تأثير الثقب الأسود (جذب الجسيمات للمركز)
                    positions[i] *= 0.96;
                    positions[i+1] *= 0.96;
                    positions[i+2] *= 0.96;
                } else {
                    positions[i+1] -= 1.5; // حركة النجوم العادية
                    if (positions[i+1] < -200) positions[i+1] = 200;
                }
            }
            starGeo.attributes.position.needsUpdate = true;
            particles.rotation.y += 0.002;
            
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }

        window.addEventListener('mousedown', () => {
            portalActive = true;
            document.getElementById('instruction').style.display = 'none';
            particles.material.color.setHex(0xff00ff);
            
            setTimeout(() => {
                document.getElementById('syko').style.opacity = '1';
                document.getElementById('syko').style.transform = 'scale(1)';
            }, 1000);
            setTimeout(() => {
                document.getElementById('inf').style.opacity = '1';
            }, 1800);
            setTimeout(() => {
                document.getElementById('yousra').style.opacity = '1';
                document.getElementById('yousra').style.transform = 'scale(1)';
            }, 2500);
        });

        init();
    </script>
</body>
</html>
"""

# عرض العمل في Streamlit
components.html(black_hole_pro, height=900, scrolling=False)

# إخفاء عناصر ستريمليت
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)
