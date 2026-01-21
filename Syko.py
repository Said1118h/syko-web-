import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO S | THE VOID", layout="wide", initial_sidebar_state="collapsed")

# كود يجمع الثقب الأسود، التفاعل، وشعار S الناري بنظام الطبقات المنفصلة
master_piece = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Syncopate:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; cursor: crosshair; }
        
        /* محرك الجرافيكس (الثقب الأسود) */
        canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; }

        /* طبقة المحتوى */
        #ui-wrapper {
            position: relative; z-index: 10; width: 100%; height: 100vh;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            pointer-events: none;
        }

        /* المرحلة 1: الأسماء الافتتاحية */
        #intro-layer {
            display: flex; flex-direction: column; align-items: center;
            transition: 1.5s ease; opacity: 0;
        }

        .names { display: flex; align-items: center; gap: 20px; margin-bottom: 30px; }
        .n-text { font-size: 5vw; color: white; letter-spacing: 1vw; text-shadow: 0 0 20px #0ff; }
        .inf-icon { font-size: 6vw; color: #f0f; animation: rotate 4s linear infinite; }
        @keyframes rotate { from {transform: rotate(0deg);} to {transform: rotate(360deg);} }

        /* المرحلة 2: شعار S المشتعل (SYKO S) */
        #final-layer {
            display: none; flex-direction: column; align-items: center;
            opacity: 0; transition: 1.5s;
        }

        .flame-s {
            font-size: 18vw; font-family: 'Oswald', sans-serif;
            background: linear-gradient(to bottom, #ffea00, #ff4e00, #ff0055);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 30px #ff4e00);
            line-height: 1; position: relative;
        }

        .syko-s-title { 
            font-size: 3vw; color: #fff; letter-spacing: 20px; 
            margin-top: -20px; text-shadow: 0 0 10px #000;
        }

        /* الأزرار */
        .btn {
            margin-top: 40px; padding: 12px 40px; background: none;
            border: 1px solid #0ff; color: #0ff; font-family: 'Syncopate';
            letter-spacing: 5px; cursor: pointer; pointer-events: all;
            transition: 0.4s; font-size: 10px; text-decoration: none;
        }
        .btn:hover { background: #0ff; color: #000; box-shadow: 0 0 30px #0ff; }

        .visible { opacity: 1 !important; pointer-events: all !important; }
        @keyframes pulseS { from {transform: scale(1);} to {transform: scale(1.05);} }
        .flame-s { animation: pulseS 2s infinite alternate; }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>

    <div id="ui-wrapper">
        <div id="intro-layer">
            <div class="names">
                <span class="n-text">SYKO</span>
                <span class="inf-icon">∞</span>
                <span class="n-text">YOUSRA</span>
            </div>
            <button class="btn" onclick="activateS()">INITIATE LINK</button>
        </div>

        <div id="final-layer">
            <div class="flame-s">S</div>
            <h1 class="syko-s-title">SYKO S</h1>
            <a href="https://www.instagram.com/s1x.s9" target="_blank" class="btn">FOLLOW THE VOID</a>
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
        uniform float trans;
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            vec2 m = (mouse.xy - 0.5 * res.xy) / min(res.y, res.x);
            
            float dist = length(uv - m);
            float ripple = smoothstep(0.2, 0.0, dist) * strength;
            uv += (uv - m) * ripple * 0.5;

            float r = length(uv);
            float s = sin(atan(uv.y, uv.x) * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.015 / abs(r - 0.3 - s * 0.08 * trans);
            
            vec3 col = vec3(0.0, 0.7, 1.0) * glow; // Cyan
            col += vec3(1.0, 0.0, 0.5) * (glow * 0.4); // Magenta
            col += vec3(0.0, 1.0, 0.8) * ripple; // Interaction

            gl_FragColor = vec4(col * smoothstep(0.1 + trans*0.5, 0.15 + trans*0.8, r), 1.0);
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

        let trans = 0, isStarted = false, strength = 0, mx = 0, my = 0;

        window.addEventListener('mousemove', (e) => { mx = e.clientX; my = window.innerHeight - e.clientY; strength = 0.6; });
        window.addEventListener('mousedown', () => {
            if(!isStarted) {
                isStarted = true;
                document.getElementById('intro-layer').classList.add('visible');
            }
        });

        function activateS() {
            document.getElementById('intro-layer').style.display = 'none';
            const final = document.getElementById('final-layer');
            final.style.display = 'flex';
            setTimeout(() => final.classList.add('visible'), 50);
        }

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            if(isStarted && trans < 1.0) trans += 0.005;
            strength *= 0.94;

            gl.uniform1f(gl.getUniformLocation(prog, 'time'), now * 0.001);
            gl.uniform2f(gl.getUniformLocation(prog, 'res'), canvas.width, canvas.height);
            gl.uniform2f(gl.getUniformLocation(prog, 'mouse'), mx, my);
            gl.uniform1f(gl.getUniformLocation(prog, 'strength'), strength);
            gl.uniform1f(gl.getUniformLocation(prog, 'trans'), trans);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);
    </script>
</body>
</html>
"""

components.html(master_piece, height=900, scrolling=False)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
