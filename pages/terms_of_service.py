import streamlit as st

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
            st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
            st.title(":blue[GCP Gen]:rainbow[AI]")
    st.page_link("homepage.py", label="Home", icon="🏠")
    st.page_link("pages/page_01_text_generation.py", label="Text Generation", icon="📖")
    st.page_link("pages/page_02_media_understanding.py", label="Media Understanding", icon="🎞️")
    st.page_link("pages/page_03_translation.py", label="Text Translation", icon="🇺🇳")
    st.page_link("pages/page_04_travel_advisor.py", label="Travel Advisor", icon="✈️")
    st.page_link("pages/page_05_rag_search.py", label="RAG Search", icon="🔍")
    st.page_link("pages/page_06_media_search.py", label="Media Search", icon="🎥")
    st.page_link("pages/page_07_image_generation.py", label="Image Generation", icon="🎨")
    st.page_link("pages/page_08_chatbot.py", label="Chatbot", icon="💬")
    st.page_link("pages/page_09_gaming_servicebot.py", label="Gaming Servicebot", icon="🤖")
    st.page_link("pages/page_10_ecommerce_servicebot.py", label="E-commerce Servicebot", icon="🤖")
    st.page_link("pages/page_11_claude_chatbot.py", label="Claude 3.5 Chatbot", icon="💬")
    st.page_link("pages/page_12_llama_chatbot.py", label="Llama 3.1 Chatbot", icon="💬")
    st.page_link("https://pantheon.corp.google.com/translation/hub", label="GCP Translation Hub", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/gallery", label="GCP Console - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/engines", label="GCP Console - App Builder", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.markdown(
        """
    ## About
    This is a generative AI platform powered by :blue[Google Cloud Vertex AI] and an enterprise-ready RAG search engine
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
    
    left_co, cent_co,last_co = st.columns([0.41,0.31,0.28])
    with cent_co:
            st.write('© LWK')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.markdown(
        f'<p style="text-align: center;">'
        f'<span style="color: grey;">Designed & Developed by</span> '
        f'<a href="{st.secrets["developer_profile_link"]}" '
        f'style="color: #185ABC; text-decoration: underline;" target="_blank">{st.secrets["developer_name"]}</a>'
        f'</p>',
        unsafe_allow_html=True
    )
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')

    st.page_link("pages/terms_of_service.py", label="Terms of Service", icon="📄")
    st.page_link("pages/privacy_policy.py", label="Privacy Policy", icon="🔒")

left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
with cent_co:
    st.title("GCP GenAI Terms of Service")

left_co, cent_co,last_co = st.columns([0.35,0.5,0.15])
with cent_co:
    st.write("Effective Date: August 1, 2024")

st.text("")

st.markdown("""

Welcome to the GCP GenAI application (hereinafter referred to as "the Application"). Before using the Application, please carefully read the following terms of service. By accessing or using the Application, you agree to be bound by these terms. If you do not agree to these terms, please do not use the Application.

## 1. Service Description

The Application is a demonstration web application designed to showcase the generative AI (GenAI) capabilities of Google Cloud's Vertex AI, including but not limited to text generation, multimodal understanding, RAG search, image generation, and chatbot functionalities. The Application is intended solely for use by Google employees to demonstrate the capabilities of Google Cloud's GenAI products or services to their clients.

## 2. Eligibility

The Application is only available to Google internal employees and is not open for use by any external third parties. You need to log in using your Google company account, and the Application will verify your email address domain to ensure you have permission to use the Application.

## 3. User Responsibilities

3.1 You agree to use the Application only for its intended purpose, which is to demonstrate Google Cloud's GenAI capabilities.

3.2 You should comply with all applicable laws and regulations, and avoid using any content that may be considered sensitive or inappropriate, including but not limited to sensitive words, sensitive images, sensitive videos, or sensitive documents.

3.3 You understand and agree that the Application bears no responsibility if the API refuses to return results due to the use of sensitive information.

## 4. Data Processing

4.1 The Application has no backend service and does not store any personal information or other information in any form, including but not limited to user-provided prompts, images, videos, or documents.

4.2 All data provided by users is instantly transmitted to the relevant Vertex AI APIs through the Application, and all information and data returned by the APIs are instantly displayed to users through the browser.

4.3 When users finish using the Application (e.g., closing the browser or clearing the conversation history), all data and information generated during this process will be immediately cleared. This is determined by the code mechanism and logic of the Application.

4.4 The Application has no cookie settings, and each login is a brand new visit.

## 5. Intellectual Property

The Application is an open-source application, and all related intellectual property rights belong to the developer. The Streamlit framework used by the Application and the Google Cloud Vertex AI API belong to their respective developers. Users who copy or modify any part of the Application should indicate the source. Users may not use the Application for commercial purposes.

## 6. Disclaimer

6.1 The Application is provided "as is" without any express or implied warranties.

6.2 The Application is hosted on Streamlit's application hosting service and does not guarantee uninterrupted or error-free operation, nor does it guarantee that any defects will be corrected.

6.3 The Application is provided free of charge to users and is not responsible for any direct, indirect, incidental, special, or consequential damages arising from its use.

6.4 The Application is a generative AI application and is not responsible for the results or information generated by GenAI. Users should independently verify the reliability and authenticity of the generated information and decide on their own how to adopt and use the generated information.

## 7. Service Changes and Termination

The Application reserves the right to modify or terminate at any time without prior notice.

## 8. Applicable Law

These terms are governed by the laws of the State of California, without regard to its conflict of law principles.

## 9. Changes to Terms

The Application may update these terms of service from time to time. We will post notice of any significant changes on this page. Continued use of the Application indicates your acceptance of any such changes.

## 10. Contact Us

If you have any questions about these terms of service, please contact: """ + f"{st.secrets['developer_email']}" + ".")
