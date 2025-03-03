import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                 torch_dtype=torch.bfloat16)