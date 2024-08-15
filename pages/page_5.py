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
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.39,0.31,0.3])
with cent_co:
    st.caption(":blue[_企业级媒体搜索引擎_]")
st.image('https://storage.googleapis.com/ghackathon/page_3_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
    st.page_link("homepage.py", label="主页", icon="🏠")
    st.page_link("pages/page_1.py", label="文本生成", icon="📖")
    st.page_link("pages/page_2.py", label="视频理解", icon="🎞️")
    st.page_link("pages/page_3.py", label="文本翻译", icon="🇺🇳")
    st.page_link("pages/page_12.py", label="旅游顾问", icon="✈️")
    st.page_link("pages/page_4.py", label="RAG搜索", icon="🔍")
    st.page_link("pages/page_5.py", label="媒体搜索", icon="🎥")
    st.page_link("pages/page_6.py", label="图片生成", icon="🎨")
    st.page_link("pages/page_7.py", label="聊天机器人", icon="💬")
    st.page_link("pages/page_8.py", label="游戏客服平台", icon="🤖")
    st.page_link("pages/page_9.py", label="电商客服平台", icon="🤖")
    st.page_link("pages/page_10.py", label="Claude3.5聊天机器人", icon="💬")
    st.page_link("pages/page_11.py", label="Llama3.1聊天机器人", icon="💬")
    st.page_link("https://pantheon.corp.google.com/translation/hub", label="GCP翻译门户", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/gallery", label="GCP控制台 - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/engines", label="GCP控制台 - App Builder", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.markdown(
        """
    ## 关于
    这是由:blue[Google Cloud Vertex AI]驱动的生成式AI平台以及企业级RAG搜索引擎
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

    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="隐私政策", icon="🔒")

# Set the request body
query = st.text_area("请输入您的问题:", "")  # Replace this with your actual query
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
        "file": "https://storage.googleapis.com/lwk-rag-videos/video_5.mp4"
    },
    "机器人": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Wall-E.jpg",
        "file": "https://storage.googleapis.com/lwk-rag-videos/video_1.mp4"
    },
    "爱你": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/I-wanna-go-to-your-world-to-love-you.png",
        "file": "https://storage.googleapis.com/lwk-rag-videos/video_2.mp4"
    },
    "春暖花开": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/meet%20you%20in%20spring.jpeg",
        "file": "https://storage.googleapis.com/lwk-rag-videos/video_4.mp4"
    },
    "哈利": {
        "image": "https://storage.googleapis.com/lwk-rag-videos/Harry%20Porter%20and%20Philosopher's%20Stone.jpg",
        "file": "https://storage.googleapis.com/lwk-rag-videos/video_3.mp4"
    }
}

# Make the POST request to the Discovery Engine API
with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
    with cent_co:
        submitted = st.form_submit_button("提交")
    if submitted:
        with st.spinner('正在处理，不要着急哦，答案正在路上...'):
            response = requests.post(endpoint_url, headers=headers, json=body)
            answer = response.json()["reply"]["reply"]
        
            st.info(response.json()["reply"]["reply"] if response.status_code == 200 else response.text)
# Check the status code of the response and print the response body

    # 检查回答是否包含关键词，并展示对应的图片和链接
    
            for keyword in content_dict:
                if keyword in answer:
                    content=content_dict[keyword]
                    left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
                    with cent_co:
                        st.image(content["image"])
                    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
                    with cent_co:
                        st.write(f'[在线观看]({content["file"]})')         
                    break  # 只展示第一个匹配的关键词
            else:
                st.write("未找到匹配关键词")
