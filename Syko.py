import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO & YOUSRA | LIQUID VOID", layout="wide", initial_sidebar_state="collapsed")

# شيدر سينمائي عالي الجودة لضمان النعومة واختفاء المربعات
ultra_smooth_shader = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #000; overflow: hidden; }
        canvas { width: 100vw; height: 100vh; display: block; }
        
        #overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 10; opacity: 0; pointer-events: none; transition: opacity 3s;
            background: rgba(0,0,0,0.8);
        }
        .name {
            font-family: 'Arial Black', sans-serif; font-size: 8vw; color: white;
            letter-spacing: 1.5vw; text-shadow: 0 0 30px #0ff, 0 0 60px #f0f; margin: 0;
        }
        .inf { font-size: 10vw; color: #f0f; filter: drop-shadow(0 0 40px #f0f); }
        .active { opacity: 1 !important; pointer-events: all !important; }
    </style>
</head>
<body>
    <div id="overlay">
        <div class="name">SYKO</div>
        <div class="inf">∞</div>
        <div class="name">YOUSRA</div>
    </div>
    <canvas id="glCanvas"></canvas>

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
            
            // تشويه الزمكان (Vortex Distortion)
            float r = length(uv);
            float a = atan(uv.y, uv.x);
            
            // إضافة النعومة الفائقة عبر Sin & Cos مع تلاشي الحواف
            float s = sin(a * 3.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.02 / abs(r - 0.3 - s * 0.1 * transition);
            
            vec3 col = vec3(0.0, 0.8, 1.0) * glow; // Cyan base
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.5); // Magenta glow
            
            // قلب الثقب الأسود الناعم
            float hole = smoothstep(0.1 + transition*0.2, 0.15 + transition*0.3, r);
            col *= hole;
            
            gl_FragColor = vec4(col, 1.0);
        }
    </script>

    <script>
        const canvas = document.getElementById('glCanvas');
        const gl = canvas.getContext('webgl');
        
        let prog = gl.createProgram();
        function createShader(type, source) {
            let s = gl.createShader(type);
            gl.shaderSource(s, document.getElementById(source).text);
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

        window.addEventListener('mousedown', () => isPressed = true);
        window.addEventListener('touchstart', () => isPressed = true);

        function render(now) {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            gl.viewport(0, 0, canvas.width, canvas.height);
            
            if(isPressed && trans < 1.0) {
                trans += 0.01;
                if(trans >= 0.99) document.getElementById('overlay').classList.add('active');
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

components.html(ultra_smooth_shader, height=900, scrolling=False)

st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
