import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="SYKO GLITCH", layout="centered")

# --- كود التشويش المتقدم (Glitch CSS) ---
st.markdown("""
<style>
    /* خلفية سوداء عميقة */
    .stApp { 
        background-color: #000; 
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* إخفاء عناصر ستريمليت الزائدة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* تأثير التشويش (Glitch Effect) */
    .glitch-container {
        position: relative;
        text-align: center;
    }

    .syko-text {
        color: white;
        font-size: 100px;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        position: relative;
        display: inline-block;
    }

    .syko-text::before,
    .syko-text::after {
        content: 'SYKO UNIVERSE';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: black;
    }

    .syko-text::before {
        left: 2px;
        text-shadow: -2px 0 #ff00ff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim 5s infinite linear alternate-reverse;
    }

    .syko-text::after {
        left: -2px;
        text-shadow: -2px 0 #00ffff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim2 5s infinite linear alternate-reverse;
    }

    @keyframes glitch-anim {
        0% { clip: rect(31px, 9999px, 94px, 0); }
        20% { clip: rect(62px, 9999px, 42px, 0); }
        40% { clip: rect(16px, 9999px, 78px, 0); }
        60% { clip: rect(87px, 9999px, 11px, 0); }
        80% { clip: rect(53px, 9999px, 86px, 0); }
        100% { clip: rect(24px, 9999px, 33px, 0); }
    }

    @keyframes glitch-anim2 {
        0% { clip: rect(10px, 9999px, 85px, 0); }
        25% { clip: rect(70px, 9999px, 20px, 0); }
        50% { clip: rect(30px, 9999px, 60px, 0); }
        75% { clip: rect(50px, 9999px, 10px, 0); }
        100% { clip: rect(90px, 9999px, 40px, 0); }
    }
</style>
""", unsafe_allow_html=True)

# --- عرض الاسم فقط ---
st.markdown("""
<div class="glitch-container">
    <div class="syko-text">SYKO UNIVERSE</div>
</div>
""", unsafe_allow_html=True)
