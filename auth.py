import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os
import json

# 设置Google OAuth 2.0客户端ID和密钥
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
REDIRECT_URI = "https://gcp-genai-zh.streamlit.app"

# 允许访问的域名列表
ALLOWED_DOMAINS = ["google.com"]

flow = Flow.from_client_config(
    {
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    },
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
    redirect_uri=REDIRECT_URI,
)

def get_login_url():
    authorization_url, _ = flow.authorization_url(prompt="consent")
    return authorization_url

def login():
    if "credentials" not in st.session_state:
        background_image_url = "https://storage.googleapis.com/ghackathon/nebula_1_2.jpg"
        background_style = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap');
        .stApp {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: center center;
            background-attachment: fixed;
        }}
        .welcome-text {{
            font-family: 'Google Sans', sans-serif;
            font-weight: 500;
            color: white;
            font-size: 48px;
            text-align: center;
            margin-bottom: 30px;
        }}
        .english-version-link {{
            position: fixed;
            top: 80px;
            right: 10px;
            z-index: 1000;
        }}
        .english-version-link a {{
            font-family: 'Google Sans', sans-serif;
            color: white;
            text-decoration: none;
            font-size: 25px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px 20px;
            border-radius: 10px;
            text-decoration: underline;
            text-decoration-color: white;
        }}
        </style>
        """
        st.markdown(background_style, unsafe_allow_html=True)
        st.markdown("<h1 class='welcome-text'>欢迎访问GCP-GenAI项目</h1>", unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.text("")

        english_version_html = """
        <div class="english-version-link">
            <a href="https://gcp-genai-en.streamlit.app/" target="_blank">English Version</a>
        </div>
        """
        st.markdown(english_version_html, unsafe_allow_html=True)
        
        google_logo_url = "https://storage.googleapis.com/ghackathon/GoogleG_FullColor_40px.svg"
    
        button_html = f"""
<style>
    .google-login-button {{
        position: relative;
        transition: transform 0.3s ease;
        overflow: hidden;
    }}
    .google-login-button:hover {{
        transform: scale(1.05);
    }}
    .google-login-button::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url('https://storage.googleapis.com/ghackathon/blue-gold.gif');
        background-size: cover;
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: 1;
    }}
    .google-login-button:hover::before {{
        opacity: 1;
    }}
    .button-content {{
        position: relative;
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
</style>
<div style="display: flex; justify-content: center; width: 100%;">
    <a href="{ get_login_url() }" style="text-decoration: none; width: 50%;">
        <div class="google-login-button" style="
            display: flex;
            align-items: center;
            background-color: #FFFFFF;
            color: #3c4043;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            justify-content: center;
            border: 1px solid #dadce0;
            width: 100%;
        ">
            <div class="button-content">
                <img src="{google_logo_url}" style="
                    width: 18px;
                    height: 18px;
                    margin-right: 10px;
                ">
                请使用您的 Google 公司账号登录
            </div>
        </div>
    </a>
</div>
"""
        st.markdown(button_html, unsafe_allow_html=True)

        footer_html = """
        <style>
        .footer-links {
            position: fixed;
            left: 0;
            bottom: 10px;
            width: 100%;
            text-align: center;
        }
        .footer-links a {
            color: white;
            text-decoration: underline;
        }
        </style>
        <div class="footer-links">
            <a href="https://gcp-genai-zh.streamlit.app/terms_of_service" target="_blank">用户服务协议</a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://gcp-genai-zh.streamlit.app/privacy_policy" target="_blank">用户隐私政策</a>
        </div>
        """
        st.markdown(footer_html, unsafe_allow_html=True)
        
        return False

    try:
        credentials_dict = st.session_state.credentials
        if isinstance(credentials_dict, str):
            credentials_dict = json.loads(credentials_dict)
        
        credentials = Credentials(
            token=credentials_dict['token'],
            refresh_token=credentials_dict['refresh_token'],
            token_uri=credentials_dict['token_uri'],
            client_id=credentials_dict['client_id'],
            client_secret=credentials_dict['client_secret'],
            scopes=credentials_dict['scopes']
        )
        
        service = build("oauth2", "v2", credentials=credentials)
        user_info = service.userinfo().get().execute()
        email = user_info.get("email")
        domain = email.split("@")[-1]

        if domain not in ALLOWED_DOMAINS:
            error_html = """
            <style>
            .centered-error {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 1rem;
                background-color: #ffecec;
                color: #721c24;
                border: 1px solid #ffecec;
                border-radius: 0.25rem;
                margin: 1rem 0;
            }
            </style>
            <div class="centered-error">
                您的邮箱域名不在允许访问的列表中，请使用您的@google.com账号登录。
            </div>
            """
            st.markdown(error_html, unsafe_allow_html=True)
            del st.session_state.credentials
            return False

        st.session_state.user_email = email
        return True
    except Exception as e:
        st.error(f"验证过程中发生错误: {str(e)}")
        if "credentials" in st.session_state:
            del st.session_state.credentials
        return False

def callback():
    try:
        flow.fetch_token(code=st.query_params["code"])
        st.session_state.credentials = {
            'token': flow.credentials.token,
            'refresh_token': flow.credentials.refresh_token,
            'token_uri': flow.credentials.token_uri,
            'client_id': flow.credentials.client_id,
            'client_secret': flow.credentials.client_secret,
            'scopes': flow.credentials.scopes
        }
        st.experimental_rerun()
    except Exception as e:
        print(f"验证过程中发生错误: {str(e)}")

def logout():
    if "credentials" in st.session_state:
        del st.session_state.credentials
    if "user_email" in st.session_state:
        del st.session_state.user_email
    st.experimental_rerun()
