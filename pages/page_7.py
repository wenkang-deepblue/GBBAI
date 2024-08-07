import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Tool
import vertexai.preview.generative_models as generative_models
import io
import uuid
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# 初始化会话状态
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_file' not in st.session_state:
    st.session_state.current_file = None
if 'file_key' not in st.session_state:
    st.session_state.file_key = 0
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'need_api_call' not in st.session_state:
    st.session_state.need_api_call = False

def reset_conversation():
    st.session_state.messages = []
    st.session_state.current_file = None
    st.session_state.file_uploaded = False
    st.session_state.file_key += 1
    st.session_state.need_api_call = False
    if 'model' in st.session_state and 'current_role' in st.session_state:
        st.session_state.chat = st.session_state.model.start_chat()
    else:
        st.session_state.pop('chat', None)

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.44,0.36,0.3])
with cent_co:
    st.caption(":blue[_企业级聊天机器人_]")
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
    # 添加"开始新的对话"按钮
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("开始新的对话", use_container_width=True):
            reset_conversation()
            st.experimental_rerun()
        
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
        
# 用于处理上传的文件
def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_id = str(uuid.uuid4())
        # 读取文件内容
        file_content = uploaded_file.getvalue()
        # 获取MIME类型
        mime_type = uploaded_file.type
        # 将文件内容编码为base64
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        
        st.session_state.current_file = {
            'id': file_id,
            'mime_type': mime_type,
            'data': encoded_content,
            'raw_data': file_content
        }
        st.session_state.file_uploaded = True

def clear_file():
    st.session_state.current_file = None
    st.session_state.file_uploaded = False
    st.session_state.file_key += 1
 
def generate_text(prompt, chat, file_data=None):
    message_parts = [prompt]
    
    # 如果有文件数据,添加到消息中
    if file_data:
        message_parts.append(Part.from_data(mime_type=file_data['mime_type'], data=file_data['data']))
            
    response = chat.send_message(
        message_parts,
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    return response

# 定义模型参数
generation_config = {
    "max_output_tokens": 8192,
    "temperature": temperature,
    "top_p": top_p,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

# 初始化Streamlit应用
if "current_role" not in st.session_state or "model" not in st.session_state:
    st.session_state.current_role = None
    st.session_state.model = None

if system_instruction_option and (system_instruction_option != st.session_state.current_role or st.session_state.model is None):
    st.session_state.current_role = system_instruction_option
    st.session_state.messages = []
    st.session_state.model = GenerativeModel(
        "gemini-1.5-pro",
        system_instruction=system_instruction_option
    )
    st.session_state.chat = st.session_state.model.start_chat()

# 创建一个容器来放置所有的对话内容
chat_container = st.container()

# 在容器中显示聊天历史和新消息
with chat_container:
    # 显示聊天历史
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
        if "file" in msg:
            file_data = msg["file"]
            if 'image' in file_data['mime_type']:
                st.image(file_data['raw_data'])
            elif 'video' in file_data['mime_type']:
                st.video(file_data['raw_data'])

    # 处理新的API调用和响应
    if st.session_state.need_api_call:
        with st.chat_message("assistant"):
            thinking_placeholder = st.empty()
            thinking_placeholder.image("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")
            response = generate_text(st.session_state.messages[-1]["content"], st.session_state.chat, st.session_state.current_file if st.session_state.file_uploaded else None)
            assistant_msg = response.candidates[0].content.parts[0].text
            thinking_placeholder.empty()
            st.write(assistant_msg)
            st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
            st.session_state.need_api_call = False
            if st.session_state.file_uploaded:
                clear_file()
            
uploaded_file = st.file_uploader("上传图片或视频文件", type=['jpg', 'jpeg', 'png', 'mp4'], key=f"file_uploader_{st.session_state.file_key}")

if uploaded_file is not None:
    process_uploaded_file(uploaded_file)

# 显示当前上传的文件
if st.session_state.current_file:
    file_data = st.session_state.current_file
    if 'image' in file_data['mime_type']:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:  # 在中间列中显示图片
            st.image(file_data['raw_data'], caption='当前上传的图片', use_column_width=True)
    elif 'video' in file_data['mime_type']:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.video(file_data['raw_data'], start_time=0)
    else:
        st.warning("上传的文件类型不支持预览。")

# 聊天输入
user_input = st.chat_input("输入您的消息")

if user_input:
    if not st.session_state.current_role:
        st.error("👈请定义一种角色：在菜单中选择或者自定义")
        st.stop()
    else:
        user_message = {"role": "user", "content": user_input}
        if st.session_state.current_file and st.session_state.file_uploaded:
            user_message["file"] = st.session_state.current_file

        st.session_state.messages.append(user_message)
        st.session_state.need_api_call = True
        st.experimental_rerun()
