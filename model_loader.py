# model_loader.py
import torch
from transformers import pipeline

def load_text_generation_pipeline(model_path):
    """Loads and returns a Hugging Face text-generation pipeline."""
    print("Loading model from local path...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    text_generator = pipeline(
        "text-generation",
        model=model_path,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    print("Model loaded successfully.")
    return text_generator