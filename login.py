import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import smtplib
from email.message import EmailMessage

# Function to ensure Firebase is initialized only once
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("prosper1-firebase-adminsdk-w1jxl-33a055c618.json")
        firebase_admin.initialize_app(cred)

# Call the initialization function
initialize_firebase()


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
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''        
    
        
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
                st.markdown('アンケートにお進みください')
                st.button('ログアウト', on_click=t) 
            
                
                            
    def ap():
        st.write('Posts')