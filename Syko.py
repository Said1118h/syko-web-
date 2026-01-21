import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | HOLO-LINK", layout="wide", initial_sidebar_state="collapsed")

# كود الجرافيكس مع صفحة الإنستغرام بمستوى الهولوغرام
hologram_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Orbitron:wght@500&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; }
        canvas { width: 100vw; height: 100vh; display: block; filter: blur(0.5px); }
        
        #reveal-layer {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 100; opacity: 0; pointer-events: none; transition: 2s ease-in-out;
        }
        .name { font-size: 8vw; color: white; letter-spacing: 2vw; text-shadow: 0 0 30px #0ff; margin: 0; }
        .inf { font-size: 10vw; color: #f0f; filter: drop-shadow(0 0 40px #f0f); }
        
        #core-btn {
            margin-top: 30px; padding: 15px 40px; background: none; 
            border: 1px solid #0ff; color: #0ff; font-family: 'Syncopate';
            letter-spacing: 5px; cursor: pointer; transition: 0.5s;
            opacity: 0; pointer-events: none;
        }

        /* --- صفحة الهولوغرام المتطورة --- */
        #second-page {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.9); z-index: 500;
            display: none; flex-direction: column; align-items: center; justify-content: center;
            opacity: 0; transition: 1s;
        }
        
        .hologram-frame {
            position: relative; padding: 60px;
            background: rgba(0, 255, 255, 0.03);
            border-left: 2px solid #0ff; border-right: 2px solid #0ff;
            box-shadow: inset 0 0 50px rgba(0, 255, 255, 0.1), 0 0 30px rgba(0, 255, 255, 0.1);
            clip-path: polygon(10% 0, 90% 0, 100% 20%, 100% 80%, 90% 100%, 10% 100%, 0 80%, 0 20%);
            animation: holo-float 4s infinite ease-in-out;
        }

        @keyframes holo-float { 
            0%, 100% { transform: translateY(0) scale(1); } 
            50% { transform: translateY(-15px) scale(1.02); } 
        }

        .scanner {
            position: absolute; top: 0; left: 0; width: 100%; height: 5px;
            background: #0ff; box-shadow: 0 0 20px #0ff;
            animation: scan 3s infinite linear; opacity: 0.5;
        }
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }

        .insta-id {
            font-size: 45px; color: #fff; text-decoration: none;
            letter-spacing: 8px; position: relative; z-index: 10;
            display: flex; flex-direction: column; align-items: center; gap: 20px;
        }
        
        .insta-id span { font-family: 'Orbitron'; font-size: 14px; color: #0ff; opacity: 0.7; }

        .glitch-link:hover {
            animation: glitch 0.3s infinite;
            text-shadow: 2px 0 #f0f, -2px 0 #0ff;
        }
        @keyframes glitch {
            0% { transform: translate(0); }
            20% { transform: translate(-3px, 2px); }
            40% { transform: translate(3px, -2px); }
            100% { transform: translate(0); }
        }

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
        <div class="hologram-frame">
            <div class="scanner"></div>
            <a href="https://www.instagram.com/s1x.s9" target="_blank" class="insta-id glitch-link">
                <span>ENCRYPTED IDENTITY</span>
                @s1x.s9
                <span style="font-size: 10px; margin-top:20px; border:1px solid #0ff; padding:5px 15px;">ESTABLISH CONNECTION</span>
            </a>
        </div>
        <p style="color:rgba(0,255,255,0.3); margin-top:40px; font-size:10px; letter-spacing:10px;">AUTHORIZED ACCESS ONLY</p>
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
            float glow = 0.02 / abs(r - 0.3 - s * 0.1 * transition);
            vec3 col = vec3(0.0, 0.8, 1.0) * glow;
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.4);
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
                }, 2000);
            }
        });

        function openSecondPage() {
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

components.html(hologram_code, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
