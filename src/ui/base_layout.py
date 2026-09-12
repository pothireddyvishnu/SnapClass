import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
                    .stApp{
                    background: #5865F2 !important;
                    }
                
                .stApp div[data-testid="stColumn"]{
                    background: #E0E3FF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }

                /* The home cards are light, so their Streamlit headings must
                   not inherit the white foreground from dark mode. */
                .stApp div[data-testid="stColumn"] [data-testid="stHeading"],
                .stApp div[data-testid="stColumn"] [data-testid="stHeading"] *,
                .stApp div[data-testid="stColumn"] [data-testid="stHeadingWithActionElements"],
                .stApp div[data-testid="stColumn"] [data-testid="stHeadingWithActionElements"] * {
                    color: #1e293b !important;
                }

                .stApp div[data-testid="stColumn"] button,
                .stApp div[data-testid="stColumn"] button * {
                    color: white !important;
                }
        </style>
    """, unsafe_allow_html=True)





def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }

            .stApp [data-testid="stHeading"],
            .stApp [data-testid="stHeading"] *,
            .stApp [data-testid="stHeadingWithActionElements"],
            .stApp [data-testid="stHeadingWithActionElements"] *,
            .stApp [data-testid="stSelectbox"] label,
            .stApp [data-testid="stCameraInput"] label,
            .stApp [data-testid="stTextInput"] label,
            .stApp [data-testid="stAudioInput"] label,
            .stApp [data-testid="stMetricLabel"],
            .stApp [data-testid="stMetricValue"] {
                color: #1e293b !important;
            }

            .stApp [data-baseweb="select"] * {
                color: #1e293b !important;
            }

            .stApp button,
            .stApp button * {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)




def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            
            /* Hide Top Bar of streamlit */

            MainMenu, footer, header{
                visibility: hidden;
            }

            .black-container{
                padding-top: 1.5rem !important;
            }

            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }

            h3, h4, p{
                font-family: 'Outfit', sans-serif !important;
            }
                
            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            
            button:hover{
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)
