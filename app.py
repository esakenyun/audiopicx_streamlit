import streamlit as st
from pydub import AudioSegment
from io import BytesIO

# Function to compress audio
def compress_audio(input_file, bitrate='64k'):
    audio = AudioSegment.from_file(input_file)
    compressed_audio = audio.set_frame_rate(44100).set_channels(1)
    # Menggunakan BytesIO untuk menyimpan audio yang telah dikompresi
    output_buffer = BytesIO()
    compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
    return output_buffer

# Main function
def main():
    st.set_page_config(page_title="Audio Compression App", page_icon="logo.svg", layout="wide", initial_sidebar_state="collapsed")

    # Custom CSS to change the theme color
    st.markdown("""
        <style>
            body {
                color: #333;
                background-color: #f0f0f0;
            }
            .sidebar .sidebar-content {
                background-color: #222;
            }
            .sidebar .sidebar-content .block-container {
                color: #fff;
            }
            .css-17eq0hr {
                color: #000;
                background-color: #ccc;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Audio Compression App")
    
    # Sidebar
    st.sidebar.image("logo.svg", width=100)
    
    # Main content
    st.write("""
    ## Upload your audio file and compress it!
    """)
    bitrate = st.sidebar.selectbox("Select bitrate", ["64k", "128k", "192k", "256k", "320k"])
    
    # File upload
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/mp3', start_time=0)
        st.write("Uploaded File Details:")
        file_details = {"Filename":audio_file.name,"FileType":audio_file.type,"FileSize":audio_file.size}
        st.write(file_details)
        
        # Compress button
        if st.button("Compress"):
            st.write("Compressing...")
            output_buffer = compress_audio(audio_file, bitrate=bitrate)
            st.success("Compression successful!")
            
            # Mengirim file kepada pengguna dan memungkinkan mereka mengunduhnya
            st.write("Download Compressed Audio")
            st.download_button(label='Download', data=output_buffer, file_name='compressed_audio.mp3', mime='audio/mp3')

# Run the app
if __name__ == '__main__':
    main()
