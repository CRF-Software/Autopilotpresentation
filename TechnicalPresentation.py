import streamlit as st

# Set page configuration
st.set_page_config(page_title="Textract Handwritten Forms | Data Science Solution", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
        padding-top: 10px;
        padding-bottom: 10px;
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
    .start-link {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the main title
st.markdown('<div class="main-title">Textract Handwritten Forms | Data Science Solution</div>', unsafe_allow_html=True)

# Create Tabs for the Presentation
tabs = st.tabs(["Overview", "Notebook Structure", "Key Features", "Real-World Applications"])

# Tab 1: Overview
with tabs[0]:
    st.markdown('<div class="sub-title">Overview</div>', unsafe_allow_html=True)
    st.write("""
    This notebook demonstrates a **data science solution** for processing handwritten forms using **Amazon Textract** 
    and **Amazon Augmented AI (A2I)**. The solution integrates **Optical Character Recognition (OCR)** for automated extraction of handwritten content and employs **human-in-the-loop (A2I)** processing for enhanced accuracy in cases of uncertain or ambiguous text.
    """)
    st.markdown('<div class="text">The notebook is divided into several key steps:</div>', unsafe_allow_html=True)
    st.write("""
    1. Setting up the environment and dependencies for Textract and A2I.
    2. Defining and configuring an A2I workflow.
    3. Processing handwritten forms with Textract and sending uncertain predictions to a human for review.
    4. Collecting and displaying results, including human reviews for low-confidence OCR outputs.
    """)

# Tab 2: Notebook Structure
with tabs[1]:
    st.markdown('<div class="sub-title">Notebook Structure</div>', unsafe_allow_html=True)
    st.write("""
    The notebook follows a clear and structured approach:
    
    - **1. Environment Setup**: This section installs the necessary Python libraries and sets up the AWS SDK (Boto3) for interacting with Textract and A2I.
    
    - **2. Configuring Textract**: The solution configures Textract to process scanned forms, specifically targeting handwritten elements.
    
    - **3. Setting Up A2I Workflow**: This part configures the Amazon A2I workflow, defining conditions for when human intervention is required. It includes:
        - Setting confidence thresholds.
        - Triggering human reviews when confidence scores are below a certain threshold.
        
    - **4. Processing Forms**: The notebook processes the forms using Textract, and if a low-confidence prediction is made, it sends the document for human review via A2I.
    
    - **5. Collecting Results**: The results from Textract and A2I are combined to provide final, high-accuracy outputs for each processed form.
    """)

# Tab 3: Key Features
with tabs[2]:
    st.markdown('<div class="sub-title">Key Features</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">This solution offers advanced features for handwritten form processing:</div>', unsafe_allow_html=True)
    st.write("""
    1. **Automated Handwriting Recognition**: Uses Amazon Textract's OCR capabilities to automatically extract handwritten text from scanned documents.
    
    2. **Human-in-the-Loop Processing**: Employs Amazon Augmented AI (A2I) to involve human reviewers for predictions with low confidence, ensuring the highest accuracy for critical data.
    
    3. **Confidence Scores**: Each prediction comes with a confidence score, allowing for selective human intervention only where needed.
    
    4. **End-to-End Workflow**: Automates the entire process from OCR extraction to human review, minimizing manual labor while improving data quality.
    
    5. **Real-Time Processing**: Capable of processing multiple documents in real-time, making it suitable for large-scale operations.
    """)

# Tab 4: Real-World Applications
with tabs[3]:
    st.markdown('<div class="sub-title">Real-World Applications</div>', unsafe_allow_html=True)
    st.write("""
    This solution can be applied across various industries and use cases:
    
    1. **Nonprofit Organizations**: Automating the processing of handwritten data, such as meal counts and attendance sheets for shelters or relief efforts.
    
    2. **Healthcare**: Extracting handwritten notes from medical forms, prescriptions, or patient intake forms where high accuracy is crucial.
    
    3. **Legal**: Processing handwritten contracts or agreements that need to be digitized and reviewed with confidence.
    
    4. **Finance**: Extracting data from handwritten invoices, receipts, or financial documents, reducing the need for manual data entry.
    
    5. **Government**: Automating the processing of handwritten forms for social services, census data, or other public sector tasks that involve large volumes of paper-based records.
    
    The combination of OCR and A2I ensures a scalable and reliable solution that can handle handwritten documents with varying degrees of legibility.
    """)

