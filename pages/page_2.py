import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from google.cloud import storage
import os
import tempfile

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

model = GenerativeModel("gemini-1.5-flash-001")
# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.39,0.31,0.30])
with cent_co:
    st.title(":blue[GBB] :rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.3,0.6,0.1])
with cent_co:
    st.caption(":blue[_Enterprise Text Content Generation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_2.png')
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

    uploaded_file = st.file_uploader("Upload file to Google Cloud Storage", type=("mp4", "wmv", "jpg", "png"))
    
    file_type = None
    
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
   
    #define file uploading function
    def upload_to_gcs(uploaded_file, bucket_name, destination_blob_name, source_file_name):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_name = temp_file.name
        bucket_name = "lwk-rag-videos"
        source_file_name = uploaded_file.name
        destination_blob_name = uploaded_file.name
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        
        generation_match_precondition = 0
        
        blob.upload_from_filename(temp_file_name, if_generation_match=generation_match_precondition)               
            
        # delete temp file
        os.remove(temp_file_name)
    
        return f"gs://{bucket_name}/{destination_blob_name}"
          
    with st.form("mysidebarform"):
        left_co, cent_co,last_co = st.columns([0.32,0.38,0.3])
        with cent_co:
            submitted = st.form_submit_button("Upload")
        
        if submitted and not uploaded_file:
            st.markdown('<font size="2" color="#EA4335">Please choose your file firstly</font>', unsafe_allow_html=True)
        
        if submitted and uploaded_file:
            with st.spinner('Uploading, a moment please...'):
                gs_uri = upload_to_gcs(uploaded_file, "your-bucket-name", uploaded_file.name, uploaded_file.name)
                st.markdown('<font size="2" color="#1E8E3E">The file has been successfully uploaded to：</font>', unsafe_allow_html=True)
                st.code(gs_uri)
         
    st.page_link("https://pantheon.corp.google.com/storage/browser/lwk-rag-videos;tab=objects?forceOnBucketsSortingFiltering=true&e=13803378&hl=en&mods=dm_deploy_from_gcs&project=lwk-genai-test&prefix=&forceOnObjectsSortingFiltering=false", label="Google Cloud Storage Bucket", icon="🌎")
    st.subheader('',divider='rainbow')
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

#define video understanding function
def generate_video_text(prompt):
    video_responses = model.generate_content(
        [media, prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    generated_video_text = ""
    for response in video_responses:
        generated_video_text += response.text

    return generated_video_text

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
gcs_file = st.text_input("Please input your Google Cloud Storage uri", placeholder='gs://"bucket name"/"file name"')

media_mime_type = None

file_extension = None

# if no file uploaded, get file type according to GCS uri
if gcs_file:
    file_extension = gcs_file.split(".")[-1].lower()
    if file_extension == "mp4":
        media_mime_type = "video/mp4"
    elif file_extension == "jpg":
        media_mime_type = "image/jpeg"
    elif file_extension == "png":
        media_mime_type = "image/png"
    elif file_extension == "gif":
        media_mime_type = "video/wmv"

# if file uploaded, get file type according to file name
elif file_type:
    if file_type == "mp4":
        media_mime_type = "video/mp4"
    elif file_type == "jpg":
        media_mime_type = "image/jpeg"
    elif file_type == "png":
        media_mime_type = "image/png"
    elif file_type == "wmv":
        media_mime_type = "video/wmv"


media = Part.from_uri(
    mime_type=media_mime_type,
    uri=gcs_file
)

prompt = st.text_area("Please input your prompt：", "")

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
    with cent_co:
        submitted = st.form_submit_button("Generate Text Content")
    if gcs_file and submitted and not prompt:
        st.info("Please input prompt")
    
    if not gcs_file and prompt and submitted:
        with st.spinner('A second please :coffee: your content is upcoming...'):
            generated_text = generate_text(prompt)
            st.write(generated_text)
        
    if prompt and submitted and gcs_file:
        prompt_with_video = f"document content: \n{media}\n\n prompt: \n{prompt}\n\n answer："
        with st.spinner('A second please :coffee: your content is upcoming...'):
            generated_video_text_text = generate_video_text(prompt_with_video)
            
            if file_extension in ("jpg", "png"):
                # get bucket name and blob name from GCS uri
                bucket_name = gcs_file.split("/")[2]
                blob_name = "/".join(gcs_file.split("/")[3:])
            
                # get GCS client and bucket
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                
                # get blob object
                blob = bucket.blob(blob_name)
                
                # get https:// uri thru blob.public.url
                public_url = blob.public_url
            
                # display the image with public_url
                st.image(public_url, caption=blob_name)
            
            st.write(generated_video_text_text)
