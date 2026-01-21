import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO | GHOST RIPPLE", layout="wide", initial_sidebar_state="collapsed")

# تعريف كود الجرافيكس والتفاعل
vortex_final_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono:wght@300&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Syncopate', sans-serif; cursor: none; }
        canvas { width: 100vw; height: 100vh; display: block; }
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
        #second-page {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: #000; z-index: 500;
            display: none; flex-direction: column; align-items: center; justify-content: center;
            opacity: 0; transition: 1s;
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
        <div style="border:1px solid #0ff; padding:50px; text-align:center;">
            <a href="https://www.instagram.com/s1x.s9" target="_blank" style="text-decoration:none; color:#fff; font-size:24px; letter-spacing:5px;">@S1X.S9</a>
            <div style="font-family:'JetBrains Mono'; color:#0ff; font-size:10px; margin-top:20px; opacity:0.5;">REALITY STABILIZED</div>
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
            float ripple = smoothstep(0.15, 0.0, distToMouse) * strength;
            uv += (uv - m) * ripple * 0.8;
            float r = length(uv);
            float a = atan(uv.y, uv.x);
            float s = sin(a * 4.0 + time + 1.0/r) * 0.5 + 0.5;
            float glow = 0.012 / abs(r - 0.3 - s * 0.08 * transition);
            vec3 col = vec3(0.0, 0.8, 1.0) * glow;
            col += vec3(1.0, 0.0, 1.0) * (glow * 0.4);
            col += vec3(0.5, 1.0, 1.0) * (ripple * 2.0);
            float hole = smoothstep(0.1 + transition*0.5, 0.15 + transition*0.8, r);
            gl_FragColor = vec4(col * hole * (1.0 - transition*0.8), 1.0);
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
        create
