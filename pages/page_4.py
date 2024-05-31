import streamlit as st
import requests
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import json

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

base_url = "https://discoveryengine.googleapis.com/v1alpha"

endpoint_url = f"{base_url}/projects/210890376426/locations/global/collections/default_collection/dataStores/lwk-rag-search-data-store_1713579228500/conversations/-:converse"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(creds.token),
}

# streamlit UI
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.34,0.36,0.3])
with cent_co:
    st.caption(":blue[_Enterprise Document Search Engine_]")
st.image('https://storage.googleapis.com/ghackathon/page_4.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

query = st.text_area("Please input your question:", "", placeholder="This database contains Google's financial reports from the past years. You can ask relevant questions, e.g. Who is the CFO of Google?")
body = {
    "query": {"input": query},
    "summarySpec": {
        "summaryResultCount": 5,
        "modelSpec": {"version": "preview"},
        "ignoreAdversarialQuery": True,
        "includeCitations": True,
    },
}

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
            uri_text = answer['reply']['summary']['summaryWithMetadata']['references'][0]['uri']  # get doc source gs:// uri
            page_number = answer['searchResults'][0]['document']['derivedStructData']['extractive_answers'][0]['pageNumber'] # get page number
        
            st.info(reply_text)
            st.markdown(f'<p style="display: inline-block;"><img src="https://storage.googleapis.com/ghackathon/PDF_logo.png" alt="Alt text" style="width: 45px; height: 55px;" /></p><a href="{uri_text}" style="padding-left: 10px;">{title}</a>', unsafe_allow_html=True)
            st.markdown(f' **Page Number:** {page_number}')

# steramlit UI
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
