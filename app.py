import streamlit as st
from utils import extract_text_from_pdf, preprocess_text
from model import analyze_match
import tempfile
import time

# Streamlit UI Setup
st.set_page_config(page_title="AI Resume & Job Matcher", page_icon="📄", layout="centered")
st.title("📄 AI Resume & Job Matcher")
st.write("### Upload your resume & job description to see how well they match!")

# File Upload
uploaded_file = st.file_uploader("📂 Upload your resume (PDF)", type=["pdf"])
resume_text = ""
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        resume_text = extract_text_from_pdf(temp_file.name)
    st.success("✅ Resume uploaded successfully!")

job_description = st.text_area("📝 Paste the job description here:", height=200, placeholder="Enter the job description...")

if st.button("Analyze Match ✅"):
    if resume_text and job_description:
        with st.spinner("🔍 Analyzing the match... Please wait."):
            time.sleep(2)  # Simulate loading time
            processed_resume = preprocess_text(resume_text)
            processed_job = preprocess_text(job_description)
            match_score = analyze_match(processed_resume, processed_job)
        
        st.success(f"🔥 Match Score: {match_score:.2f}%")
        st.progress(match_score / 100)
        
        if match_score > 80:
            st.balloons()
            st.write("🎉 Excellent match! Your resume is highly aligned with this job.")
        elif match_score > 50:
            st.write("👍 Good match! Consider fine-tuning your resume for a better fit.")
        else:
            st.write("⚠️ Weak match. You may need to modify your resume for better alignment.")
    else:
        st.warning("⚠️ Please upload a resume and enter a job description!")
