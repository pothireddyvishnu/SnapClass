import streamlit as st
import numpy as np
from PIL import Image
import time

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {student_data['name']}")
        if st.button("Logout", type='secondary', key='student_logout_btn', shortcut='Ctrl+O'):
            st.session_state.is_logged_in = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)

    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch', shortcut='Ctrl+E'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {'total_attendance': 0, 'total_classes': 0}

        stats_map[sid]['total_classes'] += 1

        if log.get('is_present'):
            stats_map[sid]['total_attendance'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid, {'total_attendance': 0, 'total_classes': 0})

        def unenroll_btn(subject_id=sid, subject_name=sub['name']):
            if st.button(
                'Unenroll from this subject',
                key=f'unenroll_subject_{subject_id}',
                type='tertiary',
                width='stretch',
                icon=':material/delete_forever:',
            ):
                unenroll_student_to_subject(student_id, subject_id)
                st.toast(f'Unenrolled from {subject_name} successfully!')
                st.rerun()


        with cols[i % 2]:
            subject_card(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    (':material/event:', 'Total', stats['total_classes']),
                    (':material/check_circle:', 'Present', stats['total_attendance'])
                ],
                footer_callback=unenroll_btn
            )

    footer_dashboard()

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if 'student_data' in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button('Go back to Home', type='secondary', key='teacher_login_back_btn', width='stretch', shortcut='Ctrl+B'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()

    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        photo_array = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning your face...'):
            detected, all_ids, num_faces = predict_attendance(photo_array)

            if num_faces == 0:
                st.warning('Face not detected!')
            elif num_faces > 1:
                st.warning('Multiple faces detected!')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome back {student["name"]}!')
                        time.sleep(2)
                        st.rerun()
                else:
                    st.info('Face not recognized! You may need to register your face.')
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input('Enter your name', placeholder='John Doe')

            st.subheader('Optional: Voice Enrollment')
            st.info('Enroll your voice only attendance')

            audio_date = None

            try:
                audio_data = st.audio_input('Record a short phrase like "I\'m present, My name is John Doe".')
            except Exception as e:
                st.error(f'Error occurred while recording audio: {e}')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile...'):
                        photo_array = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(photo_array)

                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile created! Hi {new_name}!')
                                time.sleep(2)
                                st.rerun()
                        else:
                            st.error('Could\'t capture your facial features.')
                else:
                    st.warning('Please enter your name.')

    footer_dashboard()
