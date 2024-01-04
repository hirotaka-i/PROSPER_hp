import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

# Function to ensure Firebase is initialized only once
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("prosper1-firebase-adminsdk-w1jxl-33a055c618.json")
        firebase_admin.initialize_app(cred)

# Call the initialization function
initialize_firebase()

def app():
# Usernm = []
    st.title('アカウント')
    st.markdown('研究に参加登録する場合は下のドロップダウンメニューから、ユーザー登録をお選びください。')
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
        choice = st.selectbox('ログイン/ユーザー登録',['ログイン','ユーザー登録'])
        email = st.text_input('Eメール')
        password = st.text_input('パスワード',type='password')
        

        
        if choice == 'ユーザー登録':
            password_2 = st.text_input("パスワードをもう一度いれてください",type='password')
            if password != password_2:
                st.warning('パスワードが一致しません')
            else:
                st.markdown('# ユーザー登録には同意が必要です')
                st.markdown('''
本研究に参加をご希望される方は、「ホーム」の部分にある研究の説明をしている文書（同意説明文書）を
よく読み、下記の項目についてご確認いただき、同意いただける場合のみ、
”同意してユーザー登録”のボタンを押してください。
[なお、同意説明文書はこちらをクリックしていただいても読むことができます。](https://drive.google.com/file/d/1uAbSyqgNZAFtbrSdAv415FP0wLeg1XrE/view?usp=sharing)
''')
                st.markdown('## 同意事項')
                st.markdown("""
順天堂大学医学部附属順天堂医院 脳神経内科 西川典子 殿\n
\n
研究課題名： **オープンサイエンスを目指した双方向性臨床研究を推進するためのパーキンソン病オンラインレジストリの構築**：PROSPER (Parkinson's Registry and Open Science Platform for Empowering Research)\n
\n
＜説明事項＞\n
1. はじめに
2. あなたの病気と治療法について
3. この研究の目的
4. この研究の方法
5. この研究の対象となる方について
6. この研究の予定参加期間
7. この研究の予定参加人数について
8. この研究への参加により予想される利益と起こるかもしれない不利益
9. この研究に参加しない場合の他の治療方法
10. この研究中に、あなたの健康に被害が生じた場合について
11. 研究への参加の任意性について
12. この研究に関する情報の提供について
13. 個人情報等の取扱いについて
14. 研究に参加した場合の第三者のデータ閲覧について
15. 研究に参加した場合の留意事項について
16. あなたの費用負担について
17. 利益相反について
18. 研究により得られた結果等の取扱いについて
19. データの二次利用について
20. この研究の実施体制について
21. いつでも相談窓口にご相談ください
\n

私は、上記について十分に説明いたしました。
""")

                if st.button('同意してユーザー登録'):
                    user = auth.create_user(email = email, password = password)
                    
                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button('ログイン', on_click=f)
            
            
    if st.session_state.signout:
                st.text('User ID: '+st.session_state.username)
                st.text('Eメール: '+st.session_state.useremail)
                st.markdown('アンケートにお進みください')
                st.button('ログアウト', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Posts')