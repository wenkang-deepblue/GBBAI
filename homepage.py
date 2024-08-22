import streamlit as st
from auth import login, callback, logout

#this will showed on the top of user's
st.set_page_config(
    page_title="GBB AI",
    page_icon="👋",
)

if "code" in st.query_params:
    callback()

if not login():
    st.stop()

manual_link = st.secrets["manual_link"]

st.markdown(f"""
    <div style="background-color: #D2E3FC; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 20px;">
        <span style="color: #5F6368;">请点击这里获取</span>
        <a href="{manual_link}" target="_blank" style="color: #4285F4; text-decoration: underline; font-weight: bold; font-family: 'Google Sans', sans-serif;">
            GCP-GenAI Demo手册
        </a>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">欢迎!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("log out"):
            logout()

st.image("https://storage.googleapis.com/ghackathon/galaxy%20banner%20with%20logo.png")


st.write("# 您好！欢迎使用 :blue[GCP Gen]:rainbow[AI] !")


st.markdown(
    """
    <div style="font-family: 'Google Sans', sans-serif;">
    GCP GenAI项目是利用<span style="color: #1A73E8;">Google Cloud Vertex AI</span>平台搭建的GenAI系统，其目的是演示Vertex AI各个模块可为企业实现的内容生成，媒体理解，RAG检索增强生成以及媒体搜索等功能。该项目所用到的Vertex AI模块包括：<span style="color: orange;">Gemini 1.5 Pro多模态模型，Agent Builder - Vertex AI Search，Imagen，DialogFlow</span>等等。Google Cloud中国销售及架构师团队愿意全力协助您利用Google强大的AI基础能力，以及GCP全面的AI生态及技术架构，搭建企业级的AI应用，帮助您的企业快速迭代，灵活开发，降低成本，提高效率。
    </div>
    """,
    unsafe_allow_html=True
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
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.24])
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

    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="隐私政策", icon="🔒")
