import streamlit as st

st.title("AI Resume Screener")

resume_text = st.text_area("Paste Resume Text")
job_text = st.text_area("Paste Job Description")

if st.button("Check Match"):
    st.write("Match Score: 82%")