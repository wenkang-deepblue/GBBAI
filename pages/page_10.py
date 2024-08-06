import streamlit as st
import streamlit.components.v1 as components

# Streamlit UI
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.27,0.53,0.1])
with cent_co:
    st.caption(":blue[_Enterprise Customer Service Chatbot Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_7.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# Embed Dialogflow code within an HTML component
components.html("""
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="lwk-genai-test"
  agent-id="da56aedf-e73e-4ae2-bcc3-ece9429c6328"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat
   chat-title="Google Store Assistant"
   chat-title-icon="https://storage.googleapis.com/ghackathon/GoogleG_FullColor_192px_3x.png"
   bot-writing-image="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/typing-2.gif"
   </df-messenger-chat>
</df-messenger>
<style>
    df-messenger {
        z-index: 999;
        position: fixed;
        --df-messenger-chat-border-radius: 10px;
        --df-messenger-titlebar-padding: 0 15px;
        --df-messenger-titlebar-icon-width: 25px;
        --df-messenger-titlebar-icon-height: 25px;
        --df-messenger-titlebar-icon-padding: 5px 10px 5px 230px;
        --df-messenger-titlebar-padding: 0;
        --df-messenger-titlebar-title-align: start;
        --df-messenger-titlebar-title-font-size: 20px;
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
""", height=600) # Adjust height as needed

with st.sidebar:
        left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
        with cent_co:
                st.image('https://storage.googleapis.com/ghackathon/image2.gif')
        left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
        with cent_co:
                st.title(":blue[GBB] :rainbow[AI]")
        st.page_link("homepage.py", label="Homepage", icon="🏠")
        st.page_link("pages/page_1.py", label="Article Generation", icon="📖")
        st.page_link("pages/page_2.py", label="Media Comprehension", icon="🎞️")
        st.page_link("pages/page_3.py", label="Text Translation", icon="🇺🇳")
        st.page_link("pages/page_4.py", label="Document Search", icon="🔍")
        st.page_link("pages/page_5.py", label="Media Search", icon="🎥")
        st.page_link("pages/page_6.py", label="Image Generation", icon="🎨")
        st.page_link("pages/page_7.py", label="Customer Service Chatbot", icon="🤖")
        st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/create/text?project=lwk-genai-test", label="GCP Console - Gemini", icon="🌎")
        st.page_link("https://pantheon.corp.google.com/gen-app-builder/locations/global/engines/lwk-rag-search_1713579191717/preview/search?e=13803378&mods=dm_deploy_from_gcs&project=lwk-genai-test", label="GCP Console - Vertex AI Searh", icon="🌎")
        st.text("")
        st.subheader('', divider='rainbow')
        st.text("")
        st.markdown(
            """
        ## About
        This is an enterprise readiness GenAI platform powered by :blue[Google Cloud Vertex AI]
        - [:cloud: Google Cloud Vertex AI](https://cloud.google.com/vertex-ai?hl=en)
    
        """
        )
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        left_co, cent_co,last_co = st.columns([0.3,0.4,0.30])
        with cent_co:
            st.write('© [Wenkang Li](https://moma.corp.google.com/person/wenkangli?q=image%20generatioin%20streamlit)')
        left_co, cent_co,last_co = st.columns([0.2,0.79,0.1])
        with cent_co:
            st.write(
            '''
            :grey[Designed & Developed by]
            :blue[Wenkang Li & Gunther Hua]'''
             )
        left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
        with cent_co:
            st.write(':grey[Powered by] **Vertex AI**')
