import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import json
import logging

def process_credentials(cred_dict):
    # 处理多行私钥
    if 'private_key' in cred_dict:
        cred_dict['private_key'] = cred_dict['private_key'].replace('\\n', '\n')
    return cred_dict

try:
    # 获取 TOML 格式的凭证信息
    credentials_toml = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]
    
    # 将 TOML 格式转换为字典并处理
    credentials_dict = process_credentials(dict(credentials_toml))
    
    # 创建凭证对象
    creds = service_account.Credentials.from_service_account_info(
        credentials_dict,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    
    # 验证凭证
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    
    st.success("Successfully loaded and verified credentials!")
    
    # 显示非敏感的凭证信息
    safe_info = {k: v for k, v in credentials_dict.items() if k not in ['private_key', 'private_key_id']}
    st.write("Partial credential info (non-sensitive):", json.dumps(safe_info, indent=2))

except Exception as e:
    st.error(f"An error occurred while loading the credentials: {str(e)}")
    st.error("Please check the application logs for more details.")
    
    # 显示非敏感的凭证信息（即使在错误情况下）
    if 'credentials_dict' in locals():
        safe_info = {k: v for k, v in credentials_dict.items() if k not in ['private_key', 'private_key_id']}
        st.write("Partial credential info (non-sensitive):", json.dumps(safe_info, indent=2))

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.39,0.31,0.3])
with cent_co:
    st.caption(":blue[_企业级内容生成平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_0.png')
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
    temperature = st.slider("调整模型Temperature", min_value=0.0, max_value=2.0, value=1.5, help=(
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
    st.subheader('',divider='rainbow')
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

# 定义生成文本的函数
def generate_text(prompt):
  vertexai.init(project="lwk-genai-test", location="us-central1")
  model = GenerativeModel("gemini-1.5-flash-001")
  responses = model.generate_content(
      [prompt],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  generated_text = ""
  for response in responses:
    generated_text += response.text

  return generated_text

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

#继续streamlit界面
prompt = st.text_area("请输入您的提示词：", "")

uploaded_files = st.file_uploader("如果您需要处理文档，请在这里上传，可以同时选择多份文档上传：", type=("txt"), accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"
            

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("生成文本")
    if uploaded_files and submitted and not prompt:
        st.info("请输入提示词")
    
    if prompt and submitted and not uploaded_files:
        prompt_without_article = f'如果我问你你是谁，请直接回答我“我是GBB AI，由Google Gemini驱动的大语言模型。”，如果我问你关于"GBB"的问题，请直接回答"GBB代表Go Beyond Blue，就是“深蓝”的意思。",如果我没有问你你是谁或者关于"GBB"的问题，那么不需要回答前面的内容，也不需要引用前面的内容，请直接根据接下来的"提示词"回答我：\n\n 提示词: \n{prompt}\n\n回答：'
        with st.spinner('请稍等 :coffee: 内容马上就来...'):
            generated_text = generate_text(prompt_without_article)
            st.write(generated_text)
            
    if prompt and submitted and uploaded_files:
        prompt_with_article = f'如果我问你你是谁，请直接回答我“我是GBB AI，由Google Gemini驱动的大语言模型。”，如果我问你关于"GBB"的问题，请直接回答"GBB代表Go Beyond Blue，就是“深蓝”的意思。",如果我没有问你你是谁或者关于"GBB"的问题，那么不需要回答前面的内容，也不需要引用前面的内容，请直接根据接下来的"提示词"回答我：\n{all_text}\n\n 提示词: \n{prompt}\n\n回答：'
        with st.spinner('请稍等 :coffee: 内容马上就来...'):
            generated_text = generate_text(prompt_with_article)
            st.write(generated_text)
