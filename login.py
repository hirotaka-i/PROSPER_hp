import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import smtplib
from email.message import EmailMessage
import email_setting as gmail

# Function to ensure Firebase is initialized only once
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("prosper1-firebase-adminsdk-w1jxl-33a055c618.json")
        firebase_admin.initialize_app(cred)

# Call the initialization function
initialize_firebase()

# Function to send verification email if not verified yet
def send_verification_email(email):
    try:
        elink = auth.generate_email_verification_link(email)
        # make the message in japanese by replacing trailing =en to =jp of the link
        elink = elink.replace('=en', '=jp')
        msg = EmailMessage()
        msg.set_content(f"このリンクをクリックすることでメンバー登録が完了し、アンケートに答えられます: {elink}")
        msg['Subject'] = "PROSPERメンバー登録（Eメールアドレスの確認）"
        # msg['From'] = "prosper-info@juntendo.ac.jp"
        msg['To'] = email

        # Use smtplib or another email library to send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(gmail.account, gmail.password)
            s.send_message(msg)

        return st.success("確認メールを送信しました。メールボックスをご確認ください")
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
    
    def f(): 
        try:
            user = auth.get_user_by_email(email=email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.useremail_verified = user.email_verified
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.error('ログインに失敗しました。メールアドレスとパスワードをご確認ください。問題が続く場合は事務局にお問い合わせください')
            st.warning('まだメンバーでない方は、左のメニューの「ホーム」からメンバー登録をお願いします。')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''       
        st.session_state.useremail_verified = False
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    

    

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        # choice = st.selectbox('ログイン/メンバー登録',['ログイン','メンバー登録'])
        email = st.text_input('Eメール')
        password = st.text_input('パスワード',type='password')       
        st.button('ログイン', on_click=f)
        
            
    if st.session_state.signout:
                st.text('User ID: '+st.session_state.username)
                st.text('Eメール: '+st.session_state.useremail)
                if st.session_state.useremail_verified:
                    st.success('アンケートにお進みください。')
                    st.button('ログアウト', on_click=t) 
                else:
                    st.warning('アンケートに答えるにはEメールアドレスの確認が必要です。')
                    st.markdown('下記のボタンを押すと登録されたEメールアドレスに確認メールを送信します。メールボックスをご確認ください。')
                    if st.button('確認メールを送信'):
                        send_verification_email(st.session_state.useremail)
                        st.markdown('メールアドレス確認がすみましたら、いったんログアウト後に再度ログインしてください。')
                        st.button('ログアウト', on_click=t)
                
                
                            
    def ap():
        st.write('Posts')