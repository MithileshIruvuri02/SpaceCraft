import torch
from diffusers import StableDiffusionPipeline
from config import DEVICE, MODEL_NAME

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
pipe.to(DEVICE)

def generate_image(prompt):
    """Generate multiple images at once for faster performance."""
    with torch.no_grad():
        images = pipe([prompt] * 2, num_inference_steps=30).images  # Generate 2 images at once
    image_paths = []
    for i, image in enumerate(images):
        image_path = f"assets/generated_image_{i}.png"
        image.save(image_path)
        image_paths.append(image_path)
    return image_paths  # Return all generated images

