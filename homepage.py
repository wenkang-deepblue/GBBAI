#import streamlit lib:
import streamlit as st

#this will showed on the top of user's
st.set_page_config(
    page_title="GBB AI",
    page_icon="👋",
)

st.image("https://storage.googleapis.com/ghackathon/galaxy%20banner%20with%20logo.png")


st.write("# Hello! Welcome to :blue[GBB] :rainbow[AI]!")


st.markdown(
    """
    The GBB AI project is a GenAI system built on :blue[Google Cloud Vertex AI] platform, aiming to demonstrate the capabilities of various Vertex AI modules for enterprises, such as content generation, media comprehension, RAG search, and media search. The Vertex AI modules used in this project include :orange[Gemini 1.5 Pro multimodal model, Agent Builder - Vertex AI Search, Imagen, DialogFlow]. Google Cloud China sales and engineering team is willing to fully assist you in building enterprise-level AI applications by leveraging Google's powerful AI foundation capabilities, as well as GCP's comprehensive AI ecosystem and technical architecture, to help your enterprise iterate quickly, develop flexibly, reduce costs, and improve efficiency.
    
    
    
"""
)

st.markdown(
    """
    **👈 Please click on the left for experiencing!**
    
    
"""
)

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
