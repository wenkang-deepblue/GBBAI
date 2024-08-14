import streamlit as st
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests


st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

st.image("https://storage.googleapis.com/ghackathon/galaxy%20banner%20with%20logo.png")


st.write("# 您好！欢迎使用 :blue[GCP Gen]:rainbow[AI] !")


st.markdown(
    """
    GCP GenAI项目是利用:blue[Google Cloud Vertex AI]平台搭建的GenAI系统，其目的是演示Vertex AI各个模块可为企业实现的内容生成，媒体理解，RAG检索增强生成以及媒体搜索等功能。该项目所用到的Vertex AI模块包括：:orange[Gemini 1.5 Pro多模态模型，Agent Builder - Vertex AI Search，Imagen，DialogFlow]等等。Google Cloud中国销售及架构师团队愿意全力协助您利用Google强大的AI基础能力，以及GCP全面的AI生态及技术架构，搭建企业级的AI应用，帮助您的企业快速迭代，灵活开发，降低成本，提高效率。
    
    
    
"""
)

st.markdown(
    """
    **👈 请点击左边开始体验吧！**
    
    
"""
)

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
        st.write('© LWK')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.markdown(
    '<p style="text-align: center;">'
    '<span style="color: grey;">Designed & Developed by</span> '
    f'<a href="{st.secrets["developer_profile_link"]}" '
    'style="color: #185ABC; text-decoration: underline;" target="_blank">{st.secrets["developer_name"]}</a>'
    '</p>',
    unsafe_allow_html=True
)
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')

    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="隐私政策", icon="🔒")
