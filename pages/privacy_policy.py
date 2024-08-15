import streamlit as st

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
            st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.36,0.32,0.32])
    with cent_co:
            st.title(":blue[GCP Gen]:rainbow[AI]")
    st.page_link("homepage.py", label="主页", icon="🏠")
    st.page_link("pages/page_1.py", label="文本生成", icon="📖")
    st.page_link("pages/page_2.py", label="视频理解", icon="🎞️")
    st.page_link("pages/page_3.py", label="文本翻译", icon="🇺🇳")
    st.page_link("pages/page_12.py", label="旅游顾问", icon="✈️")
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

    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="隐私政策", icon="🔒")

left_co, cent_co,last_co = st.columns([0.23,0.7,0.07])
with cent_co:
    st.title("GCP GenAI隐私政策")

left_co, cent_co,last_co = st.columns([0.36,0.5,0.14])
with cent_co:
    st.write("生效日期: 2024年8月1日")

st.text("")

st.markdown("""




本隐私政策描述了GCP GenAI应用（以下简称"本应用"）如何收集、使用和保护您的个人信息。我们重视您的隐私，并致力于保护您的个人数据。请仔细阅读本政策，了解我们的做法。

## 1. 信息收集

1.1 本应用不收集、存储或处理任何用户个人信息。

1.2 在使用本应用时，您需要使用Google账号登录。本应用仅验证您的邮件地址域名，以确认您是否有权限使用本应用，但不会记录或存储您的任何个人信息，包括但不限于姓名、邮件地址、电话号码等。

1.3 本应用没有任何形式的后端存储服务，包括但不限于数据库、磁盘以及对象存储服务，因此不会，也没有任何可能存储任何形式的个人信息或其他信息。

## 2. 信息使用

2.1 本应用仅将用户提供的数据(如提示词、图片、视频或文档)即时传递给Google Cloud Vertex AI的相关API，并将API返回的结果即时显示给用户。

2.2 由于本应用不会存储用户数据，因此不会，也没有能力将用户数据用于任何其他目的，更加不会与任何第三方共享用户数据。

## 3. 数据安全

3.1 由于本应用不存储任何用户数据，因此不存在数据泄露的风险。

3.2 所有数据传输都通过安全的HTTPS协议进行，以确保数据在传输过程中的安全性。

## 4. Cookie和跟踪技术

本应用不使用cookies或任何其他跟踪技术。每次登录都是一次全新的访问。

## 5. 第三方服务

本应用使用Google Cloud Vertex AI的API。根据Google Cloud的使用政策，Google Cloud有权拒绝响应违反其"负责任的AI"政策的请求。

## 6. 数据保留

6.1 本应用不保留任何用户数据。

6.2 当用户结束使用本应用(例如关闭浏览器或清空对话记录)后，所有在此过程中产生的数据和信息都将被即时清除。这是由本应用的代码机制和逻辑所决定的。

## 7. 用户权利

由于本应用不收集或存储任何个人数据，因此不涉及通常的数据主体权利，如访问权、更正权、删除权等。

## 8. 儿童隐私

本应用不面向18岁以下的个人提供服务，也不会故意收集18岁以下个人的任何信息。

## 9. 国际数据传输

本应用可能涉及将数据传输到美国或其他国家/地区的Google服务器。但请注意，这种传输是即时的，不涉及数据存储。

## 10. 隐私政策的变更

本应用可能会不时更新本隐私政策。任何重大变更都将在本页面上公布。我们建议您定期查看本政策以了解任何更新。

## 11. 联系我们

如果您对本隐私政策有任何疑问或担忧，请联系本应用的开发者：""" + f"{st.secrets['developer_email']}" + "。")
