import streamlit as st
import numpy as np
from PIL import Image

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def student_screen():


    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button('Go back to Home', type='secondary', key='teacher_login_back_btn', width='stretch'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        photo_array = np.array(Image.open(photo_source))
    footer_dashboard()