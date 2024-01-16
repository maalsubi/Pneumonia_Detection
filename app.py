import streamlit as st
from prediction import show
from home import display
from PIL import Image

img=Image.open("icon.png")
st.set_page_config(
        page_title="Pnemonia Detector",
        page_icon=img,
        layout="wide",
        initial_sidebar_state="expanded",
)

page_bg_img="""
<style>
    [data-testid="stAppViewContainer"]{
        background-color:#EBF0F1;
    }
    p{
        color:#090A0A;
    }
    h5,h3,h1{
        color:#090A0A;
    }
    div.stButton > button:first-child {
        background-color: #00cc00;color:white;font-size:20px;height:3em;width:15em;border-radius:10px 10px 10px 10px;
    }

</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


st.sidebar.header('Navigations')

options = ["HOME", "PREDICTIONS"]

default_option_index = options.index("HOME")
selected_option = st.sidebar.selectbox("Select an option", options, index=default_option_index)


if selected_option=='PREDICTIONS':
    show()
if selected_option=='HOME':
    display()