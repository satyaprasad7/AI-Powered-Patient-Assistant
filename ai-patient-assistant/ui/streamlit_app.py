import sys
import os
import streamlit as st
project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, project_root)

from app.main import run_patient_assistant

from app.main import run_patient_assistant

st.set_page_config(
    page_title="AI Patient Assistant",
    layout="wide"
)

st.title(
    "🏥 AI-Powered Patient Assistant"
)

patient = st.text_input(
    "Patient Name"
)

symptoms = st.text_area(
    "Enter Symptoms"
)

question = st.text_input(
    "Medical Question"
)

policy = st.text_input(
    "Insurance Policy"
)

if st.button(
        "Run Patient Assistant"):

    result = run_patient_assistant(
        patient,
        symptoms,
        question,
        policy
    )

    st.subheader(
        "Symptom Assessment"
    )

    st.json(
        result["assessment"]
    )

    st.subheader(
        "Appointment"
    )

    st.json(
        result["appointment"]
    )

    st.subheader(
        "Medical FAQ"
    )

    st.write(
        result["faq"]
    )

    st.subheader(
        "Insurance"
    )

    st.json(
        result["insurance"]
    )