import streamlit as st
from pydub import AudioSegment
from io import BytesIO
from PIL import Image

def compress_image(image, width, height):
    image.thumbnail((width, height))
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    return image

def compress_audio(input_file, bitrate='64k'):
    audio = AudioSegment.from_file(input_file)
    compressed_audio = audio.set_frame_rate(44100).set_channels(1)
    output_buffer = BytesIO()
    compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
    return output_buffer

# Page functions
def home():
    st.title("AudioPicX 🔉🎦")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""

        """)
        st.write("""

        """)
        st.write("""

        """)
        st.write("""

        """)
        st.write("""

        """)
        st.write("""

        """)
        st.write("""
        # Welcome To AudioPicX
         Get ready to optimize your audio and image files effortlessly with AudioPicX, setting the stage for streamlined data handling and enhanced media performance
        """)
        st.write("""
         ##### Open Sidebar And Start Now 
        """)
    with col2:
        st.image("./images/homebackground.svg", width=500)

# Image Compression      
def imageCompression():
    st.title("Image Compression")
    st.write("""
    Reveal beauty in a smaller size. Make moments easily shareable with efficient image compression and resizing.
    """)

    upload_image = st.file_uploader("Upload an Image for Compression", type=["jpg", "jpeg", "png"])

    if upload_image is not None:
        image = Image.open(upload_image)
        st.image(image, caption="Preview Image", use_column_width=False)
        width = st.number_input("Enter the desired width for the compressed image:", value=image.width)
        aspect_ratio = image.width / image.height
        height = int(width / aspect_ratio)
        st.write(f"Calculated Height For Compression: {height}")

        if st.button("Compress"):
            compressed_image = compress_image(image, width, height)
            st.image(compressed_image, caption="Compressed Image", use_column_width=False)
            img_buffer = BytesIO()
            compressed_image.save(img_buffer, format='JPEG')
            img_bytes = img_buffer.getvalue()
            st.download_button(label='Download Compressed Image', data=img_bytes, file_name='compressed_image.jpg', mime='image/jpeg')

# Audio Compression
def audioCompression():
    st.title("Audio Compression 🔉")
    st.write("""
    Enhance your audio with advanced compression. Save space, maintain quality. Enjoy clear sound, no compromises.
    """)

    upload_file = st.file_uploader("Upload an Audio File for Compression", type=["mp3", "wav"])
    bitrate = st.selectbox("Select Bitrate For Compression", ["32k", "64k", "128k", "192k", "256k"])

    if upload_file is not None:
        st.audio(upload_file, format='audio/mp3', start_time=0)    
        
        if st.button("Compress"):
            st.write("Compressing...")
            output_buffer = compress_audio(upload_file, bitrate=bitrate)
            st.success("Compression successful!")
            st.write("Download Compressed Audio")
            st.download_button(label='Download', data=output_buffer, file_name='compressed_audio.mp3', mime='audio/mp3')

# Main function
def main():
    st.set_page_config(page_title="AudioPicX", page_icon="./images/logo.svg", layout="wide", initial_sidebar_state="collapsed")

    # Sidebar
    st.sidebar.image("./images/logo.svg", width=200)
    st.sidebar.success("Select Your Page ⬇️")
    page = st.sidebar.selectbox("Select Page", ["Home", "Image Compression", "Audio Compression"])

    if page == "Home":
        home()
    elif page == "Image Compression":
        imageCompression()
    elif page == "Audio Compression":
        audioCompression()

# Run the app
if __name__ == '__main__':
    main()
