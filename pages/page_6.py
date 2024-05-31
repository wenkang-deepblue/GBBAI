import streamlit as st
import base64
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

# Streamlit UI
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.33,0.38,0.29])
with cent_co:
    st.caption(":blue[_Enterprise Image Generation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_6.png')
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
    number_of_images = st.slider("Number of generated image", min_value=1, max_value=4, value=4)
    aspect_ratio = st.selectbox(
    "Please choose image aspect ratio：",
    ("1:1", "9:16", "16:9", "3:4", "4:3"),
    index=None,
    placeholder="Image aspect ratio")
    st.subheader('',divider='rainbow')
    
prompt = st.text_area("Please input your prompt：", "")
    
# Define project information
PROJECT_ID = "lwk-genai-test"
LOCATION = "us-central1"
output_files = None

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")

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
    """Adjust display layout according to image number"""
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
    left_co, cent_co,last_co = st.columns([0.38,0.33,0.29])
    with cent_co:
        submitted = st.form_submit_button("Generate Image")
        
if prompt and submitted and not aspect_ratio:
    st.error("👈 Please choose image aspect ratio")

if prompt and submitted and aspect_ratio:
    with st.spinner('A moment please :coffee: image upcoming...'):
        output_files=generate_image(prompt)
        if output_files:
            display_images(output_files)
                
with st.sidebar:
    st.page_link("homepage.py", label="Homepage", icon="🏠")
    st.page_link("pages/page_1.py", label="Article Generation", icon="📖")
    st.page_link("pages/page_2.py", label="Media Comprehension", icon="🎞️")
    st.page_link("pages/page_3.py", label="Text Translation", icon="🇺🇳")
    st.page_link("pages/page_4.py", label="Document Search", icon="🔍")
    st.page_link("pages/page_5.py", label="Media Search", icon="🎥")
    st.page_link("pages/page_6.py", label="Image Generation", icon="🎨")
    st.page_link("pages/page_7.py", label="Customer Service Chatbot", icon="🤖")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/create/text?project=lwk-genai-test", label="GCP Console - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/locations/global/engines/lwk-rag-search_1713579191717/preview/search?e=13803378&mods=dm_deploy_from_gcs&project=lwk-genai-test", label="GCP Console - Vertex AI Searh", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.markdown(
        """
    ## About
    This is an enterprise readiness GenAI platform powered by :blue[Google Cloud Vertex AI]
    - [:cloud: Google Cloud Vertex AI](https://cloud.google.com/vertex-ai?hl=en)

    """
    )
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    left_co, cent_co,last_co = st.columns([0.3,0.4,0.30])
    with cent_co:
        st.write('© [Wenkang Li](https://moma.corp.google.com/person/wenkangli?q=image%20generatioin%20streamlit)')
    left_co, cent_co,last_co = st.columns([0.2,0.79,0.1])
    with cent_co:
        st.write(
        '''
        :grey[Designed & Developed by]
        :blue[Wenkang Li & Gunther Hua]'''
         )
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')
