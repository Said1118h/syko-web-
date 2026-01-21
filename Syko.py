import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO | THE SINGULARITY", layout="wide", initial_sidebar_state="collapsed")

# شيدر (Shader) احترافي للثقب الأسود - جرافيكس سينمائي
black_hole_shader = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Arial Black', sans-serif; }
        #canvas-container { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; }
        
        .overlay {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 10; pointer-events: none;
        }
        
        .name-container { opacity: 0; transition: 3s; }
        .syko-yousra {
            font-size: 80px; font-weight: 900; letter-spacing: 20px; color: #fff;
            text-shadow: 0 0 30px #ff00ff, 0 0 60px #00ffff;
        }
        .infinity { font-size: 120px; color: #ff00ff; margin: 10px 0; display: block; }
        
        #enter-btn {
            position: absolute; bottom: 10%; left: 50%; transform: translateX(-50%);
            padding: 15px 40px; background: none; border: 2px solid #00ffff;
            color: #00ffff; letter-spacing: 5px; cursor: pointer; z-index: 20;
            transition: 0.5s; font-weight: bold;
        }
        #enter-btn:hover { background: #00ffff; color: #000; box-shadow: 0 0 50px #00ffff; }
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <div class="overlay" id="names">
        <div class="syko-yousra">SYKO</div>
        <div class="infinity">∞</div>
        <div class="syko-yousra">YOUSRA</div>
    </div>
    <button id="enter-btn" onclick="startVortex()">ENTER THE VOID</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // كود الشيدر المتقدم لإنشاء ثقب أسود واقعي (Interstellar Style)
        const fragmentShader = `
            uniform float time;
            uniform vec2 resolution;
            uniform float zoom;

            void main() {
                vec2 uv = (gl_FragCoord.xy - 0.5 * resolution.xy) / min(resolution.y, resolution.x);
                float r = length(uv);
                float angle = atan(uv.y, uv.x);
                
                // تشويه الفضاء حول الثقب الأسود
                float distort = 0.2 / (r + 0.01);
                float spiral = angle + distort * zoom + time * 0.5;
                
                // إنشاء قرص التراكم المتوهج
                float disk = smoothstep(0.4, 0.15, r) * smoothstep(0.1, 0.2, r);
                vec3 color = vec3(0.5, 0.0, 0.5) * disk * (1.0 + sin(spiral * 10.0));
                color += vec3(0.0, 0.8, 0.8) * disk * (1.0 + cos(spiral * 5.0));
                
                // قلب الثقب الأسود (العدم)
                float hole = smoothstep(0.12, 0.13, r);
                color *= hole;
                
                gl_FragColor = vec4(color, 1.0);
            }
        `;

        let scene, camera, renderer, material, mesh;
        let zoomVal = 1.0;
        let active = false;

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
            renderer = new THREE.WebGLRenderer();
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('canvas-container').appendChild(renderer.domElement);

            const geometry = new THREE.PlaneGeometry(2, 2);
            material = new THREE.ShaderMaterial({
                uniforms: {
                    time: { value: 0 },
                    resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
                    zoom: { value: 1.0 }
                },
                fragmentShader
            });

            mesh = new THREE.Mesh(geometry, material);
            scene.add(mesh);
            animate();
        }

        function startVortex() {
            active = true;
            document.getElementById('enter-btn').style.display = 'none';
            setTimeout(() => {
                document.getElementById('names').style.opacity = '1';
            }, 2000);
        }

        function animate(t) {
            material.uniforms.time.value = t * 0.001;
            if(active && material.uniforms.zoom.value < 50.0) {
                material.uniforms.zoom.value += 0.2;
            }
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }

        window.addEventListener('resize', () => {
            renderer.setSize(window.innerWidth, window.innerHeight);
            material.uniforms.resolution.value.set(window.innerWidth, window.innerHeight);
        });

        init();
    </script>
</body>
</html>
"""

components.html(black_hole_shader, height=900, scrolling=False)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)
