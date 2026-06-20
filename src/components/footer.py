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
            color:#FFD700;
            font-size:22px;
            font-weight:800;
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
            color:#FFD700;
            font-size:22px;
            font-weight:800;
        ">
                Darshil Detroja
            </span>
        </div>
    """, unsafe_allow_html=True)