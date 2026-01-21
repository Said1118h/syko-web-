import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO BOOSTER", layout="wide")

full_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-database.js"></script>
    <style>
        body { background: #000; color: white; font-family: sans-serif; overflow: hidden; }
        canvas { position: fixed; top: 0; left: 0; z-index: 1; }
        #ui { position: relative; z-index: 10; display: flex; align-items: center; justify-content: center; height: 100vh; }
        .box { background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 30px; border-radius: 20px; border: 1px solid #0ff; text-align: center; width: 320px; }
        button { width: 100%; padding: 12px; background: #0ff; border: none; font-weight: bold; cursor: pointer; margin-top: 10px; }
    </style>
</head>
<body>
    <canvas id="glCanvas"></canvas>
    <div id="ui">
        <div class="box">
            <h2>COINS: <span id="coins">0</span></h2>
            <div id="login">
                <input type="text" id="user" placeholder="Username" style="width:100%; padding:10px; margin-top:10px;">
                <button onclick="login()">START</button>
            </div>
            <div id="actions" style="display:none;">
                <button onclick="follow()">FOLLOW @S1X.S9 (+10)</button>
                <button onclick="claim()" style="background:#f0f;">REDEEM 100</button>
            </div>
        </div>
    </div>
    <script>
        const firebaseConfig = {
            apiKey: "AIzaSyAbrrwnTAYVa-z83G9plOfieP4bm1rxDtA",
            authDomain: "syko-booster.firebaseapp.com",
            projectId: "syko-booster",
            storageBucket: "syko-booster.firebasestorage.app",
            messagingSenderId: "53373305140",
            appId: "1:53373305140:web:0b69db40be835905206561",
            databaseURL: "https://syko-booster-default-rtdb.firebaseio.com"
        };
        firebase.initializeApp(firebaseConfig);
        const db = firebase.database();
        let myUser = "";

        function login() {
            myUser = document.getElementById('user').value.trim().toLowerCase();
            if(!myUser) return;
            db.ref('users/' + myUser).on('value', (s) => {
                let val = s.val() ? s.val().coins : 0;
                if(!s.exists()) db.ref('users/' + myUser).set({coins: 0});
                document.getElementById('coins').innerText = val;
                document.getElementById('login').style.display = 'none';
                document.getElementById('actions').style.display = 'block';
            });
        }
        function follow() {
            window.open('https://www.instagram.com/s1x.s9', '_blank');
            db.ref('users/' + myUser).once('value', (s) => {
                db.ref('users/' + myUser).update({coins: (s.val().coins || 0) + 10});
            });
        }
        function claim() {
            db.ref('users/' + myUser).once('value', (s) => {
                if(s.val().coins >= 100) {
                    db.ref('users/' + myUser).update({coins: s.val().coins - 100});
                    db.ref('orders').push({user: myUser, time: Date.now()});
                    alert("Order Sent!");
                } else { alert("Need 100!"); }
            });
        }
        // Black Hole Animation
        const canvas = document.getElementById('glCanvas');
        const gl = canvas.getContext('webgl');
        const vs = `attribute vec2 p; void main(){gl_Position=vec4(p,0,1);}`;
        const fs = `precision highp float; uniform float t; uniform vec2 r; void main(){vec2 uv=(gl_FragCoord.xy-.5*r)/min(r.y,r.x); float d=length(uv); float s=sin(atan(uv.y,uv.x)*4.+t+1./d)*.5+.5; float g=.01/abs(d-.35-s*.05); gl_FragColor=vec4(vec3(0,.8,1)*g,1);}`;
        const pr = gl.createProgram();
        function cS(t,s){let sh=gl.createShader(t);gl.shaderSource(sh,s);gl.compileShader(sh);gl.attachShader(pr,sh);}
        cS(gl.VERTEX_SHADER,vs); cS(gl.FRAGMENT_SHADER,fs); gl.linkProgram(pr); gl.useProgram(pr);
        const b=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,b); gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,1,1,1,-1,-1,1,-1]),gl.STATIC_DRAW);
        const p=gl.getAttribLocation(pr,'p'); gl.enableVertexAttribArray(p); gl.vertexAttribPointer(p,2,gl.FLOAT,0,0,0);
        function draw(n){
            canvas.width=window.innerWidth; canvas.height=window.innerHeight; gl.viewport(0,0,canvas.width,canvas.height);
            gl.uniform1f(gl.getUniformLocation(pr,'t'),n*0.001); gl.uniform2f(gl.getUniformLocation(pr,'r'),canvas.width,canvas.height);
            gl.drawArrays(gl.TRIANGLE_STRIP,0,4); requestAnimationFrame(draw);
        }
        requestAnimationFrame(draw);
    </script>
</body>
</html>
"""

components.html(full_code, height=800)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)
