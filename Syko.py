import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | THE CORE", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس المطور مع صفحة الإنستغرام
final_pro_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Syncopate:wght@700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Orbitron', sans-serif; }
        canvas { width: 100vw; height: 100vh; display: block; }
        
        #reveal-layer {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 100; opacity: 0; pointer-events: none; transition: 2s ease-in-out;
        }
        .name { font-size: 8vw; color: white; letter-spacing: 2vw; text-shadow: 0 0 30px #0ff; margin: 0; }
        .inf { font-size: 10vw; color: #f0f; filter: drop-shadow(0 0 40px #f0f); }
        
        #core-btn {
            margin-top: 30px; padding: 15px 40px; background: none; 
            border: 2px solid #0ff; color: #0ff; font-family: 'Syncopate';
            letter-spacing: 5px; cursor: pointer; transition: 0.5s;
            opacity: 0; pointer-events: none;
        }
        #core-btn:hover { background: #0ff; color: #000; box-shadow: 0 0 50px #0ff; }

        /* الصفحة الثانية - التصميم العالمي */
        #second-page {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, #0a0a0a 0%, #000 100%); z-index: 500;
            display: none; flex-direction: column; align-items: center; justify-content: center;
            opacity: 0; transition: 1.5s;
        }
        
        .insta-card {
            padding: 40px; border: 1px solid rgba(0, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.02); border-radius: 20px;
            text-align: center; backdrop-filter: blur(10px);
        }

        .insta-link {
            font-size: 30px; color: #fff; text-decoration: none;
            font-family: 'Syncopate'; letter-spacing: 3px;
            display: flex; align-items: center; gap: 15px;
            transition: 0.3s;
        }
        .insta-link:hover { color: #ff00ff; text-shadow: 0 0 20px #ff00ff; transform: translateY(-5px); }

        .active { opacity: 1 !important; pointer-events: all !important; }
        .show-page { display: flex !important; opacity: 1 !important; }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>

    <div id="reveal-layer">
        <div class="name">SYKO</div>
        <div class="inf">∞</div>
        <div class="name">YOUSRA</div>
        <button id="core-btn" onclick="openSecondPage()">CONNECT</button>
    </div>

    <div id="second-page">
        <div class="insta-card">
            <h2 style="color:#0ff; letter-spacing:10px; margin-bottom:40px;">PRIVATE ACCESS</h2>
            <a href="https://www.instagram.com/s1x.s9" target="_blank" class="insta-link">
                <span style="font-size:40px;">📸</span> @s1x.s9
            </a>
            <p style="color:#555; margin-top:30px; font-size:12px; letter-spacing:2px;">CLICK TO FOLLOW THE JOURNEY</p>
        </div>
        <button onclick="location.reload()" style="background:none; border:none; color:#333; margin-top:50px; cursor:pointer; font-size:10px; letter-spacing:5px;">BACK TO VOID</button>
    </div>

    <script id="vs" type="f">
        attribute vec2 position;
        void main() { gl_Position = vec4(position, 0.0, 1.0); }
    </script>

    <script id="fs" type="f">
        precision highp float;
        uniform float time;
        uniform vec2 res;
        uniform float transition;
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            float r = length(uv);
            float a = atan(uv.y, uv.x);
            float s = sin(a * 3.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.02 / abs(r - 0.3 - s * 0.1 * transition);
            vec3 col = vec3(0.0, 0.8, 1.0) * glow;
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.5);
            float hole = smoothstep(0.1 + transition*0.5, 0.15 + transition*0.8, r);
            gl_FragColor = vec4(col * hole, 1.0);
        }
    </script>

    <script>
        const canvas = document.getElementById('glCanvas');
        const gl = canvas.getContext('webgl');
        let prog = gl.createProgram();
        
        function createShader(type, id) {
            let s = gl.createShader(type);
            gl.shaderSource(s, document.getElementById(id).text);
            gl.compileShader(s);
            gl.attachShader(prog, s);
        }
        createShader(gl.VERTEX_SHADER, 'vs');
        createShader(gl.FRAGMENT_SHADER, 'fs');
        gl.linkProgram(prog);
        gl.useProgram(prog);

        const posBuf = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,1,1,1,-1,-1,1,-1]), gl.STATIC_DRAW);
        const posLoc = gl.getAttribLocation(prog, 'position');
        gl.enableVertexAttribArray(posLoc);
        gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

        let trans = 0;
        let isPressed = false;

        window.addEventListener('mousedown', () => {
            if(!isPressed) {
                isPressed = true;
                setTimeout(() => {
                    document.getElementById('core-btn').style.opacity = "1";
                    document.getElementById('core-btn').style.pointerEvents = "all";
                }, 2500);
            }
        });

        function openSecondPage() {
            document.getElementById('second-page').classList.add('show-page');
        }

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            if(isPressed && trans < 1.0) {
                trans += 0.005;
                if(trans >= 0.85) document.getElementById('reveal-layer').classList.add('active');
            }
            gl.uniform1f(gl.getUniformLocation(prog, 'time'), now * 0.001);
            gl.uniform2f(gl.getUniformLocation(prog, 'res'), canvas.width, canvas.height);
            gl.uniform1f(gl.getUniformLocation(prog, 'transition'), trans);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);
    </script>
</body>
</html>
"""

components.html(final_pro_code, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
