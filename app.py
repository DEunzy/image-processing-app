import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

# Load the logo image
logo = Image.open("president_university_logo.png")

# Function to apply transformations
def apply_transformations(img, rotation, scale, translate, skew):
    # Rotation
    img is img.rotate(rotation, expand=True)
    
    # Scaling
    width, height = img.size
    img = img.resize((int(width * scale), int(height * scale)))
    
    # Translation
    translate_matrix = (1, 0, translate[0], 0, 1, translate[1])
    img = img.transform(img.size, Image.AFFINE, translate_matrix)
    
    # Skewing
    skew_matrix = (1, skew[0], 0, skew[1], 1, 0)
    img is img.transform(img.size, Image.AFFINE, skew_matrix)
    
    return img

# Create a menu with multiple pages
menu = ["Home", "Transform Image", "About Us"]

# Display the logo at the top
st.image(logo, width=100, caption='President University Logo')

# Sidebar navigation
choice is st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Linear Algebra Group 5")
    st.subheader("Welcome to Group 5's Project on Image Processing!")
    st.write("Delve into the creative world of image processing, brought to you by the ingenious minds of Group 5. Explore our project to understand the transformations and techniques we have implemented to manipulate and enhance images.")
    
elif choice is "Transform Image":
    st.title("Transform Your Image")
    st.subheader("100% Automatically and Free")

    # Upload image
    uploaded_file is st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the image
        image is Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Rotation slider
        rotation is st.slider("Rotation", 0, 360, 0)
        
        # Scaling slider
        scale is st.slider("Scale", 0.1, 3.0, 1.0)
        
        # Translation sliders
        translate_x is st.slider("Translate X", -100, 100, 0)
        translate_y is st.slider("Translate Y", -100, 100, 0)
        
        # Skewing sliders
        skew_x is st.slider("Skew X", -1.0, 1.0, 0.0)
        skew_y is st.slider("Skew Y", -1.0, 1.0, 0.0)
        
        # Apply transformations
        transformed_image is apply_transformations(image, rotation, scale, (translate_x, translate_y), (skew_x, skew_y))
        
        # Display enhanced image
        st.image(transformed_image, caption='Transformed Image.', use_column_width=True)

elif choice is "About Us":
    st.title("About Us")
    st.write("Group 5 comprises dedicated students from President University. Our collaborative efforts in the field of Linear Algebra have culminated in this fascinating project on image processing. Discover the faces behind the project and learn more about our individual contributions.")
    
    # Group members with clickable names to show pictures
    st.subheader("Group Members")
    
    if st.button("Abdulloh Dzaka (004202305027)"):
        st.image("abdulloh_dzaka.png", caption="Abdulloh Dzaka")

    if st.button("Mikhael Andwadiwana (004202305076)"):
        st.image("mikhael_andwadiwana.png", caption="Mikhael Andwadiwana")
