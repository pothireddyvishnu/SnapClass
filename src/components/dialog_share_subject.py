import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    headers = st.context.headers
    protocol = headers.get("X-Forwarded-Proto", "https")
    host = headers.get("X-Forwarded-Host") or headers.get("Host")
    app_domain = f"{protocol}://{host}"

    join_url = f'{app_domain}/join?code={subject_code}'
    st.header('Scan QR to Join')
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        st.code(join_url, language='text')
        st.code(subject_code, language='text')
        st.info('Copy this link to share with your students.')

    with col2:
        st.markdown('### Scan to Join')
        st.image(out.getvalue(), caption='QR Code')