import streamlit as st
from firebase_admin import firestore
import pandas as pd

def app():
    st.title('パーキンソン病のデータ')
    st.markdown('ここではパーキンソン病のデータを見ることができます。')
    st.markdown('パーキンソン病難病指定者数')
    # read df
    df=pd.read_csv('data/PDN.csv')
    # display df
    st.dataframe(df)
    st.markdown('出典：衛生行政報告例 / 令和4年度衛生行政報告例 / 統計表 / 年度報')

    if st.session_state.username!='':        
        st.subheader('アンケート集計結果')
        st.markdown('現在集計中です。')


    if st.session_state.username=='':        
        st.text('ログインをしていただくと、アンケートの集計結果も見ることができます。')