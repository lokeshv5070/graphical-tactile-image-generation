import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to convert image to sketched image
def convert_to_sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    final = cv2.divide(img_gray, 255-85 , scale=255)
    return final

# Main Streamlit app
def main():
    st.title("Image to Sketch Converter")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        
        # Convert image to sketched image
        sketched_image = convert_to_sketch(image)
        
        # Display original and sketched image
        st.subheader("Original Image")
        st.image(image, caption='Original Image', use_column_width=True)
        
        st.subheader("Sketched Image")
        st.image(sketched_image, caption='Sketched Image', use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()