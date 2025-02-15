import streamlit as st
import tempfile
import time
import matplotlib.pyplot as plt
import seaborn as sns
from utils import extract_text_from_pdf, preprocess_text
from model import analyze_match

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
    st.info("📄 Resume extracted successfully. Ready for analysis!")
    st.toast("📑 Resume processing complete!")

# Job Description Input
job_description = st.text_area("📝 Paste the job description here:", height=200, placeholder="Enter the job description...")

if st.button("Analyze Match ✅"):
    if resume_text and job_description:
        with st.spinner("🔍 Analyzing the match... Please wait."):
            time.sleep(2)  # Simulate loading time
            processed_resume = preprocess_text(resume_text)
            processed_job = preprocess_text(job_description)
            match_score = analyze_match(processed_resume, processed_job)
        
        # Display Match Score
        st.success(f"🔥 Match Score: {match_score:.2f}%")
        st.progress(match_score / 100)
        
        # Analysis Result
        if match_score > 80:
            st.balloons()
            st.write("🎉 Excellent match! Your resume is highly aligned with this job.")
        elif match_score > 50:
            st.write("👍 Good match! Consider fine-tuning your resume for a better fit.")
        else:
            st.write("⚠️ Weak match. You may need to modify your resume for better alignment.")
        
        # Visual Insights
        st.write("### 📊 Resume Analysis Insights")
        labels = ["Match", "Missing Skills"]
        values = [match_score, 100 - match_score]
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#FF5252'], startangle=140)
        st.pyplot(fig)
        
        # Additional Insights Section
        st.write("### 📌 Additional Recommendations")
        st.success("📌 Consider adding more keywords related to the job description.")
        st.warning("⚠️ Ensure your resume format is ATS-friendly.")
        st.info("💡 Highlight more relevant projects or experiences to boost match percentage.")
    
    else:
        st.warning("⚠️ Please upload a resume and enter a job description!")
