import streamlit as st
from PIL import Image, ImageEnhance, ImageOps, ImageDraw
import numpy as np
from io import BytesIO

# Load the logo image
logo = Image.open("president_university_logo.png")

# Function to apply transformations
def apply_transformations(img, rotation, scale, translate, skew, brightness, contrast, filter_type):
    # Rotation
    img = img.rotate(rotation, expand=True)
    
    # Scaling
    width, height = img.size
    img = img.resize((int(width * scale), int(height * scale)))
    
    # Translation
    translate_matrix = (1, 0, translate[0], 0, 1, translate[1])
    img = img.transform(img.size, Image.AFFINE, translate_matrix)
    
    # Skewing
    skew_matrix = (1, skew[0], 0, skew[1], 1, 0)
    img = img.transform(img.size, Image.AFFINE, skew_matrix)
    
    # Brightness Adjustment
    brightness_enhancer = ImageEnhance.Brightness(img)
    img = brightness_enhancer.enhance(brightness)
    
    # Contrast Adjustment
    contrast_enhancer = ImageEnhance.Contrast(img)
    img = contrast_enhancer.enhance(contrast)
    
    # Apply Filters
    if filter_type == "Grayscale":
        img = ImageOps.grayscale(img)
    elif filter_type == "Sepia":
        sepia = np.array(img.convert("RGB"))
        sepia = sepia.dot([0.393, 0.769, 0.189, 0.349, 0.686, 0.168, 0.272, 0.534, 0.131])
        sepia[sepia > 255] = 255
        img = Image.fromarray(sepia.astype('uint8'))
    elif filter_type == "Negative":
        img = ImageOps.invert(img.convert("RGB"))
    
    return img

# Function to convert image to bytes
def get_image_download_link(img, filename, text):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = buffered.getvalue()
    btn = st.download_button(label=text, data=img_str, file_name=filename, mime="image/png")
    return btn

# Create a menu with multiple pages
menu = ["Home", "Transform Image", "About Us"]

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", menu)

# Display the logo at the top
st.sidebar.image(logo, width=100, caption='President University Logo')

if choice == "Home":
    st.title("Linear Algebra Group 5")
    st.subheader("Welcome to our Image Processing Project")
    st.write("Explore the transformations and techniques we used to manipulate and enhance images.")
    
elif choice == "Transform Image":
    st.title("Transform Your Image")
    st.subheader("100% Automatically and Free")

    # Upload image
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Rotation slider with tooltip
        rotation = st.slider("Rotation", 0, 360, 0, help="Rotate the image in degrees.")
        
        # Scaling slider with tooltip
        scale = st.slider("Scale", 0.1, 3.0, 1.0, help="Scale the image size.")
        
        # Translation sliders with tooltip
        translate_x = st.slider("Translate X", -100, 100, 0, help="Translate the image horizontally.")
        translate_y = st.slider("Translate Y", -100, 100, 0, help="Translate the image vertically.")
        
        # Skewing sliders with tooltip
        skew_x = st.slider("Skew X", -1.0, 1.0, 0.0, help="Skew the image horizontally.")
        skew_y = st.slider("Skew Y", -1.0, 1.0, 0.0, help="Skew the image vertically.")
        
        # Brightness slider with tooltip
        brightness = st.slider("Brightness", 0.1, 2.0, 1.0, help="Adjust the brightness of the image.")
        
        # Contrast slider with tooltip
        contrast = st.slider("Contrast", 0.1, 2.0, 1.0, help="Adjust the contrast of the image.")
        
        # Filter type with tooltip
        filter_type = st.selectbox("Select Filter", ["None", "Grayscale", "Sepia", "Negative"], help="Apply a filter to the image.")
        
        # Apply transformations
        transformed_image = apply_transformations(image, rotation, scale, (translate_x, translate_y), (skew_x, skew_y), brightness, contrast, filter_type)
        
        # Display enhanced image with side-by-side preview
        st.image(transformed_image, caption='Transformed Image.', use_column_width=True)

        # Add download button
        get_image_download_link(transformed_image, "transformed_image.png", "Download Transformed Image")

elif choice == "About Us":
    st.title("About Us")
    st.write("We are Group 5 from President University, working on a project in Linear Algebra focusing on image processing. Meet the team members who made this project possible.")
    
    # Group members with clickable names to show pictures
    st.subheader("Group Members")
    
    if st.button("Abdulloh Dzaka (004202305027)"):
        st.image("abdulloh_dzaka.png", caption="Abdulloh Dzaka")

    if st.button("Mikhael Andwadiwana (004202305076)"):
        st.image("mikhael_andwadiwana.png", caption="Mikhael Andwadiwana")
