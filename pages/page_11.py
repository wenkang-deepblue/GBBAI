import streamlit as st
import base64
import openai
from google.auth import default, transport
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
import re
from PIL import Image
import io
import base64
import requests

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]
creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# 刷新凭证
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# 初始化 Vertex AI
project_id = "lwk-genai-test"
location = "us-central1"
vertexai.init(project=project_id, location=location, credentials=creds)

# 设置 OpenAI 客户端的 URL
url = f"https://us-central1-aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/{location}/endpoints/openapi"

# 创建 OpenAI 客户端
client = openai.OpenAI(
    base_url=url,         
    api_key=creds.token,
)

APP_ID = "llama_chat"

def load_gif(gif_url):
    response = requests.get(gif_url)
    if response.status_code == 200:
        contents = response.content
        data_url = base64.b64encode(contents).decode("utf-8")
        return f"data:image/gif;base64,{data_url}"
    else:
        st.error(f"无法加载GIF图像：HTTP状态码 {response.status_code}")
        return ""

# 加载GIF图片
thinking_gif = load_gif("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.43,0.37,0.3])
with cent_co:
    st.caption(":blue[_Llama3.1聊天机器人_]")
st.image('https://storage.googleapis.com/ghackathon/page_18_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

#继续streamlit sidebar界面
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GBB] :rainbow[AI]")
    temperature = st.slider("调整模型Temperature", min_value=0.0, max_value=2.0, value=1.0, help=(
        """
        Temperature用于响应生成期间的采样，这发生在应用 topP 和 topK 时。Temperature控制了token选择中的随机程度。对于需要较少开放式或创造性响应的提示，较低的temperature是好的，而较高的temperature可以导致更多样化或创造性的结果。Temperature为 0 意味着始终选择最高概率的token。在这种情况下，给定提示的响应大多是确定的，但仍有可能出现少量变化。
        
        如果模型返回的响应过于通用、太短或模型给出回退响应，请尝试提高temperature。
        """
    ))
    top_p = st.slider ("调整模型Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P 改变了模型选择输出tokens的方式。Tokens按照从最可能（见top-K）到最不可能的顺序进行选择，直到它们的概率之和等于top-P值。例如，如果token A、B和C的概率分别为0.3、0.2和0.1，top-P值为0.5，那么模型将使用温度从A或B中选择下一个token，并排除C作为候选。

        指定较低的值会得到较少的随机响应，指定较高的值会得到更多的随机响应。
        """
    ))
    
    generic_chat = "你是一个乐于助人的人类助手，请用用户跟你对话的语言来进行与用户的对话"
    python_expert = "你是一个python专家，可以帮助用户生成python代码，解释python代码，完善python代码"
    
    st.subheader('', divider='rainbow')
    
    system_instruction_option = ""
        
    system_instruction_option1 = st.radio(
        "请选择AI的角色：",
        ("友好的助手", "Python专家", "自定义"),
        index=None,
    )
    
    if system_instruction_option1 == "自定义":
        system_instruction_option2 = st.text_area ("请在此自由定义AI的角色：", "")
        submitted = st.button("提交")
        if submitted:
            st.session_state.custom_role_description = system_instruction_option2
    
    if system_instruction_option1 == "友好的助手":
        system_instruction_option = generic_chat
    elif system_instruction_option1 == "Python专家":
        system_instruction_option = python_expert
    elif system_instruction_option1 == "自定义" and "custom_role_description" in st.session_state:
        system_instruction_option = st.session_state.custom_role_description
    
    if system_instruction_option:
        st.write(f"您选择的AI角色描述为：{system_instruction_option}")
    else:
        st.error("请选择或定义AI角色")
   
    st.text("")
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
    left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
    with cent_co:
        st.write('© GBB')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.write(':grey[Designed & Developed by] :blue[李文康]')
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')

# LLaMA model
MODEL_ID = 'meta/llama3-405b-instruct-maas'

def generate_text(messages):
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=4000,
    )
    
    # 获取消息内容
    content = response.choices[0].message.content
    
    # 移除开头的多个"assistant"
    content = re.sub(r'\n+', '', re.sub(r'^(assistant)+', '', content).lstrip())
   
    # 返回处理后的消息内容
    return content.strip()
    
# 初始化Streamlit应用
if f"{APP_ID}_messages" not in st.session_state:
    st.session_state[f"{APP_ID}_messages"] = []
if f"{APP_ID}_current_role" not in st.session_state:
    st.session_state[f"{APP_ID}_current_role"] = None

if system_instruction_option and system_instruction_option != st.session_state[f"{APP_ID}_current_role"]:
    st.session_state[f"{APP_ID}_current_role"] = system_instruction_option
    st.session_state[f"{APP_ID}_messages"] = [{"role": "system", "content": system_instruction_option}]

for msg in st.session_state.get(f"{APP_ID}_messages", [])[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not st.session_state.get(f"{APP_ID}_current_role"):
        st.error("👈请定义一种角色：在菜单中选择或者自定义")
        st.stop()
    else:
        st.session_state[f"{APP_ID}_messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # 创建一个空的占位符来显示GIF
        gif_placeholder = st.empty()

        # 显示GIF，不包含任何文本
        gif_placeholder.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="{thinking_gif}" alt="" style="width:30px;">'
            f'</div>',
            unsafe_allow_html=True
        )

        # 生成AI响应
        response = generate_text(st.session_state[f"{APP_ID}_messages"])

        # 移除GIF
        gif_placeholder.empty()

    st.session_state[f"{APP_ID}_messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
