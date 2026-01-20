import streamlit as st
import streamlit.components.v1 as components

# إعدادات النظام الاحترافي
st.set_page_config(page_title="SYKO & YOUSRA OS", layout="wide", initial_sidebar_state="collapsed")

# إدارة الصفحات
if "current_page" not in st.session_state:
    st.session_state.current_page = "HOME"

# --- 1. كود الخلفية والتفاعل (JavaScript & CSS) ---
core_ui = """
<style>
    body { margin: 0; background: #000; color: #fff; font-family: 'Segoe UI', sans-serif; overflow: hidden; }
    canvas { position: fixed; top: 0; left: 0; z-index: -1; }
    
    /* تأثير التشويش PRO */
    .glitch-box {
        text-align: center; margin-top: 5vh;
    }
    .name {
        font-size: 80px; font-weight: 900; letter-spacing: 15px;
        text-transform: uppercase; position: relative;
        text-shadow: 2px 2px #ff00ff, -2px -2px #00ffff;
        animation: glitch 1s infinite;
    }
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    .sub-text { color: #00ffff; letter-spacing: 5px; font-size: 15px; margin-top: 10px; }
</style>
<canvas id="canvas"></canvas>
<div class="glitch-box">
    <div class="name">SYKO <span style="color:#ff00ff">✕</span> YOUSRA</div>
    <div class="sub-text">NEXT-GEN DIGITAL INTERFACE</div>
</div>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    let particles = [];
    window.addEventListener('mousemove', (e) => {
        for (let i = 0; i < 2; i++) particles.push(new P(e.x, e.y));
    });
    class P {
        constructor(x, y) {
            this.x = x; this.y = y;
            this.size = Math.random() * 4 + 1;
            this.spX = Math.random() * 2 - 1;
            this.spY = Math.random() * 2 - 1;
            this.color = Math.random() > 0.5 ? '#ff00ff' : '#00ffff';
        }
        update() { this.x += this.spX; this.y += this.spY; if(this.size > 0.1) this.size -= 0.05; }
        draw() { ctx.fillStyle = this.color; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill(); }
    }
    function anim() {
        ctx.fillStyle = 'rgba(0,0,0,0.1)'; ctx.fillRect(0,0,canvas.width,canvas.height);
        particles.forEach((p, i) => { p.update(); p.draw(); if(p.size<=0.1) particles.splice(i,1); });
        requestAnimationFrame(anim);
    }
    anim();
</script>
"""

# عرض الهيدر المتفاعل
components.html(core_ui, height=300)

# --- 2. القائمة الاحترافية (Navigation) ---
st.markdown("""
<style>
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #00ffff !important;
        color: #00ffff !important;
        border-radius: 5px !important;
        transition: 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        background: #00ffff !important;
        color: #000 !important;
        box-shadow: 0 0 20px #00ffff;
    }
</style>
""", unsafe_allow_html=True)

nav_col = st.columns(3)
with nav_col[0]:
    if st.button("🌌 THE CORE"): st.session_state.current_page = "HOME"
with nav_col[1]:
    if st.button("📂 THE VAULT"): st.session_state.current_page = "VAULT"
with nav_col[2]:
    if st.button("📟 STATUS"): st.session_state.current_page = "STATUS"

st.write("---")

# --- 3. محتوى الصفحات الـ PRO ---

if st.session_state.current_page == "HOME":
    st.markdown("""
    <div style="background: rgba(255,0,255,0.05); border: 1px solid #ff00ff; padding: 40px; border-radius: 20px; text-align: center;">
        <h2 style="color:#ff00ff; letter-spacing:5px;">SYSTEM ONLINE</h2>
        <p style="color:#fff; font-size:18px;">Welcome to the shared consciousness of SYKO and YOUSRA. <br> 
        Everything here is built for the future.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == "VAULT":
    st.subheader("📁 ACCESSING ARCHIVES...")
    v_col = st.columns(3)
    for i, title in enumerate(["CYBER-RESOURCES", "NEURAL LINKS", "ENCRYPTED DATA"]):
        with v_col[i]:
            st.markdown(f"""
            <div style="border: 1px solid #00ffff; padding: 20px; border-radius: 10px; background: #111;">
                <h4 style="color:#00ffff;">{title}</h4>
                <p style="font-size:12px; color:gray;">Status: Secure</p>
                <div style="height:2px; background:linear-gradient(90deg, #00ffff, transparent);"></div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.current_page == "STATUS":
    st.subheader("📟 SYSTEM DIAGNOSTICS")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("CPU LOAD")
        st.progress(85)
        st.write("MEMORY INTEGRITY")
        st.progress(98)
    with col_b:
        st.code("""
        > BOOTING SYKO_OS...
        > LOADING YOUSRA_MODULES... [OK]
        > BYPASSING FIREWALL... [DONE]
        > SYSTEM STABLE.
        """, language="bash")

# إخفاء عناصر ستريمليت
st.markdown("<style>header, footer {visibility: hidden;}</style>", unsafe_allow_html=True)
