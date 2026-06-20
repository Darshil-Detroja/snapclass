import streamlit as st

def footer_home():
    st.markdown("""
        <div style="
            margin-top:2rem;
            text-align:center;
            font-size:18px;
            font-weight:700;
            font-family:'Segoe UI', sans-serif;
            color:white;
            letter-spacing:1px;
        ">
            Created with ❤️ by
            <span style="
                background: linear-gradient(90deg, #ff4b4b, #6c63ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size:20px;
            ">
                Darshil Detroja
            </span>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top:2rem;
            text-align:center;
            font-size:18px;
            font-weight:700;
            font-family:'Segoe UI', sans-serif;
            color:black;
            letter-spacing:1px;
        ">
            Created with ❤️ by
            <span style="
                background: linear-gradient(90deg, #ff4b4b, #6c63ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size:20px;
            ">
                Darshil Detroja
            </span>
        </div>
    """, unsafe_allow_html=True)