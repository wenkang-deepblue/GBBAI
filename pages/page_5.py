import streamlit as st
import requests
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import json

# Get the credentials from the Service Account key
credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# Set the base URL for the Discovery Engine API
base_url = "https://discoveryengine.googleapis.com/v1alpha"

# Construct the endpoint URL
endpoint_url = f"{base_url}/projects/210890376426/locations/global/collections/default_collection/dataStores/lwk-media-search_1714306590615/conversations/-:converse"

# Set the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(creds.token),
}

left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.caption(":blue[_Enterprise Media Search Engine_]")
st.image('https://storage.googleapis.com/ghackathon/page_5.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# Set the request body
query = st.text_area("Please input your question:", "", placeholder="e.g. Is there a movie about robot?")  # Replace this with your actual query
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
    "飞屋环游记": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Up.jpg",
        "file": "https://storage.googleapis.com/lwk-testing-files/video_1.mp4"
    },
    "机器人总动员": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Wall-E.jpg",
        "file": "https://storage.googleapis.com/lwk-testing-files/video_3.mp4"
    },
    "好想去你的世界爱你": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/I-wanna-go-to-your-world-to-love-you.png",
        "file": "https://storage.googleapis.com/lwk-testing-files/video_2.mp4"
    },
    "春暖花开去见你": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/meet%20you%20in%20spring.jpeg",
        "file": "https://storage.googleapis.com/lwk-testing-files/video_4.mp4"
    },
    "哈利波特与魔法石": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Harry%20Porter%20and%20Philosopher's%20Stone.jpg",
        "file": "https://storage.googleapis.com/lwk-testing-files/video_5.mp4"
    }
}

# Make the POST request to the Discovery Engine API
with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.3,0.28])
    with cent_co:
        submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner('Your question is processing, answer is upcoming...'):
            response = requests.post(endpoint_url, headers=headers, json=body)
            answer = response.json()
        
            reply_text = answer['reply']['reply']  # get text following 'reply'
            title = answer['reply']['summary']['summaryWithMetadata']['references'][0]['title']
            
            st.markdown(reply_text)

            for keyword in content_dict:
                if keyword in title:
                    content=content_dict[keyword]
                    left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
                    with cent_co:
                        st.image(content["image"])
                    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
                    with cent_co:
                        st.write(f'[Watch Online]({content["file"]})')         
                    break
            else:
                st.write("Can't find related information")

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
