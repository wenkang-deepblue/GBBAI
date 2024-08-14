import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="GBB AI", page_icon="👋")

# Google客户端ID（替换为您的实际ID）
GOOGLE_CLIENT_ID = "210890376426-vmftp13cdmbmd723rcht9916s9eaf4rs.apps.googleusercontent.com"

def verify_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        return idinfo
    except ValueError:
        return None

def is_valid_email_domain(email):
    allowed_domains = ['google.com']
    domain = email.split('@')[-1]
    return domain in allowed_domains

if 'user' not in st.session_state:
    st.session_state["user"] = None

def main():  
    # 显示Google登录按钮
    st.components.v1.html(
        f"""
        <script src="https://accounts.google.com/gsi/client" async defer></script>
        <div id="g_id_onload"
             data-client_id="{GOOGLE_CLIENT_ID}"
             data-callback="handleCredentialResponse">
        </div>
        <div class="g_id_signin" data-type="standard"></div>
        <script>
        function handleCredentialResponse(response) {{
            const credential = response.credential;
            window.parent.postMessage({{type: "GOOGLE_AUTH", credential: credential}}, "*");
        }}
        </script>
        """,
        height=50
    )

    # 处理从JavaScript接收到的消息
    # 处理从JavaScript接收到的消息
if st.session_state["user"] is None:
    message = st.query_params.get("message")
    if message and message == "GOOGLE_AUTH":
        credential = st.query_params.get("credential")
        if credential:
            user_info = verify_google_token(credential)
            if user_info and is_valid_email_domain(user_info['email']):
                st.session_state["user"] = user_info
                st.experimental_rerun()
            elif user_info:
                st.error('请使用@google.com邮箱登录')
            else:
                st.error('登录验证失败。')

    if st.session_state["user"]:
        st.image("../rag-demo/pdf/galaxy banner with logo.png")
        st.write(f"# 您好，{st.session_state['user']['email']}！欢迎使用 :blue[GBB] :rainbow[AI] !")
        st.markdown(
            """
            GBB AI项目是利用:blue[Google Cloud Vertex AI]平台搭建的GenAI系统，其目的是演示Vertex AI各个模块可为企业实现的内容生成，媒体理解，RAG检索增强生成以及媒体搜索等功能。该项目所用到的Vertex AI模块包括：:orange[Gemini 1.5 Pro多模态模型，Agent Builder - Vertex AI Search，Imagen，DialogFlow]等等。Google Cloud中国销售及架构师团队愿意全力协助您利用Google强大的AI基础能力，以及GCP全面的AI生态及技术架构，搭建企业级的AI应用，帮助您的企业快速迭代，灵活开发，降低成本，提高效率。
            
            **👈 请点击左边开始体验吧！**
            """
        )

        with st.sidebar:
            left_co, cent_co, last_co = st.columns([0.34, 0.33, 0.33])
            with cent_co:
                st.image('../rag-demo/pdf/image2.gif')
            left_co, cent_co, last_co = st.columns([0.36, 0.32, 0.32])
            with cent_co:
                st.title(":blue[GBB] :rainbow[AI]")
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
            left_co, cent_co, last_co = st.columns([0.39, 0.31, 0.30])
            with cent_co:
                st.write('© GBB')
            left_co, cent_co, last_co = st.columns([0.09, 0.83, 0.08])
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
    else:
        st.write("# 欢迎使用 GBB AI")
        st.write("请登录以访问完整功能。")

if __name__ == "__main__":
    main()
