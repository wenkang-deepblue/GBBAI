import streamlit as st
import base64
from anthropic import AnthropicVertex
import httpx
import io
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
from PIL import Image

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# 初始化AnthropicVertex客户端
client = AnthropicVertex(region="europe-west1", project_id="lwk-genai-test", credentials=creds)

APP_ID = "claude_chat"

def get_custom_loading_gif():
    with open("../rag-demo/pages/typing-dots.gif", "rb") as f:
        contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")
    
    # 移除alt文本，调整样式以适应您的布局
    return f'<img src="data:image/gif;base64,{data_url}" style="display: block; margin: auto; width: 30px;">'

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.43,0.37,0.3])
with cent_co:
    st.caption(":blue[_Claude 3.5 聊天机器人_]")
st.image('https://storage.googleapis.com/ghackathon/page_18_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# 初始化会话状态
if f"{APP_ID}_messages" not in st.session_state:
    st.session_state[f"{APP_ID}_messages"] = []
if f"{APP_ID}_current_image" not in st.session_state:
    st.session_state[f"{APP_ID}_current_image"] = None

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GBB] :rainbow[AI]")
    st.page_link("homepage.py", label="主页", icon="🏠")
    st.page_link("pages/page_1.py", label="文本生成", icon="📖")
    st.page_link("pages/page_2.py", label="视频理解", icon="🎞️")
    st.page_link("pages/page_3.py", label="文本翻译", icon="🇺🇳")
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
        st.write('© GBB')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.write(':grey[Designed & Developed by] :blue[李文康]')
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')
    
chat_container = st.container()

# 显示聊天消息
with chat_container:
    for message in st.session_state[f"{APP_ID}_messages"]:
        with st.chat_message(message["role"]):
            if isinstance(message["content"], dict):
                if message["content"].get("type") == "text":
                    st.write(message["content"].get("text", ""))
                elif message["content"].get("type") == "image":
                    st.image(message["content"].get("image"))
                elif message["content"].get("type") == "image_and_text":
                    st.image(message["content"].get("image"))
                    st.write(message["content"].get("text", ""))
            elif isinstance(message["content"], str):
                st.write(message["content"])
                
gif_placeholder = st.empty()
    
uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.session_state[f"{APP_ID}_current_image"] = image
    st.image(image, caption="上传的图片", use_column_width=True)

# 聊天输入
user_input = st.chat_input("在这里输入你的消息...")

left_co, cent_co,last_co = st.columns([0.41,0.34,0.27])
with cent_co:
    if st.button("清除聊天记录"):
        st.session_state[f"{APP_ID}_messages"] = []
        st.session_state[f"{APP_ID}_current_image"] = None
        st.experimental_rerun()

if user_input:
    # 准备新的用户消息
    new_user_message = {"role": "user", "content": {}}
    
    if st.session_state[f"{APP_ID}_current_image"]:
        img_byte_arr = io.BytesIO()
        current_image = st.session_state[f"{APP_ID}_current_image"]
        if current_image:
            current_image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            img_base64 = base64.b64encode(img_byte_arr).decode("utf-8")
            
            new_user_message["content"]["type"] = "image_and_text"
            new_user_message["content"]["image"] = current_image
            new_user_message["content"]["image_base64"] = img_base64
            new_user_message["content"]["text"] = user_input
            
            with st.chat_message("user"):
                st.image(current_image)
                st.write(user_input)
        
        # 清除当前图片，确保后续文本输入不会再附加图片
        st.session_state[f"{APP_ID}_current_image"] = None
        uploaded_file = None
            
    elif user_input:
        new_user_message["content"]["type"] = "text"
        new_user_message["content"]["text"] = user_input
        
        with chat_container.chat_message("user"):
            st.write(user_input)
    
    # 将新消息添加到会话历史
    st.session_state[f"{APP_ID}_messages"].append(new_user_message)
    
    # 准备发送给Claude的消息历史
    claude_messages = []
    for msg in st.session_state[f"{APP_ID}_messages"]:
        if isinstance(msg["content"], dict):
            if msg["content"].get("type") == "text":
                claude_messages.append({"role": msg["role"], "content": [{"type": "text", "text": msg["content"].get("text", "")}]})
            elif msg["content"].get("type") == "image_and_text":
                claude_messages.append({
                    "role": msg["role"],
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": msg["content"].get("image_base64", ""),
                            },
                        },
                        {
                            "type": "text",
                            "text": msg["content"].get("text", "")
                        }
                    ]
                })
        elif isinstance(msg["content"], str):
            claude_messages.append({"role": msg["role"], "content": [{"type": "text", "text": msg["content"]}]})
        
    # 获取Claude的响应
    gif_placeholder.markdown(get_custom_loading_gif(), unsafe_allow_html=True)
        
    try:
        response = client.messages.create(
            max_tokens=4096,
            messages=claude_messages,
            model="claude-3-5-sonnet@20240620",
        )
    
        # 显示Claude的响应
        assistant_response = response.content[0].text
        st.session_state[f"{APP_ID}_messages"].append({"role": "assistant", "content": {"type": "text", "text": assistant_response}})
        with chat_container.chat_message("assistant"):
            st.write(assistant_response)
    finally:
        gif_placeholder.empty()

elif st.session_state[f"{APP_ID}_current_image"]:
    st.warning("请输入提示词")
