import streamlit as st

st.set_page_config(page_title="SYKO | Future Concept", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    .stApp { background-color: #050505; color: #ffffff; }
    .syko-logo {
        font-family: 'Orbitron', sans-serif;
        font-size: 80px;
        text-align: center;
        background: linear-gradient(90deg, #ff00ff, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 0px 15px rgba(0, 210, 255, 0.6));
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="syko-logo">SYKO</h1>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>Welcome to my world</h3>", unsafe_allow_html=True)

if st.button("Activate SYKO Power"):
    st.balloons()
    st.success("SYKO IS LIVE! 🚀")
