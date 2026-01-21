import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO | THE TERMINAL", layout="wide", initial_sidebar_state="collapsed")

final_god_level = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=JetBrains+Mono:wght@300&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; }
        canvas { width: 100vw; height: 100vh; display: block; }
        
        /* شاشة الأسماء - الانتقال السلس */
        #reveal-layer {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 100; opacity: 0; pointer-events: none; transition: 1.5s ease-in-out;
        }
        .name { font-size: 8vw; color: white; letter-spacing: 2vw; text-shadow: 0 0 30px #0ff; margin: 0; }
        .inf { font-size: 10vw; color: #f0f; filter: drop-shadow(0 0 40px #f0f); }
        
        #core-btn {
            margin-top: 30px; padding: 12px 35px; background: none; 
            border: 1px solid rgba(0, 255, 255, 0.5); color: #0ff; font-family: 'Syncopate';
            letter-spacing: 5px; cursor: pointer; transition: 0.5s; font-size: 10px;
            opacity: 0; pointer-events: none;
        }
        #core-btn:hover { background: #0ff; color: #000; box-shadow: 0 0 30px #0ff; }

        /* الصفحة الثانية - الـ Cyber Terminal */
        #second-page {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: #000; z-index: 500;
            display: none; flex-direction: column; align-items: center; justify-content: center;
            opacity: 0; transition: 1s;
        }

        .terminal-container {
            position: relative; width: 320px; height: 320px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            border: 1px solid rgba(0, 255, 255, 0.1);
        }

        /* زوايا رقمية متطورة */
        .corner { position: absolute; width: 20px; height: 20px; border: 2px solid #0ff; }
        .top-l { top: -2px; left: -2px; border-right: none; border-bottom: none; }
        .top-r { top: -2px; right: -2px; border-left: none; border-bottom: none; }
        .bot-l { bottom: -2px; left: -2px; border-right: none; border-top: none; }
        .bot-r { bottom: -2px; right: -2px; border-left: none; border-top: none; }

        .insta-id {
            text-decoration: none; color: #fff; font-size: 24px;
            letter-spacing: 5px; z-index: 10; text-align: center;
        }
        
        .status-tag {
            font-family: 'JetBrains Mono'; font-size: 10px; color: #0ff;
            opacity: 0.5; margin-bottom: 20px; letter-spacing: 2px;
        }

        .pulse-line {
            width: 100px; height: 1px; background: #0ff; margin-top: 30px;
            box-shadow: 0 0 15px #0ff; animation: pulseWidth 2s infinite;
        }
        @keyframes pulseWidth { 0%, 100% { width: 50px; opacity: 0.2; } 50% { width: 150px; opacity: 1; } }

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
        <button id="core-btn" onclick="openSecondPage()">INITIATE LINK</button>
    </div>

    <div id="second-page">
        <div class="terminal-container">
            <div class="corner top-l"></div><div class="corner top-r"></div>
            <div class="corner bot-l"></div><div class="corner bot-r"></div>
            
            <div class="status-tag">SIGNAL DETECTED</div>
            <a href="https://www.instagram.com/s1x.s9" target="_blank" class="insta-id">
                @S1X.S9
            </a>
            <div class="pulse-line"></div>
            <div class="status-tag" style="margin-top:20px; margin-bottom:0;">ENCRYPTED IDENTITY</div>
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
        uniform float transition;
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            float r = length(uv);
            float a = atan(uv.y, uv.x);
            float s = sin(a * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.015 / abs(r - 0.3 - s * 0.08 * transition);
            vec3 col = vec3(0.0, 0.8, 1.0) * glow;
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.4);
            float hole = smoothstep(0.1 + transition*0.5, 0.15 + transition*0.8, r);
            gl_FragColor = vec4(col * hole * (1.0-transition*0.8), 1.0);
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

        let trans = 0; let isPressed = false;

        window.addEventListener('mousedown', () => {
            if(!isPressed) {
                isPressed = true;
                setTimeout(() => {
                    document.getElementById('core-btn').style.opacity = "1";
                    document.getElementById('core-btn').style.pointerEvents = "all";
                }, 2000);
            }
        });

        function openSecondPage() {
            // إخفاء الصفحة الأولى تماماً قبل إظهار الثانية
            document.getElementById('reveal-layer').style.display = 'none';
            document.getElementById('second-page').classList.add('show-page');
        }

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            if(isPressed && trans < 1.0) {
                trans += 0.006;
                if(trans >= 0.8) document.getElementById('reveal-layer').classList.add('active');
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

components.html(final_god_level, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
