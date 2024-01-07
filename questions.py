import streamlit as st

def app():
        
    if st.session_state.username=='':
        st.title('アンケートリンク')
        st.text('アンケートに答えるにはログインをしてください。')
    elif not st.session_state.useremail_verified:
        st.title('アンケートリンク')
        st.markdown('アンケートに答えるには「ログイン」ページから確認メールを送信して、メールアドレスの確認を行ってください')
    else:
        st.markdown(f'[基本情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSfYzTLLeenQccEtp9ZyyOiznLkLwK1PpF-hdmQ4cLg9RwHt7A/viewform?usp=pp_url&entry.2056512396={st.session_state.username})')