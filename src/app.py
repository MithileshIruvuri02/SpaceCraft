import streamlit as st
import os
import uuid
from image_generator import generate_image  # Assuming this function generates the image

st.set_page_config(page_title="SpaceCraft - AI Interior Design", layout="wide")

# Sidebar: Theme Suggestions
st.sidebar.title("🎨 Theme Suggestions")
theme_options = [
    "Modern Living Room with Neutral Tones",
    "Minimalist Bedroom with Warm Lighting",
    "Industrial Kitchen with Exposed Brick",
    "Scandinavian Office with Wooden Accents",
]
selected_theme = st.sidebar.radio("Choose a theme:", theme_options)

st.title("🏠 AI-Powered Interior Design Helper")
st.write("Describe your ideal room, and AI will generate the design.")

# User input prompt
user_prompt = st.text_area("Describe your room:", selected_theme if selected_theme else "")

if st.button("Generate Design"):
    if user_prompt:
        st.write("🎨 Generating design... Please wait.")
        
        # Call the image generator to create the image
        image_paths = generate_image(user_prompt)  # Assuming this function returns a list of image paths
        
        # Display all generated images
        for image_path in image_paths:
            st.image(image_path, caption="Generated Design", use_container_width=True)
            
            # Provide a download button for each image
            with open(image_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download Design",
                    data=file,
                    file_name=os.path.basename(image_path),
                    mime="image/png"
                )
    else:
        st.warning("⚠️ Please enter a description first.")
