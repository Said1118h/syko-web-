import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="S", layout="wide", initial_sidebar_state="collapsed")

# كود الواجهة النقية: حرف S فقط مع الثقب الأسود التفاعلي
pure_s_void = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #000; overflow: hidden; cursor: none; }
        
        canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; }

        #ui {
            position: relative; z-index: 10; width: 100%; height: 100vh;
            display: flex; align-items: center; justify-content: center;
            pointer-events: none; opacity: 0;
            animation: fadeIn 3s forwards;
        }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        .flame-s {
            font-size: 30vw; font-family: 'Oswald', sans-serif;
            background: linear-gradient(to bottom, #fff, #ffea00, #ff4e00, #ff0055);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 50px #ff4e00);
            line-height: 0.8;
            animation: floatS 4s infinite alternate ease-in-out;
        }

        @keyframes floatS {
            from { transform: translateY(0) scale(1); filter: drop-shadow(0 0 30px #ff4e00); }
            to { transform: translateY(-20px) scale(1.05); filter: drop-shadow(0 0 70px #ffea00); }
        }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>
    <div id="ui">
        <div class="flame-s">S</div>
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
        void main() {
            vec2 uv = (gl_FragCoord.xy - 0.5 * res.xy) / min(res.y, res.x);
            vec2 m = (mouse.xy - 0.5 * res.xy) / min(res.y, res.x);
            float dist = length(uv - m);
            float ripple = smoothstep(0.3, 0.0, dist) * strength;
            uv += (uv - m) * ripple * 0.4;
            float r = length(uv);
            float s = sin(atan(uv.y, uv.x) * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.012 / abs(r - 0.35 - s * 0.05);
            vec3 col = vec3(0.0, 0.7, 1.0) * glow + vec3(1.0, 0.0, 0.4) * (glow * 0.5) + vec3(0.4, 1.0, 0.8) * ripple;
            gl_FragColor = vec4(col * smoothstep(0.1, 0.2, r), 1.0);
        }
    </script>

    <script>
        const canvas = document.getElementById('glCanvas');
        const gl = canvas.getContext('webgl');
        let prog = gl.createProgram();
        function createShader(type, id) {
            let s = gl.createShader(type);
            gl.shaderSource(s, document.getElementById(id).text);
            gl.compileShader(s); gl.attachShader(prog, s);
        }
        createShader(gl.VERTEX_SHADER, 'vs');
        createShader(gl.FRAGMENT_SHADER, 'fs');
        gl.linkProgram(prog); gl.useProgram(prog);
        const posLoc = gl.getAttribLocation(prog, 'position');
        const posBuf = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,1,1,1,-1,-1,1,-1]), gl.STATIC_DRAW);
        gl.enableVertexAttribArray(posLoc);
        gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

        let strength = 0, mx = 0, my = 0;
        window.addEventListener('mousemove', (e) => { mx = e.clientX; my = window.innerHeight - e.clientY; strength = 0.6; });
        window.addEventListener('touchmove', (e) => { mx = e.touches[0].clientX; my = window.innerHeight - e.touches[0].clientY; strength = 0.6; });

        function render(now) {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
