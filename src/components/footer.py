import streamlit as st


def footer_home():

    st.markdown(f"""
                <div style="margin-top: 2rem; display: flex; justify-content: center; align-items: center;">
                    <p style="font-weight: bold; color:white;"> Created by VISHNU </p>
                </div>
            
               """, unsafe_allow_html=True)



def footer_dashboard():

    st.markdown(f"""
                <div style="margin-top: 2rem; display: flex; justify-content: center; align-items: center;">
                    <p style="font-weight: bold; color:black;"> Created by VISHNU </p>
                </div>
            
               """, unsafe_allow_html=True)