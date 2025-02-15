from sentence_transformers import SentenceTransformer, util
import torch
import re

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

BIASED_WORDS = {"hardworking": "dedicated", "aggressive": "proactive", "perfectionist": "detail-oriented"}

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

def detect_bias(text):
    """Detects biased words in the resume and suggests neutral alternatives."""
    found_biases = {}
    for word, suggestion in BIASED_WORDS.items():
        if re.search(rf'\b{word}\b', text, re.IGNORECASE):
            found_biases[word] = suggestion
    return found_biases
