import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import os

credentials_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

creds = service_account.Credentials.from_service_account_info(
    credentials_json,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# Streamlit UI
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.3,0.6,0.1])
with cent_co:
    st.caption(":blue[_Enterprise Text Content Generation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_1.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
#Continue streamlit sidebar UI
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
        st.title(":blue[GBB] :rainbow[AI]")
    temperature = st.slider("Adjust Temperature", min_value=0.0, max_value=2.0, value=1.0, help=(
        """
        Temperature controls the randomness in token selection \n

        -A lower temperature is good when you expect a true or correct response. A temperature of 0 means the highest probability token is always selected. \n
        -A higher temperature can lead to diverse or unexpected results. Some models have a higher temperature max to encourage more random responses. \n
        The selected model gemini-1.5-flash-001 has a temperature range of 0 - 2 and a default of 1.0
        """
    ))
    top_p = st.slider ("Adjust Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-p changes how the model selects tokens for output. Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value. For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).
        """
    ))
    st.subheader('',divider='rainbow')
    st.text("")
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

# define text generation function
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

#continue streamlit UI
prompt = st.text_area("Please input your prompt：", "")

uploaded_files = st.file_uploader("If you need to process documents, please upload here. Multiple documents acceptable：", type=("txt"), accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"
            

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
    with cent_co:
        submitted = st.form_submit_button("Generate Text Conntent")
    if uploaded_files and submitted and not prompt:
        st.info("Please input prompt")
    
    if prompt and submitted and not uploaded_files:
        prompt_without_article = f'prompt: \n{prompt}\n\n answer：'
        with st.spinner('A second please :coffee: you content is upcoming...'):
            generated_text = generate_text(prompt_without_article)
            st.write(generated_text)
            
    if prompt and submitted and uploaded_files:
        prompt_with_article = f'prompt: \n{prompt}\n\n answer：'
        with st.spinner('A second please :coffee: you content is upcoming...'):
            generated_text = generate_text(prompt_with_article)
            st.write(generated_text)
