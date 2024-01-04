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
この研究を行いたいと考えています。
より詳しい説明は下記のPDFファイルをご覧ください。印刷もできます。
[なお、同意説明文書はこちらをクリックしていただいても読むことができます。](https://drive.google.com/file/d/1uAbSyqgNZAFtbrSdAv415FP0wLeg1XrE/view?usp=sharing)
''')
    st.markdown(pdf_display, unsafe_allow_html=True)