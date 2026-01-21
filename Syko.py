import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO S | SMOOTH VOID", layout="wide", initial_sidebar_state="collapsed")

smooth_void_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Syncopate:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; cursor: none; }
        
        canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; }

        #content-layer {
            position: relative; z-index: 10; width: 100%; height: 100vh;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            pointer-events: none;
        }

        /* حاوية الأسماء - تختفي تدريجياً */
        .intro-ui {
            position: absolute; display: flex; align-items: center; gap: 20px;
            transition: opacity 2s ease, transform 2s ease;
        }
        .n-text { font-size: 5vw; color: white; letter-spacing: 1.5vw; text-shadow: 0 0 20px #0ff; }
        .inf-icon { font-size: 6vw; color: #f0f; animation: rot 4s linear infinite; }

        /* حاوية SYKO S - تظهر تدريجياً */
        .final-ui {
            position: absolute; display: flex; flex-direction: column; align-items: center;
            opacity: 0; transform: scale(0.8);
            transition: opacity 2.5s ease, transform 2.5s ease;
        }
        .flame-s {
            font-size: 22vw; font-family: 'Oswald', sans-serif;
            background: linear-gradient(to bottom, #ffea00, #ff4e00, #ff0055);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 40px #ff4e00);
            line-height: 0.8;
        }
        .syko-s-label { font-size: 3vw; color: #fff; letter-spacing: 25px; margin-top: 10px; opacity: 0.8; }

        @keyframes rot { from {transform: rotate(0deg);} to {transform: rotate(360deg);} }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>

    <div id="content-layer">
        <div class="intro-ui" id="intro">
            <span class="n-text">SYKO</span>
            <span class="inf-icon">∞</span>
            <span class="n-text">YOUSRA</span>
        </div>

        <div class="final-ui" id="final">
            <div class="flame-s">S</div>
            <h1 class="syko-s-label">SYKO S</h1>
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
        uniform float progress; // معامل التداخل الانسيابي
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            vec2 m = (mouse.xy - 0.5 * res.xy) / min(res.y, res.x);
            
            float dist = length(uv - m);
            float ripple = smoothstep(0.25, 0.0, dist) * strength;
            uv += (uv - m) * ripple * 0.4;

            float r = length(uv);
            float s = sin(atan(uv.y, uv.x) * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.015 / abs(r - 0.3 - s * 0.08 * progress);
            
            vec3 col = vec3(0.0, 0.8, 1.0) * glow; 
            col += vec3(1.0, 0.0, 0.5) * (glow * 0.5);
            col += vec3(0.5, 1.0, 0.9) * ripple;

            gl_FragColor = vec4(col * smoothstep(0.1 + progress*0.4, 0.15 + progress*0.7, r), 1.0);
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

        let progress = 0, isInteracting = false, strength = 0, mx = 0, my = 0;

        function startInteraction() {
            if(!isInteracting) {
                isInteracting = true;
                // تداخل سموذ: اختفاء الأول وظهور الثاني
                document.getElementById('intro').style.opacity = '0';
                document.getElementById('intro').style.transform = 'scale(1.2) blur(10px)';
                setTimeout(() => {
                    const final = document.getElementById('final');
                    final.style.opacity = '1';
                    final.style.transform = 'scale(1)';
                }, 1000);
            }
        }

        window.addEventListener('mousemove', (e) => { 
            mx = e.clientX; my = window.innerHeight - e.clientY; 
            strength = 0.6; 
            if(strength > 0.1) startInteraction(); 
        });
        
        window.addEventListener('touchmove', (e) => { 
            mx = e.touches[0].clientX; my = window.innerHeight - e.touches[0].clientY; 
            strength = 0.6; 
            startInteraction(); 
        });

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            if(isInteracting && progress < 1.0) progress += 0.004;
            strength *= 0.94;

            gl.uniform1f(gl.getUniformLocation(prog, 'time'), now * 0.001);
            gl.uniform2f(gl.getUniformLocation(prog, 'res'), canvas.width, canvas.height);
            gl.uniform2f(gl.getUniformLocation(prog, 'mouse'), mx, my);
            gl.uniform1f(gl.getUniformLocation(prog, 'strength'), strength);
            gl.uniform1f(gl.getUniformLocation(prog, 'progress'), progress);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
            requestAnimationFrame(render);
        }
        requestAnimationFrame(render);
    </script>
</body>
</html>
"""

components.html(smooth_void_code, height=900, scrolling=False)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
