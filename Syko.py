import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | GOD LEVEL", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس السينمائي الفائق - مستوى استوديوهات هوليوود
god_level_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Orbitron:wght@900&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; }
        #canvas-container { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; }
        
        /* تأثير انفجار الصفحة الثانية */
        #final-stage {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 100; opacity: 0; visibility: hidden; background: #000;
            transition: all 1s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .hero-text {
            font-size: clamp(60px, 15vw, 150px); color: #fff; text-transform: uppercase;
            letter-spacing: 30px; margin: 0; position: relative;
            text-shadow: 0 0 30px #00ffff, 0 0 60px #ff00ff, 0 0 100px #00ffff;
            animation: glitch-flicker 3s infinite;
        }

        .infinity-king {
            font-size: 180px; color: #ff00ff; margin: -20px 0;
            filter: drop-shadow(0 0 50px #ff00ff);
            transform: scale(0); transition: 2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes glitch-flicker {
            0%, 100% { opacity: 1; transform: skew(0deg); }
            5% { opacity: 0.8; transform: skew(2deg); }
            10% { opacity: 1; transform: skew(-1deg); }
        }

        .flash {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: #fff; z-index: 500; opacity: 0; pointer-events: none;
        }

        .show-stage { opacity: 1 !important; visibility: visible !important; }
        .show-stage .infinity-king { transform: scale(1); }
    </style>
</head>
<body>
    <div class="flash" id="flash-effect"></div>
    <div id="canvas-container"></div>

    <div id="final-stage">
        <h1 class="hero-text">SYKO</h1>
        <div class="infinity-king">∞</div>
        <h1 class="hero-text">YOUSRA</h1>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        let scene, camera, renderer, starMesh, vortexMesh;
        let isAttracting = false;
        let bloomScale = 1;

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 5;

            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('canvas-container').appendChild(renderer.domElement);

            // نسيج الجزيئات (The Cosmic Dust)
            const geo = new THREE.BufferGeometry();
            const pos = [];
            for (let i = 0; i < 15000; i++) {
                pos.push(Math.random()*20-10, Math.random()*20-10, Math.random()*20-10);
            }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            const mat = new THREE.PointsMaterial({ color: 0x00ffff, size: 0.02, transparent: true, blending: THREE.AdditiveBlending });
            starMesh = new THREE.Points(geo, mat);
            scene.add(starMesh);

            animate();
        }

        function animate() {
            requestAnimationFrame(animate);
            starMesh.rotation.y += 0.001;
            
            if (isAttracting) {
                const posArr = starMesh.geometry.attributes.position.array;
                for (let i = 0; i < posArr.length; i += 3) {
                    posArr[i] *= 0.95;     // سحب X
                    posArr[i+1] *= 0.95;   // سحب Y
                    posArr[i+2] *= 0.95;   // سحب Z
                }
                starMesh.geometry.attributes.position.needsUpdate = true;
                starMesh.material.color.lerp(new THREE.Color(0xff00ff), 0.05);
                camera.position.z *= 0.98; // زووم مرعب للداخل
            }
            renderer.render(scene, camera);
        }

        window.addEventListener('mousedown', () => {
            if(!isAttracting) {
                isAttracting = true;
                // فلاش انفجاري عند الابتلاع
                setTimeout(() => {
                    document.getElementById('flash-effect').style.opacity = '1';
                    setTimeout(() => {
                        document.getElementById('flash-effect').style.opacity = '0';
                        document.getElementById('final-stage').classList.add('show-stage');
                    }, 100);
                }, 1500);
            }
        });

        init();
    </script>
</body>
</html>
"""

components.html(god_level_code, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
