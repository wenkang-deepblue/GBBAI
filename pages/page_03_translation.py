import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from auth import login, callback, logout

if "code" in st.query_params:
    callback()

if not login():
    st.stop()

with st.sidebar:
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">Welcome!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("log out"):
            logout()

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.42,0.30,0.28])
with cent_co:
    st.caption(":blue[_Enterprise-ready Translation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_4_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
# Define translation_option as a global variable
translation_option = None
    
# Continue streamlit sidebar interface
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
    temperature = st.slider("Adjust Model Temperature", min_value=0.0, max_value=2.0, value=1.0, help=(
        """
        Temperature is used for sampling during response generation, which occurs when applying topP and topK. Temperature controls the degree of randomness in token selection. For prompts that require less open-ended or creative responses, a lower temperature is good, while a higher temperature can lead to more diverse or creative results. A temperature of 0 means always selecting the highest probability token. In this case, the response for a given prompt is mostly deterministic, but there may still be some variation.
        
        If the model returns responses that are too generic, too short, or the model gives fallback responses, try increasing the temperature.
        """
    ))
    top_p = st.slider ("Adjust Model Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P changes how the model selects output tokens. Tokens are chosen from most likely to least likely (see top-K) until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have probabilities 0.3, 0.2, and 0.1 respectively, and the top-P value is 0.5, the model will select the next token from A or B using temperature and discard C as a candidate.

        Specifying a lower value will result in less random responses, while specifying a higher value will result in more random responses.
        """
    ))
    st.subheader('',divider='rainbow')
    translation_option = st.selectbox(
    "Please select the target language for translation:",
    ("German", "French", "Spanish", "Portuguese", "Italian", "Russian", "Arabic", "Chinese", "Japanese", "Korean", "English"),
    index=None,
    placeholder="Please select a language")
    st.page_link("homepage.py", label="Home", icon="🏠")
    st.page_link("pages/page_01_text_generation.py", label="Text Generation", icon="📖")
    st.page_link("pages/page_02_media_understanding.py", label="Media Understanding", icon="🎞️")
    st.page_link("pages/page_03_translation.py", label="Text Translation", icon="🇺🇳")
    st.page_link("pages/page_04_travel_advisor.py", label="Travel Advisor", icon="✈️")
    st.page_link("pages/page_05_rag_search.py", label="RAG Search", icon="🔍")
    st.page_link("pages/page_06_media_search.py", label="Media Search", icon="🎥")
    st.page_link("pages/page_07_image_generation.py", label="Image Generation", icon="🎨")
    st.page_link("pages/page_08_chatbot.py", label="Chatbot", icon="💬")
    st.page_link("pages/page_09_gaming_servicebot.py", label="Gaming Servicebot", icon="🤖")
    st.page_link("pages/page_10_ecommerce_servicebot.py", label="E-commerce Servicebot", icon="🤖")
    st.page_link("pages/page_11_claude_chatbot.py", label="Claude 3.5 Chatbot", icon="💬")
    st.page_link("pages/page_12_llama_chatbot.py", label="Llama 3.1 Chatbot", icon="💬")
    st.page_link("https://pantheon.corp.google.com/translation/hub", label="GCP Translation Hub", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/gallery", label="GCP Console - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/engines", label="GCP Console - App Builder", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.markdown(
        """
    ## About
    This is a generative AI platform powered by :blue[Google Cloud Vertex AI] and an enterprise-ready RAG search engine
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
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

    st.page_link("pages/terms_of_service.py", label="Terms of Service", icon="📄")
    st.page_link("pages/privacy_policy.py", label="Privacy Policy", icon="🔒")

# Define the function to generate text
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

# Define generation model parameters
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

# Continue streamlit interface
st.write("Please note: To help you distinguish the translation results, please choose either 'Upload Document' or 'Input Text'.")

uploaded_files = st.file_uploader("Please upload the documents you need to translate. You can select multiple documents to upload:", type=("txt"), accept_multiple_files=True)

prompt = st.text_area("Or input the text you need to translate:", "")

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"
            

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("Start Translation")
    if uploaded_files and prompt and translation_option and submitted:
        st.error("To help you distinguish the translation results, please choose either 'Upload Document' or 'Input Text'.")
        
    if uploaded_files and prompt and submitted:
        st.error("To help you distinguish the translation results, please choose either 'Upload Document' or 'Input Text'.")
        
    if uploaded_files and submitted and not prompt and not translation_option:
        st.error("👈 Please select the language you want to translate to.")
        
    if prompt and submitted and not uploaded_files and not translation_option:
        st.error("👈 Please select the language you want to translate to.")
    
    if prompt and translation_option and submitted and not uploaded_files:
        prompt_without_article = f"Please translate the following text into {translation_option}, and output the translation result directly\n\n Text to be translated: \n{prompt}\n\nAnswer:"
        with st.spinner('Please wait :coffee: Almost done...'):
            generated_text = generate_text(prompt_without_article)
            st.write(generated_text)
            
    if uploaded_files and translation_option and submitted and not prompt:
        prompt_with_article = f"Please translate the following text into {translation_option}, and output the translation result directly\n\n Text to be translated: \n{all_text}\n\nAnswer:"
        with st.spinner('Please wait :coffee: Almost done...'):
            generated_text = generate_text(prompt_with_article)
            st.write(generated_text)
