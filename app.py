import streamlit as st
from pathlib import Path
import json
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import base64

# Directories and file paths
THIS_DIR = Path(__file__).parent
ASSETS = THIS_DIR / "assets"

# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Function to apply snowfall effect with multiple emojis falling separately
def run_snow_animation():
    # Pass a list of emojis to the 'emoji' parameter
    rain(
        emoji="🥂²²",               # List of emojis
        font_size=30,                     # Size of the emojis
        falling_speed=7,                  # Speed at which emojis fall
        animation_length="infinite"       # Duration of the animation
    )

# Function to get the name from query parameters using the updated API
def get_person_name():
    query_params = st.query_params
    return query_params.get("name", ["Yashii"])[0]

# Page configuration
st.set_page_config(page_title="YASH", page_icon="🥂")

# Run snowfall animation
run_snow_animation()

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Embed custom CSS with background image and styling
def set_custom_css():
    background_image = get_base64_image(ASSETS / "background.jpg")
    css = f"""
    <style>
    /* Import Playfair Display font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    /* Set the background image for the entire page */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Add a semi-transparent overlay to enhance text readability */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4); /* Semi-transparent black overlay */
        z-index: -1;
    }}

    /* Customize header (h1) with Playfair Display font and larger size */
    h1 {{
        color: #000000; /* Black */
        font-family: 'Playfair Display', serif;
        font-size: 60px; /* Larger size for prominence */
    }}

    /* Customize paragraph text with Black color and larger size */
    p, .stText {{
        color: #000000; /* Black */
        font-size: 20px; /* Increased size for better readability */
    }}

    /* Customize Streamlit buttons */
    button {{
        background-color: #FFD700; /* Gold */
        color: #FFC0CB;            /* Rose Pink */
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 6px 3px;
        cursor: pointer;
        border-radius: 10px;
        font-family: 'Playfair Display', serif; /* Match button font with header */
    }}

    /* Hover effect for buttons */
    button:hover {{
        background-color: #DAA520; /* Goldenrod */
        color: #FFFFFF;            /* White */
    }}

    /* Responsive Design: Adjust styles for smaller screens */
    @media only screen and (max-width: 768px) {{
        h1 {{
            font-size: 40px; /* Reduce font size on smaller screens */
        }}

        p, .stText {{
            font-size: 16px; /* Adjust paragraph font size */
        }}

        button {{
            padding: 10px 20px; /* Adjust button padding */
            font-size: 16px;    /* Adjust button font size */
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply custom CSS
set_custom_css()

# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Happy Birthday {PERSON_NAME}! 😺🎂", anchor=False)

# Display the Lottie animation
lottie_animation = load_lottie_animation(ASSETS / "Animation - Birthday.json")
st_lottie(lottie_animation, key="lottie-birthday", height=300)

# Personalized birthday message with inline CSS to ensure black color
st.markdown(
    f"<p style='color: #000000; font-size:25px;'>Dear {PERSON_NAME}, 🎉🎂 Wishing you a fantastic day full of happiness, love, and unforgettable moments. May your year ahead be filled with success, joy, and endless laughter. Enjoy your special day! 🎈✨          -Inshaf😎-</p>",
    unsafe_allow_html=True
)
