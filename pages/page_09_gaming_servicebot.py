import streamlit as st
import streamlit.components.v1 as components
from auth import login, callback, logout

if "code" in st.query_params:
    callback()

if not login():
    st.stop()

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

def custom_page_link(url, label, icon, new_tab=False):
    
    if new_tab:
        st.markdown(
            f'''
            <div class="row-widget stPageLink" style="width: 282px; margin: -0.4rem 0 0.65rem 0;">
                <div class="st-emotion-cache-j7qwjs e11k5jya2" style="padding: 0;">
                    <a href="/{url}" target="_blank" rel="noopener noreferrer" 
                       class="st-emotion-cache-n7e918 e11k5jya1" style="display: flex; align-items: center;">
                        <span color="#31333F" class="st-emotion-cache-6jwljf eyeqlp52" style="margin-right: 0rem;">
                            <span data-testid="stIconEmoji" aria-hidden="true" 
                                  class="st-emotion-cache-8hkptd eyeqlp50">{icon}</span>
                        </span>
                        <span class="st-emotion-cache-pkbazv e11k5jya0">
                            <div data-testid="stMarkdownContainer" 
                                 class="st-emotion-cache-187vdiz e1nzilvr4">
                                <p style="margin: 0;">{label}</p>
                            </div>
                        </span>
                    </a>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.page_link(url, label=label, icon=icon)

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.4,0.32,0.28])
with cent_co:
    st.caption(":blue[_Enterprise-ready Customer Service Bot Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_15_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
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

# Embed Dialogflow code within an HTML component
components.html("""
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="lwk-genai-test"
  agent-id="6cff449c-8ce8-44d8-982d-b8f49a55bc00"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat
   chat-title="Game Assistant"
   chat-title-icon="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/Blizzard_Entertainment_Logo.png"
   bot-writing-image="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/typing-2.gif"
   </df-messenger-chat>
</df-messenger>
<style>
    df-messenger {
        z-index: 999;
        position: fixed;
        --df-messenger-chat-border-radius: 10px;
        --df-messenger-titlebar-padding: 0 15px;
        --df-messenger-titlebar-icon-width: 70px;
        --df-messenger-titlebar-icon-height: 37px;
        --df-messenger-titlebar-icon-padding: 5px 10px 5px 208px;
        --df-messenger-titlebar-padding: 0;
        --df-messenger-titlebar-title-align: start;
        --df-messenger-titlebar-title-font-size: 30px;
        --df-messenger-titlebar-font-color: #000;
        --df-messenger-font-color: #1967D2;
        --df-messenger-font-family: Google Sans;
        --df-messenger-chat-background: #f3f6fc;
        --df-messenger-message-user-background: #D2E3FC;
        --df-messenger-message-user-font-color: #1967D2;
        --df-messenger-message-bot-background: #CEEAD6;
        --df-messenger-message-bot-font-color: #000;
        --df-messenger-chat-scroll-button-enabled-display: flex;
        --df-messenger-chat-scroll-button-align: center;
        --df-messenger-chat-scroll-button-text-display: inline;
        --df-messenger-message-bot-writing-font-color: #9AA0A6;
        --df-messenger-message-bot-writing-image-width: 70px;
        --df-messenger-message-bot-writing-image-height: 14px;
        left: 0;
        top: 0;
        bottom: 0;
        width: 702px;
        margin: auto;
    }
</style>
""", height=600)
