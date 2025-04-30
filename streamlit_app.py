import streamlit as st

# Set page config
st.set_page_config(page_title="Engineering Maths Calculator", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 60px;
        text-align: center;
        color: black;
    }
    .subtitle {
        font-size: 30px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 30px;
        color: black;
    }
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .stButton > button {
        font-size: 20px !important;
        width: 80%;
        padding: 10px;
        margin: 10px 0;
        background-color: #f0f0f0;
        color: black;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="title">ENGINEERING MATHS CALCULATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This is for the first year students.</div>', unsafe_allow_html=True)

# Button section
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Each button displays a link or a message — you can replace with logic later
if st.button("Gauss Theorem"):
    st.markdown('[Open Gauss Theorem App](https://bilinear-math-project.streamlit.app/)', unsafe_allow_html=True)

if st.button("Stroke Theorem"):
    st.markdown('[Open Stroke Theorem App](https://bilinear-math-project.streamlit.app/)', unsafe_allow_html=True)

if st.button("Green Theorem"):
    st.markdown('[Open Green Theorem App](https://bilinear-math-project.streamlit.app/)', unsafe_allow_html=True)

if st.button("Bilinear Transformation"):
    st.markdown('[Open Bilinear Transformation App](https://bilinear-math-project.streamlit.app/)', unsafe_allow_html=True)

if st.button("Eigen Value and Eigen Vector"):
    st.markdown('[Open Eigen App](https://eigen-value-eigen-vector.streamlit.app/)', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
