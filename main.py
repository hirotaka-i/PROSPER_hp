import streamlit as st

from streamlit_option_menu import option_menu


import home, questions, login, dataviz, about
st.set_page_config(
        page_title="PROSPER",
)

button_css = f"""
<style>
  div.stButton > button:first-child  {{
    font-weight  : bold                ;/* 文字：太字                   */
    border       :  5px solid #f36     ;/* 枠線：ピンク色で5ピクセルの実線 */
    border-radius: 10px 10px 10px 10px ;/* 枠線：半径10ピクセルの角丸     */
    background   : #ddd                ;/* 背景色：薄いグレー            */
  }}
</style>
"""


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='PROSPER ',
                options=['ホーム','ログイン','アンケート','データ','お問い合わせ'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='none',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "ホーム":
            home.app()
            
        else:

            # initialize for home.py for registration status
            st.session_state.registration = False
            
            if app == "ログイン":
                login.app()    
            if app == "アンケート":
                questions.app()        
            if app == 'データ':
                dataviz.app()
            if app == 'お問い合わせ':
                about.app()    
             
          
             
    run()            
         
