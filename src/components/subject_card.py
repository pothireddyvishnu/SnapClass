import streamlit as st


def subject_card(name, code, section, stats=None, header_callback=None, footer_callback=None):
    card_key = f"subject_card_{''.join(char if char.isalnum() else '_' for char in str(code))}"
    st.markdown(
        f"""
        <style>
            .st-key-{card_key} {{
                background: white;
                border: 1px solid black;
                border-left: 8px solid #EB459E;
                border-radius: 20px;
                padding: 25px;
                margin-bottom: 20px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    card = st.container(key=card_key)
    with card:
        title_col, action_col = st.columns([3, 2], vertical_alignment='center')
        with title_col:
            st.markdown(f'<h3 style="margin:0; color: #1e293b; font-size: 1.5rem">{name}</h3>', unsafe_allow_html=True)
        with action_col:
            if header_callback:
                header_callback()

    html = f"""
        <style>
            .material-symbols-rounded {{
                font-family: 'Material Symbols Rounded';
                font-size: 1rem;
                vertical-align: -0.18em;
            }}
            .subject-stat, .subject-stat *, .subject-stat b {{
                color: #1e293b !important;
            }}
        </style>
        <p style="color:#64748b; margin:10px 0;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            if icon.startswith(':material/') and icon.endswith(':'):
                icon_name = icon[len(':material/'):-1]
                icon = f'<span class="material-symbols-rounded">{icon_name}</span>'
            html += f'<div class="subject-stat" style="background: #EB459E10; color: #1e293b !important; padding:5px 12px; border-radius:12px; font-size:0.9rem"><span style="color: #1e293b !important;">{icon}</span> <b style="color: #1e293b !important;">{value}</b> <span style="color: #1e293b !important;">{label}</span></div>'
        
        html+= "</div>"

    with card:
        st.markdown(html, unsafe_allow_html=True)

        if footer_callback:
            footer_callback()
