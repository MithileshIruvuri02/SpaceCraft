import torch

# Check if GPU is available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Model name (Stable Diffusion)
MODEL_NAME = "stabilityai/stable-diffusion-2-1-base"

