import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

# Function to apply transformations
def apply_transformations(img, rotation, scale, translate, skew):
    # Rotation
    img = img.rotate(rotation, expand=True)
    
    # Scaling
    width, height = img.size
    img = img.resize((int(width * scale), int(height * scale)))
    
    # Translation
    img = ImageOps.offset(img, translate[0], translate[1])
    
    # Skewing
    skew_matrix = (1, skew[0], 0, skew[1], 1, 0)
    img = img.transform(img.size, Image.AFFINE, skew_matrix)
    
    return img

# Title
st.title("Transform Your Image")

# Subtitle
st.subheader("100% Automatically and Free")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Rotation slider
    rotation = st.slider("Rotation", 0, 360, 0)
    
    # Scaling slider
    scale = st.slider("Scale", 0.1, 3.0, 1.0)
    
    # Translation sliders
    translate_x = st.slider("Translate X", -100, 100, 0)
    translate_y = st.slider("Translate Y", -100, 100, 0)
    
    # Skewing sliders
    skew_x = st.slider("Skew X", -1.0, 1.0, 0.0)
    skew_y = st.slider("Skew Y", -1.0, 1.0, 0.0)
    
    # Apply transformations
    transformed_image = apply_transformations(image, rotation, scale, (translate_x, translate_y), (skew_x, skew_y))
    
    # Display enhanced image
    st.image(transformed_image, caption='Transformed Image.', use_column_width=True)
