import streamlit as st
import base64

# Function to convert PDF file to base64
def get_pdf_file_as_base64(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        encoded_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
    return encoded_pdf

# Path to your PDF file
pdf_file_path = 'data/consent_doc.pdf'

# Convert your PDF to base64
pdf_base64 = get_pdf_file_as_base64(pdf_file_path)

# Embed the PDF in an iframe
pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf"></iframe>'



def app():
    st.title('PROPSERについて')
    st.markdown('''
この研究では、オンラインアンケート（症状調査）を行います。
ご同意いただいた方のみ、アンケートに回答していただく、
という方法で皆様の臨床症状や薬剤歴などのデータを収集して、
オンラインで臨床研究を実施します。
患者さんと医療者が双方向性に、誰もが自分の意志に基づいて研究に参加でき、
データの収集と利用をオンライン上でオープンに行うことで、
よりよい治療を発展させる研究を目指すコミュニティを構築することを目的に
この研究を行いたいと考えています。''')
    
    # insert a jpeg image (./data/prosper.jpg)
    st.image('./data/prosper.jpg', width=700)

    st.markdown('''
この研究に関するより詳しい説明は[こちらの説明文書をご覧ください。](https://drive.google.com/file/d/1uAbSyqgNZAFtbrSdAv415FP0wLeg1XrE/view?usp=sharing)
ご賛同していただける方は下記ボタンよりメンバー登録にお進みください。                
''')

    # a red bottun to go start registration
    if st.button('同意してメンバー登録'):
        st.session_state.signedout = True
        st.session_state.signout = True
        st.session_state.username = ''
        st.session_state.useremail = ''
        st.session_state.password = ''
        st.session_state.password_2 = ''
        st.session_state.choice = ''
        st.session_state.email = ''
        st.session_state.password = ''




    # st.markdown(pdf_display, unsafe_allow_html=True)