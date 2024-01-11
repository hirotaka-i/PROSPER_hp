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

# Function to update Firebase custom claims and open the Google Form
def handle_form_button_click(uid, form_name, link):
    # Update custom claims with the current time
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Get current claims
    user = auth.get_user(uid)
    current_claims = user.custom_claims if user.custom_claims else {}

    # Add or update the claim for the specific form
    current_claims[form_name] = current_date
    auth.set_custom_user_claims(uid, current_claims)

    # Open the Google Form
    webbrowser.open_new_tab(link)


def app():
        
    if st.session_state.username=='':
        st.title('アンケートリンク')
        st.text('アンケートに答えるにはログインをしてください。')
    elif not st.session_state.useremail_verified:
        st.title('アンケートリンク')
        st.markdown('アンケートに答えるには「ログイン」ページから確認メールを送信して、メールアドレスの確認を行ってください')
        
    else:
        user = auth.get_user(st.session_state.username)
        st.session_state.custom_claims=user.custom_claims
        st.markdown(st.session_state.custom_claims)
        

        if st.button("Reset Custom Claims"):
            reset_custom_claims(st.session_state.username)
            st.success("Custom claims reset!")
        
        st.warning('アンケートには予めメンバーIDが入力されています。こちらは変更せずに次に進んでください\n')
        
        st.markdown('\n')
        st.markdown(f'[基本情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSeczVrafMvPsGrsqQsNY8U8jBH5U2JUcB5Uf_Y2hlPe2MmZeg/viewform?usp=pp_url&entry.1850808469={st.session_state.username})')
        st.markdown('\n')
        st.markdown(f'[経過情報アンケート](https://docs.google.com/forms/d/e/1FAIpQLSdAG4PcOxFNITy4PbimVyg9Z0SjYqhqssQop0FvzHVJBOev_g/viewform?usp=pp_url&entry.2128319109={st.session_state.username})')
        st.markdown('\n')
        st.markdown(f'[生活アンケート１](https://docs.google.com/forms/d/e/1FAIpQLScue4b3DzDJ--YDEPXY_z7mK4oojFyBy1LgbwLStrDMz6sDfA/viewform?usp=pp_url&entry.1185128633={st.session_state.username})')
        st.markdown('\n')
        st.markdown(f'[生活アンケート２](https://docs.google.com/forms/d/e/1FAIpQLSc0nmQY5ruw7FKNKcrNOWPff4LniJrz2tCm-gduVi9Bj2PToA/viewform?usp=pp_url&entry.692875108={st.session_state.username})')
        st.markdown('\n')
        st.markdown(f'[test](https://docs.google.com/forms/d/e/1FAIpQLSf7ycjTwE2sbV-rXqCGoyfzQHMTf69ms8B7SEGGnV2jn_1cYA/viewform?usp=pp_url&entry.2056512396={st.session_state.username})')
        
        test_one='このアンケートは最初に一度だけご回答ください'
        test_rep='このアンケートは何度回答していただいても構いません。'
        
        ###
        st.markdown('#### テストアンケート')
        form00='Test'
        link=f'https://docs.google.com/forms/d/e/1FAIpQLSf7ycjTwE2sbV-rXqCGoyfzQHMTf69ms8B7SEGGnV2jn_1cYA/viewform?usp=pp_url&entry.2056512396={st.session_state.username}'
        if form00 in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日] {st.session_state.custom_claims[form00]}')
            st.markdown(test_rep)
        else:
            st.markdown(f'まだ回答していません')
        if st.button('テストをはじめる'):
            handle_form_button_click(st.session_state.username, form00, link)   

        ###
        st.markdown('#### 基本情報アンケート')
        form01='Basic'
        link=f'https://docs.google.com/forms/d/e/1FAIpQLSeczVrafMvPsGrsqQsNY8U8jBH5U2JUcB5Uf_Y2hlPe2MmZeg/viewform?usp=pp_url&entry.1850808469={st.session_state.username}'
        if form01 in st.session_state.custom_claims.keys():
            st.markdown(f'[最後に回答した日時] {st.session_state.custom_claims[form01]}')
            st.markdown(test_one)
        else:
            st.markdown(f'[最後に回答した日時] まだ回答していません')
            if st.button('基本情報アンケートをはじめる'):
                handle_form_button_click(st.session_state.username, form01, link)