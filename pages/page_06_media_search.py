import streamlit as st
import requests
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import json
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
            
credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

base_url = "https://discoveryengine.googleapis.com/v1alpha"

endpoint_url = f"{base_url}/projects/210890376426/locations/global/collections/default_collection/dataStores/lwk-media-search_1714306590615/conversations/-:converse"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(creds.token),
}

left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.41,0.31,0.28])
with cent_co:
    st.caption(":blue[_Enterprise-ready Media Search Engine_]")
st.image('https://storage.googleapis.com/ghackathon/page_3_zh.png')
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

query = st.text_area("Please input your question:", "")
body = {
    "query": {"input": query},
    "summarySpec": {
        "summaryResultCount": 5,
        "modelSpec": {"version": "preview"},
        "ignoreAdversarialQuery": True,
        "includeCitations": True,
    },
}

content_dict = {
    "飞屋": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Up.jpg",
        "file": "https://storage.googleapis.com/media-rag-search-videos/video_1.mp4"
    },
    "机器人": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Wall-E.jpg",
        "file": "https://storage.googleapis.com/media-rag-search-videos/video_3.mp4"
    },
    "爱你": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/I-wanna-go-to-your-world-to-love-you.png",
        "file": "https://storage.googleapis.com/media-rag-search-videos/video_2.mp4"
    },
    "春暖花开": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/meet%20you%20in%20spring.jpeg",
        "file": "https://storage.googleapis.com/media-rag-search-videos/video_4.mp4"
    },
    "哈利": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Harry%20Porter%20and%20Philosopher's%20Stone.jpg",
        "file": "https://storage.googleapis.com/media-rag-search-videos/video_5.mp4"
    }
}

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
    with cent_co:
        submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner('Processing, please be patient, the answer is on its way...'):
            response = requests.post(endpoint_url, headers=headers, json=body)
            answer = response.json()["reply"]["reply"]
        
            st.info(response.json()["reply"]["reply"] if response.status_code == 200 else response.text)

    # Check if the answer contains keywords and display corresponding images and links
    
            for keyword in content_dict:
                if keyword in answer:
                    content=content_dict[keyword]
                    left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
                    with cent_co:
                        st.image(content["image"])
                    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
                    with cent_co:
                        st.write(f'[Watch Online]({content["file"]})')         
                    break  # Only display the first matching keyword
            else:
                st.write("No matching keywords found")
