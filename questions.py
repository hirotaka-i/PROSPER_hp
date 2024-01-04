import streamlit as st

def app():
        
    if st.session_state.username=='':
        st.title('アンケートリンク')
        st.text('アンケートに答えるにはログインをしてください。')
    else:
        st.markdown(f'[基本情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSfYzTLLeenQccEtp9ZyyOiznLkLwK1PpF-hdmQ4cLg9RwHt7A/viewform?usp=pp_url&entry.2056512396={st.session_state.username})')