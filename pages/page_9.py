import streamlit as st
import streamlit.components.v1 as components

def custom_page_link(url, label, icon, new_tab=False):
    
    if new_tab:
        st.markdown(
            f'''
            <div class="row-widget stPageLink" style="width: 282px; margin: -0.4rem 0 0.cbec99246ab9ab5rem 0;">
                <div class="st-emotion-cache-j7qwjs e11k5jya2" style="padding: 0;">
                    <a href="/{url}" target="_blank" rel="noopener noreferrer" 
                       class="st-emotion-cache-n7e918 e11k5jya1" style="display: flex; align-items: center;">
                        <span color="#31333F" class="st-emotion-cache-6jwljf eyeqlp52" style="margin-right: 0rem;">
                            <span data-testid="stIconEmoji" aria-hidden="true" 
                                  class="st-emotion-cache-8hkptd eyeqlp50">{icon}</span>
                        </span>
                        <span class="st-emotion-cache-pkbazv e11k5jya0">
                            <div data-testid="stMarkdownContainer" 
                                 class="st-emotion-cache-187vdiz e1nzilvr4">
                                <p style="margin: 0;">{label}</p>
                            </div>
                        </span>
                    </a>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.page_link(url, label=label, icon=icon)

# Streamlit UI
left_left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.38,0.32,0.3])
with cent_co:
    st.caption(":blue[_企业级客服机器人平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_15_zh.png')
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
    custom_page_link("https://gbb-ai.streamlit.app/page_8", label="游戏客服平台", icon="🤖")
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
    
    left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
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
""", height=600)
