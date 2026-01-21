import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO S | THE ULTIMATE VOID", layout="wide", initial_sidebar_state="collapsed")

# الكود الجامع لكل التأثيرات
master_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Syncopate:wght@700&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; cursor: crosshair; }
        canvas { width: 100vw; height: 100vh; display: block; position: fixed; top:0; left:0; z-index:1; }
        
        #ui-layer { position: relative; z-index: 10; width: 100%; height: 100vh; pointer-events: none; }

        /* شاشة البداية: SYKO & YOUSRA */
        #reveal-layer {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            opacity: 0; transition: 2s ease-in-out;
        }
        .name-wrapper { display: flex; align-items: center; gap: 30px; }
        .name { font-size: 6vw; color: white; letter-spacing: 1.5vw; text-shadow: 0 0 20px #0ff; }
        .inf { font-size: 8vw; color: #f0f; filter: drop-shadow(0 0 30px #f0f); animation: spin 5s linear infinite; }
        @keyframes spin { from {transform: rotate(0deg);} to {transform: rotate(360deg);} }

        #core-btn {
            margin-top: 40px; padding: 15px 40px; background: none; 
            border: 1px solid #0ff; color: #0ff; font-family: 'Syncopate';
            letter-spacing: 5px; cursor: pointer; transition: 0.5s; font-size: 12px;
            opacity: 0; pointer-events: none;
        }
        #core-btn:hover { background: #0ff; color: #000; box-shadow: 0 0 40px #0ff; }

        /* الواجهة النهائية: SYKO S */
        #final-interface {
            display: none; flex-direction: column; align-items: center; justify-content: center;
            height: 100vh; opacity: 0; transition: 1.5s;
        }
        .s-logo {
            font-size: 20vw; font-family: 'Oswald', sans-serif;
            background: linear-gradient(to bottom, #ffea00, #ff0055);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 30px #ff0055);
            animation: pulse 2s infinite alternate;
        }
        @keyframes pulse { from {transform: scale(1);} to {transform: scale(1.05);} }
        
        .syko-s-text { font-size: 4vw; color: #fff; letter-spacing: 15px; margin-top: -30px; }

        .active { opacity: 1 !important; pointer-events: all !important; }
        .show-flex { display: flex !important; opacity: 1 !important; pointer-events: all !important; }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>

    <div id="ui-layer">
        <div id="reveal-layer">
            <div class="name-wrapper">
                <div class="name">SYKO</div>
                <div class="inf">∞</div>
                <div class="name">YOUSRA</div>
            </div>
            <button id="core-btn" onclick="goToFinal()">INITIATE LINK</button>
        </div>

        <div id="final-interface">
            <div class="s-logo">S</div>
            <div class="syko-s-text">SYKO S</div>
            <a href="https://www.instagram.com/s1x.s9" target="_blank" 
               style="margin-top:40px; color:#0ff; text-decoration:none; border:1px solid #0ff; padding:10px 30px; font-size:10px; letter-spacing:3px;">
               FOLLOW THE VOID
            </a>
        </div>
    </div>

    <script id="vs" type="f">
        attribute vec2 position;
        void main() { gl_Position = vec4(position, 0.0, 1.0); }
    </script>

    <script id="fs" type="f">
        precision highp float;
        uniform float time;
        uniform vec2 res;
        uniform vec2 mouse;
        uniform float strength;
        uniform float transition;
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            vec2 m = (mouse.xy - 0.5 * res.xy) / min(res.y, res.x);
            
            float distToMouse = length(uv - m);
            float ripple = smoothstep(0.2, 0.0, distToMouse) * strength;
            uv += (uv - m) * ripple * 0.5;

            float r = length(uv);
            float a = atan(uv.y, uv.x);
            float s = sin(a * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.015 / abs(r - 0.3 - s * 0.08 * transition);
            
            vec3 col = vec3(0.0, 0.8, 1.0) * glow;
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.4);
            col += vec3(0.0, 1.0, 1.0) * (ripple * 3.0);

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

        const posLoc = gl.getAttribLocation(prog, 'position');
        const posBuf = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,1,1,1,-1,-1,1,-1]), gl.STATIC_DRAW);
        gl.enableVertexAttribArray(posLoc);
        gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

        let trans = 0, isPressed = false, strength = 0, mouseX = 0, mouseY = 0;

        window.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = window.innerHeight - e.clientY; strength = 0.6; });
        window.addEventListener('mousedown', () => {
            if(!isPressed) {
                isPressed = true;
                setTimeout(() => {
                    document.getElementById('reveal-layer').classList.add('active');
                    document.getElementById('core-btn').classList.add('active');
                }, 1000);
            }
        });

        function goToFinal() {
            document.getElementById('reveal-layer').style.display = 'none';
            document.getElementById('final-interface').classList.add('show-flex');
        }

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            if(isPressed && trans < 1.0) trans += 0.005;
            strength *= 0.94;

            gl.uniform1f(gl.getUniformLocation(prog, 'time'), now * 0.001);
            gl.uniform2f(gl.getUniformLocation(prog, 'res'), canvas.width, canvas.height);
            gl.uniform2f(gl.getUniformLocation(prog, 'mouse'), mouseX, mouseY);
            gl.uniform1f(gl.getUniformLocation(prog, 'strength'), strength);
            gl.uniform1f(gl.getUniformLocation(prog, 'transition'), trans);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);
    </script>
</body>
</html>
"""

components.html(master_code, height=900, scrolling=False)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
