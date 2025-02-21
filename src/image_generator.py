import torch
from diffusers import StableDiffusionPipeline
from config import DEVICE, MODEL_NAME
import uuid
import os
from PIL import Image

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
pipe.to(DEVICE)

def generate_image(prompt):
    """Generate multiple images at once for faster performance."""
    with torch.no_grad():
        images = pipe([prompt] * 2, num_inference_steps=30).images  # Generate 2 images at once
    
    # Generate unique identifier for each batch of images
    unique_id = uuid.uuid4().hex
    
    image_paths = []
    for i, image in enumerate(images):
        # Use UUID to ensure unique filenames
        image_path = os.path.join("assets", f"generated_image_{unique_id}_{i}.png")
        
        # Save the image to the unique path
        image.save(image_path)
        image_paths.append(image_path)
    
    return image_paths  # Return all generated images
