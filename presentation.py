import streamlit as st

# Set page configuration
st.set_page_config(page_title="Autoplito | ML-Powered Meal Count Solution", layout="centered")

# Title Section (Global for all Tabs)
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
        padding-top: 10px;
        padding-bottom: 30px;
    }
    .sub-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .text {
        font-size: 18px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Display the main title
st.markdown('<div class="main-title">Autoplito - ML-Powered Meal Count Solution</div>', unsafe_allow_html=True)

# Create Tabs for the Presentation
tabs = st.tabs(["Overview", "Key Features", "Why Choose Autoplito?", "Get Started"])

# Tab 1: Overview
with tabs[0]:
    st.markdown('<div class="sub-title">Overview</div>', unsafe_allow_html=True)
    st.write("""
    **Autoplito** is a state-of-the-art machine learning application developed for the financial team at **The Children's Rescue Fund (CRF)**. 
    This app automatically processes handwritten meal counts from paper sheets using **Optical Character Recognition (OCR)** and **Intelligent Document Processing (IDP)**.
    Autoplito not only extracts the data but also provides **confidence scores** for each reading, allowing users to validate the accuracy of the captured information.
    """)
    st.markdown('<div class="text">Key Benefits Include:</div>', unsafe_allow_html=True)
    st.write("""
    - Automates data entry from handwritten sheets, saving hours of manual work.
    - Offers confidence scores to assess the accuracy of the OCR readings.
    - Seamlessly integrates into the CRF financial workflow to improve data quality.
    """)

# Tab 2: Key Features
with tabs[1]:
    st.markdown('<div class="sub-title">Key Features</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Autoplito offers advanced capabilities to streamline meal count processing:</div>', unsafe_allow_html=True)
    st.write("""
    1. **OCR & IDP**: Uses Optical Character Recognition and Intelligent Document Processing to digitize handwritten meal count sheets.
    2. **Confidence Scores**: Automatically provides confidence scores for each count, helping to ensure data accuracy.
    3. **Error Detection**: Flags low-confidence readings for review, enabling the financial team to focus on potential inaccuracies.
    4. **Real-Time Processing**: Processes meal count sheets quickly and provides immediate results for operational use.
    """)

# Tab 3: Why Choose Autoplito?
with tabs[2]:
    st.markdown('<div class="sub-title">Why Choose Autoplito?</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Autoplito offers unmatched efficiency and accuracy for handling handwritten data at CRF:</div>', unsafe_allow_html=True)
    st.write("""
    - **Time-Saving**: Reduces manual data entry by 90%, allowing staff to focus on higher-value tasks.
    - **Confidence Scores**: Empowers teams with the ability to quickly verify the reliability of data, reducing errors.
    - **Seamless Integration**: Easily integrates with existing financial systems to streamline meal tracking and reporting.
    - **High Accuracy**: State-of-the-art machine learning algorithms ensure precise meal count recognition, even for hard-to-read handwriting.
    """)

# Tab 4: Get Started
with tabs[3]:
    st.markdown('<div class="sub-title">Get Started with Autoplito</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Interested in revolutionizing how CRF handles meal counts? Autoplito is the solution.</div>', unsafe_allow_html=True)
    st.write("""
    - **Request a Demo**: Reach out to schedule a live demo and see Autoplito in action.
    - **Implementation Support**: We offer hands-on assistance to integrate Autoplito into your financial workflow.
    - **Contact Us**: Ready to streamline your meal count processes? Contact us to discuss how Autoplito can enhance your operations.
    """)

    st.markdown("""
    ---
    *Note*: Autoplito is part of CRF’s ongoing commitment to using cutting-edge technology to improve operational efficiency and data accuracy.
    """)
