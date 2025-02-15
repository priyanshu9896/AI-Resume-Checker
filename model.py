from sentence_transformers import SentenceTransformer, util
import torch

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def analyze_match(resume_text, job_description):
    """Analyzes how well the resume matches the job description."""
    # Encode the texts
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    
    # Compute cosine similarity
    cosine_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    # Convert to percentage
    match_score = cosine_score * 100
    return match_score
