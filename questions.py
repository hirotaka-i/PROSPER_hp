import streamlit as st

def app():
        
    if st.session_state.username=='':
        st.title('アンケートリンク')
        st.text('アンケートに答えるにはログインをしてください。')
    elif not st.session_state.useremail_verified:
        st.title('アンケートリンク')
        st.markdown('アンケートに答えるには「ログイン」ページから確認メールを送信して、メールアドレスの確認を行ってください')
        
    else:
        st.warning('アンケートには予めメンバーIDが入力されています。こちらは変更せずに次に進んでください\n')
        st.markdown('\n')
        st.markdown(f'[基本情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSeczVrafMvPsGrsqQsNY8U8jBH5U2JUcB5Uf_Y2hlPe2MmZeg/viewform?usp=pp_url&entry.1850808469={st.session_state.username})')
        st.markdown('\n')
        st.markdown(f'[経過情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSdAG4PcOxFNITy4PbimVyg9Z0SjYqhqssQop0FvzHVJBOev_g/viewform?usp=pp_url&entry.2128319109={st.session_state.username})')