import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import webbrowser
from datetime import datetime
    
# def reset_custom_claims(uid):
#     # Reset the custom claims to an empty dictionary
#     auth.set_custom_user_claims(uid, {})
#     print(f"Custom claims reset for user: {uid}")

def record_button_click(uid, form_name):
    # Update custom claims with the current time
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Get current claims
    user = auth.get_user(uid)
    current_claims = user.custom_claims if user.custom_claims else {}

    # Add or update the claim for the specific form
    current_claims[form_name] = current_date
    auth.set_custom_user_claims(uid, current_claims)


def app():
        
    if st.session_state.username=='':
        st.title('アンケートリンク')
        st.text('アンケートに答えるにはログインをしてください。')
    elif not st.session_state.useremail_verified:
        st.title('アンケートリンク')
        st.markdown('アンケートに答えるには「ログイン」ページから確認メールを送信して、メールアドレスの確認を行ってください')
        
    else:
        user = auth.get_user(st.session_state.username)
        st.session_state.custom_claims = user.custom_claims if user.custom_claims else {}
        
        
        # Check command (comment out for production)
        # st.markdown(st.session_state.custom_claims)
        # if st.button("Reset Custom Claims"):
        #     reset_custom_claims(st.session_state.username)
        #     st.success("Custom claims reset!")
        
        st.warning('アンケートには予めメンバーIDが入力されています。こちらは変更せずに次に進んでください\n')
        
        test_one='このアンケートは最初に一度だけご回答頂いたので結構です。何度もご回答いただく必要はありません。'
        test_rep='このアンケートは何度回答していただいても構いません。現在の状況を教えてください。'

        ###
        st.markdown('#### 基本情報アンケート')
        form01='Basic'
        link01=f'https://docs.google.com/forms/d/e/1FAIpQLSeczVrafMvPsGrsqQsNY8U8jBH5U2JUcB5Uf_Y2hlPe2MmZeg/viewform?usp=pp_url&entry.1850808469={st.session_state.username}'
        if form01 in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日時] {st.session_state.custom_claims[form01]}')
            st.markdown(test_one)
        else:
            st.markdown(f'[最後に回答した日時] まだ回答していません')
        if st.button('基本情報アンケートをはじめる'):
            record_button_click(st.session_state.username, form01)
            st.link_button('アンケートを開く', link01)


        ###
        st.markdown('#### 経過情報アンケート')
        form_keika='keika'
        link_keika=f'https://docs.google.com/forms/d/e/1FAIpQLSdAG4PcOxFNITy4PbimVyg9Z0SjYqhqssQop0FvzHVJBOev_g/viewform?usp=pp_url&entry.2128319109={st.session_state.username}'
        if form_keika in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日時] {st.session_state.custom_claims[form_keika]}')
            st.markdown(test_rep)
        else:
            st.markdown(f'[最後に回答した日時] まだ回答していません')
        if st.button('経過情報アンケートをはじめる'):
            record_button_click(st.session_state.username, form_keika)
            st.link_button('アンケートを開く', link_keika)


        ###
        st.markdown('#### 生活アンケート１')
        form_life1='mds_updrs1'
        link_life1=f'https://docs.google.com/forms/d/e/1FAIpQLScue4b3DzDJ--YDEPXY_z7mK4oojFyBy1LgbwLStrDMz6sDfA/viewform?usp=pp_url&entry.1185128633={st.session_state.username}'
        if form_life1 in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日時] {st.session_state.custom_claims[form_life1]}')
            st.markdown(test_rep)
        else:
            st.markdown(f'[最後に回答した日時] まだ回答していません')
        if st.button('生活アンケート１をはじめる'):
            record_button_click(st.session_state.username, form_life1)
            st.link_button('アンケートを開く', link_life1)

        ###
        st.markdown('#### 生活アンケート２')
        form_life2='mds_updrs2'
        link_life2=f'https://docs.google.com/forms/d/e/1FAIpQLSc0nmQY5ruw7FKNKcrNOWPff4LniJrz2tCm-gduVi9Bj2PToA/viewform?usp=pp_url&entry.692875108={st.session_state.username}'
        if form_life2 in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日時] {st.session_state.custom_claims[form_life2]}')
            st.markdown(test_rep)
        else:
            st.markdown(f'[最後に回答した日時] まだ回答していません')
        if st.button('生活アンケート２をはじめる'):
            record_button_click(st.session_state.username, form_life2)
            st.link_button('アンケートを開く', link_life2)