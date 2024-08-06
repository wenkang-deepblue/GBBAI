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

# 设置Discovery Engine API变量
base_url = "https://discoveryengine.googleapis.com/v1alpha"

# 创建endpoint URL
endpoint_url = f"{base_url}/projects/210890376426/locations/global/collections/default_collection/dataStores/lwk-rag-search-data-store_1713579228500/conversations/-:converse"

# 设置请求报头
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(creds.token),
}

# streamlit界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.39,0.31,0.3])
with cent_co:
    st.caption(":blue[_企业级RAG搜索引擎_]")
st.image('https://storage.googleapis.com/ghackathon/page_2_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# steramlit界面
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GBB] :rainbow[AI]")
    st.page_link("homepage.py", label="主页", icon="🏠")
    st.page_link("pages/page_0.py", label="文本生成", icon="📖")
    st.page_link("pages/page_9.py", label="视频理解", icon="🎞️")
    st.page_link("pages/page_13.py", label="文本翻译", icon="🇺🇳")
    st.page_link("pages/page_2.py", label="RAG搜索", icon="🔍")
    st.page_link("pages/page_3.py", label="媒体搜索", icon="🎥")
    st.page_link("pages/page_16.py", label="图片生成", icon="🎨")
    st.page_link("pages/page_18.py", label="聊天机器人", icon="💬")
    st.page_link("pages/page_15.py", label="游戏客服平台", icon="🤖")
    st.page_link("pages/page_21.py", label="电商客服平台", icon="🤖")
    st.page_link("pages/page_19.py", label="Claude3.5聊天机器人", icon="💬")
    st.page_link("pages/page_23.py", label="Llama3.1聊天机器人", icon="💬")
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
    - [:cloud: Google Cloud Vertex AI](https://cloud.google.com/vertex-ai?hl=en)

    """
    )
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
    with cent_co:
        st.write('© GBB')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.write(':grey[Designed & Developed by] :blue[李文康]')
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')

# 设置查询提示词
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

# 设置结果返回结果关键词以展示相应图片
content_dict = {
    "以色列": {
        "image": "../rag-demo/pdf/以色列.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%A5%E8%89%B2%E5%88%97%EF%BC%9A%E4%B8%80%E4%B8%AA%E5%9B%BD%E5%AE%B6%E7%9A%84%E8%AF%9E%E7%94%9F.pdf"
    },
    "微积分": {
        "image": "../rag-demo/pdf/微积分.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%85%AB%E5%8D%A6%E5%BE%AE%E7%A7%AF%E5%88%86.pdf"
    },
    "量子": {
        "image": "../rag-demo/pdf/量子通信.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1.pdf"
    },
    "考古": {
        "image": "../rag-demo/pdf/考古现场.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%9B%B4%E8%A7%82%E8%80%83%E5%8F%A4%E7%8E%B0%E5%9C%BA.pdf"
    },
    "近视": {
        "image": "../rag-demo/pdf/近视.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E8%BF%91%E8%A7%86%E6%80%8E%E4%B9%88%E5%8A%9E.pdf"
    },
    "故事":{
        "image": "../rag-demo/pdf/写故事.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%86%99%E6%95%85%E4%BA%8B.pdf"
    }
}

# 向Discovery Engine API发送POST请求
with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
    with cent_co:
        submitted = st.form_submit_button("提交")
    if submitted:
        with st.spinner('正在处理，不要着急哦，答案正在路上...'):
            response = requests.post(endpoint_url, headers=headers, json=body)
            answer = response.json()["reply"]["reply"]
        
            st.info(response.json()["reply"]["reply"] if response.status_code == 200 else response.text)
# 检查请求响应代码并返回请求结果

    # 检查回答是否包含关键词，并展示对应的图片和链接
    
            for keyword in content_dict:
                if keyword in answer:
                    content=content_dict[keyword]
                    left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
                    with cent_co:
                        st.image(content["image"])
                    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
                    with cent_co:
                        st.write(f'[在线阅读]({content["file"]})')         
                    break  # 只展示第一个匹配的关键词
            else:
                st.write("未找到匹配关键词")
