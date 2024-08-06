import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from vertexai.preview.vision_models import ImageGenerationModel
import tempfile

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.39,0.32,0.29])
with cent_co:
    st.caption(":blue[_企业级图片生成平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_16_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GBB] :rainbow[AI]")
    number_of_images = st.slider("生成图片数量", min_value=1, max_value=4, value=4)
    aspect_ratio = st.selectbox(
    "请选择图片比例：",
    ("1:1", "9:16", "16:9", "3:4", "4:3"),
    index=None,
    placeholder="请选择宽高比")
    st.subheader('',divider='rainbow')
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
    st.page_link("https://translationhub.cloud.google.com/portal/cbec99246ab9ab5?projectId=210890376426", label="GCP翻译门户", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/create/text?project=lwk-genai-test", label="GCP控制台 - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/locations/global/engines/lwk-rag-search_1713579191717/preview/search?e=13803378&mods=dm_deploy_from_gcs&project=lwk-genai-test", label="GCP控制台 - RAG搜索", icon="🌎")
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
    
prompt = st.text_area("请输入您的提示词：", "")

generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

def generate_image(prompt):
    images = generation_model.generate_images(
        prompt=prompt,
        # Optional parameters
        number_of_images=number_of_images,
        language="auto",
        aspect_ratio=aspect_ratio,
        safety_filter_level="block_few",
        person_generation="allow_all",
    )
    output_files = []
    for i, image in enumerate(images):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            output_file = temp_file.name
            image.save(location=output_file, include_generation_parameters=False)
            output_files.append(output_file)
    return output_files
    
def display_images(image_files):
    """根据图片数量调整显示布局"""
    num_images = len(image_files)
    if num_images == 1:
        st.image(image_files[0])
    elif num_images == 2:
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_files[0])
        with col2:
            st.image(image_files[1])
    elif num_images == 3:
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_files[0])
        with col2:
            st.image(image_files[1])
        left_co, cent_co,last_co = st.columns([0.25,0.5,0.25])
        with cent_co:
            st.image(image_files[2])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_files[0])
            st.image(image_files[1])
        with col2:
            st.image(image_files[2])
            st.image(image_files[3])
    
with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("生成图片")
        
if prompt and submitted and not aspect_ratio:
    st.error("👈 请选择您的图片宽高比。")

if prompt and submitted and aspect_ratio:
    with st.spinner('请稍等 :coffee: 正在生成图片...'):
        output_files=generate_image(prompt)
        if output_files:
            display_images(output_files)
