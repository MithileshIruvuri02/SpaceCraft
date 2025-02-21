# 🌌 SpaceCraft - AI Interior Design Helper  

**SpaceCraft** is an AI-powered tool that generates interior design images based on user descriptions. Whether you're an interior designer, homeowner, or enthusiast, SpaceCraft helps you visualize room designs with AI-generated images.  

---

## 🚀 Features  
✅ **AI-Generated Designs** - Describe your ideal room, and AI creates a visual representation.  
✅ **Fast & Free Model** - Uses Stable Diffusion for efficient image generation.  
✅ **Download Designs** - Save generated images with a single click.  
✅ **Theme Suggestions** - Get inspired with pre-built room themes.  
 

---

## 🛠️ Tech Stack  
- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Model**: Stable Diffusion (Hugging Face Diffusers)  
- **Dependencies**: `streamlit`, `torch`, `diffusers`, `transformers`, `safetensors`, `accelerate`  

---

## 🎥 How It Works  
1️⃣ **Enter a Room Description** - Example: "A modern minimalist bedroom with warm lighting"  
2️⃣ **AI Generates an Image** - SpaceCraft uses AI to visualize your idea  
3️⃣ **Download & Share** - Save the generated image for reference  

---

## 🖥️ Installation & Running Locally  

### **Clone the Repository**  
```sh
git clone https://github.com/MithileshIruvuri02/SpaceCraft.git
cd SpaceCraft
```
### **Create a Virtual Environment**
```sh
python -m venv env
```
 **Activate it**:
 - **Windows**:
```sh

env\Scripts\activate
   ```
- **Mac/Linux**
```sh
source env/bin/activate
```
### **Install Dependencies**
```sh
pip install -r requirements.txt
```
### **Run the App**
```sh
streamlit run src/app.py
```
