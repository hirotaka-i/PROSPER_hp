import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

import smtplib
from email.message import EmailMessage
import app_config as app_config
import json
import requests
import os

# Function to ensure Firebase is initialized only once
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("prosper1-firebase-adminsdk-w1jxl-33a055c618.json")
        firebase_admin.initialize_app(cred)

# Call the initialization function
initialize_firebase()

def sign_in_with_email_and_password(email, password, api_key):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# Function to send an email
def send_email(email, text_body):
    try:
        msg = EmailMessage()
        msg.set_content(text_body)
        msg['Subject'] = "PROSPER事務局からのお知らせ"
        msg['From'] = app_config.account
        msg['To'] = email

        # Use smtplib or another email library to send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(app_config.account, app_config.password)
            s.send_message(msg)

        return st.success("メールを送信しました。メールボックスをご確認ください")
    except Exception as e:
        return st.error(f"An error occurred: {e}")


def app():
# Usernm = []
    # main    
    st.title('アカウント　ログイン')
    st.markdown('まだメンバーでない方は、左のメニューの「**ホーム**」からメンバー登録をお願いします。')
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'login_error' not in st.session_state:
        st.session_state.login_error = False
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

        
    def f(): 
        try:
            # user = auth.get_user_by_email(email=email)
            USER = sign_in_with_email_and_password(email, password, app_config.firebase_web_api)
            # st.markdown(user)
            st.session_state.username = USER['localId']
            st.session_state.useremail = USER['email']
            
            # check if the email is verified
            user = auth.get_user_by_email(email=email)
            st.session_state.signedout = True
            st.session_state.signout = True
            st.session_state.useremail_verified = user.email_verified
            st.session_state.login_error = False
  
            
        # except:
        except Exception as e:
            # st.error(f"An error occurred: {e}") 
            st.error('ログインに失敗しました。メールアドレスとパスワードをご確認ください。問題が続く場合は事務局にお問い合わせください')
            st.warning('まだメンバーでない方は、左のメニューの「ホーム」からメンバー登録をお願いします。')
            st.session_state.login_error = True
            st.session_state.signedout = False
            st.session_state.signout = False

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        st.session_state.useremail_verified = False
        st.session_state.login_error = False

    # st.markdown(st.session_state)

    if st.session_state['login_error']:
        # st.text('2')
        email = st.text_input('Eメール')
        password = st.text_input('パスワード',type='password')    
        st.button('ログイン', on_click=f)  
        if len(email)>3:
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('*パスワードを忘れた方は下記のボタンを押して、パスワード再設定のリンクを送信してください。')
            if st.button('パスワード再設定のリンクを送信'):
                try:
                    elink=auth.generate_password_reset_link(email)
                    text_body=f"こちらのリンクからパスワードの再設定をお願いします。:{elink}"
                    send_email(email, text_body=text_body)
                    st.session_state.login_error = False
                except:
                    st.error('メールアドレスが登録されていません。メンバー登録をお願いします。')

    
    elif  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        # st.text('1')
        # choice = st.selectbox('ログイン/メンバー登録',['ログイン','メンバー登録'])
        email = st.text_input('Eメール')
        password = st.text_input('パスワード',type='password')       
        st.button('ログイン', on_click=f)
    
    

    # if st.session_state.signout:        
    else:
        # st.text('3')
        st.text('User ID: '+st.session_state.username)
        st.text('Eメール: '+st.session_state.useremail)
        if st.session_state.useremail_verified:
            # st.text('4')
            st.success('アンケートにお進みください。')
            st.button('ログアウト', on_click=t) 
        else:
            # st.text('5')
            st.warning('アンケートに答えるにはEメールアドレスの確認が必要です。')
            st.markdown('下記のボタンを押すと登録されたEメールアドレスに確認メールを送信します。メールボックスをご確認ください。')
            if st.button('確認メールを送信'):
                # st.text('6')
                elink = auth.generate_email_verification_link(st.session_state.useremail)
                # make the message in japanese by replacing trailing =en to =jp of the link
                elink = elink.replace('=en', '=jp')                
                text_body=f"このリンクをクリックすることでメンバー登録が完了し、アンケートに答えられます: {elink}"
                send_email(st.session_state.useremail, text_body=text_body)
                st.markdown('メールアドレス確認がすみましたら、いったんログアウト後に再度ログインしてください。')
                # st.markdown(st.session_state)
                st.button('ログアウト', on_click=t)