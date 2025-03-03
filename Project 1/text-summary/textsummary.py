import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                 torch_dtype=torch.bfloat16)