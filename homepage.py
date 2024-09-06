import streamlit as st
from auth import login, callback, logout

#this will showed on the top of user's
st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

if "code" in st.query_params:
    callback()

if not login():
    st.stop()

manual_link = st.secrets["manual_link"]

st.markdown(f"""
    <div style="background-color: #D2E3FC; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 20px;">
        <span style="color: #5F6368;">Click here to get</span>
        <a href="{manual_link}" target="_blank" style="color: #4285F4; text-decoration: underline; font-weight: bold; font-family: 'Google Sans', sans-serif;">
            GCP-GenAI Demo Manual
        </a>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">Welcome!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("log out"):
            logout()

st.image("https://storage.googleapis.com/ghackathon/galaxy%20banner%20with%20logo.png")


st.write("# Hi, there! Welcome to :blue[GCP Gen]:rainbow[AI]!")

st.markdown(
    """
    <div style="font-family: 'Google Sans', sans-serif;">
    The GCP GenAI project is a GenAI system built using the <span style="color: #1A73E8;">Google Cloud Vertex AI</span> platform. Its purpose is to demonstrate various functionalities that Vertex AI modules can achieve for enterprises, including content generation, media understanding, RAG (Retrieval-Augmented Generation), and media search. The project utilizes Vertex AI modules such as <span style="color: orange;">Gemini 1.5 Pro multimodal model, Agent Builder - Vertex AI Search, Imagen, DialogFlow</span>, and more. The Google Cloud Sales and Architecture team is committed to fully assisting you in leveraging Google's powerful AI foundational capabilities, as well as GCP's comprehensive AI ecosystem and technical architecture, to build enterprise-level AI applications. Our goal is to help your enterprise iterate quickly, develop flexibly, reduce costs, and improve efficiency.
    </div>
    """,
    unsafe_allow_html=True
)

st.text("")

st.markdown(
    """
    **👈 Please click on the left to start experiencing!**
    
    
"""
)

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.3,0.5,0.2])
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
    This is a generative AI platform and enterprise-ready RAG search engine powered by :blue[Google Cloud Vertex AI]
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
    st.text("")
    st.text("")
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
