import streamlit as st
from firebase_admin import auth
import smtplib
from email.message import EmailMessage


# Function to send verification email
def send_verification_email(email):
    try:
        link = auth.generate_email_verification_link(email)
        msg = EmailMessage()
        msg.set_content(f"このリンクをクリックすることでメンバー登録が完了します: {link}")
        msg['Subject'] = "PROSPERメンバー登録（Eメールアドレスの確認）"
        msg['From'] = "prosper-info@juntendo.ac.jp"
        msg['To'] = email

        # Use smtplib or another email library to send the email
        with smtplib.SMTP('smtp.example.com', 587) as s:
            s.starttls()
            s.login("your-email@example.com", "your-password")
            s.send_message(msg)

        return "Verification email sent."
    except Exception as e:
        return f"An error occurred: {e}"


# Function for the toggling behavior for the registration_button
def toggle_registration_button():
    if st.session_state.registration == True:
        st.session_state.registration = False
    else:
        st.session_state.registration = True
    

def app():
    st.title('PROPSERについて')
    st.markdown('''
この研究では、オンラインアンケート（症状調査）を行います。
ご同意いただいた方のみ、アンケートに回答していただく、
という方法で皆様の臨床症状や薬剤歴などのデータを収集して、
オンラインで臨床研究を実施します。
患者さんと医療者が双方向性に、誰もが自分の意志に基づいて研究に参加でき、
データの収集と利用をオンライン上でオープンに行うことで、
よりよい治療を発展させる研究を目指すコミュニティを構築することを目的に
この研究を行いたいと考えています。''')
    
    # insert a jpeg image (./data/prosper.jpg)
    st.image('./data/prosper.jpg', width=700)

    st.markdown('''
この研究に関するより詳しい説明は[こちらの説明文書をご覧ください。](https://drive.google.com/file/d/1uAbSyqgNZAFtbrSdAv415FP0wLeg1XrE/view?usp=sharing)
研究に賛同し、参加していただける方は下記ボタンよりメンバー登録にお進みください。                
''')

    
    
    # initialize session state
    if 'registration' not in st.session_state:
        st.session_state.registration = False

    st.button('メンバー登録', key='registration_step1', on_click=toggle_registration_button)


    if st.session_state.signout*st.session_state.signedout:
        st.warning('現在ログイン中です。メンバー登録は完了しております。')
        st.session_state.registration = False

    if st.session_state.registration == True:
        
        st.markdown("""
            ### [こちらをクリックして](https://drive.google.com/file/d/1uAbSyqgNZAFtbrSdAv415FP0wLeg1XrE/view?usp=sharing)、もういちど研究説明文書をよくお読みになったうえで、下記についてご確認ください。\n
            なお、リンク先の説明文書を印刷するには、右上のプリンターのアイコンを押して印刷してください。\n
            \n
            \n
            ===\n
        """)

        st.markdown("""
            順天堂大学医学部附属順天堂医院 脳神経内科 西川典子 殿\n
            \n
            研究課題名： **オープンサイエンスを目指した双方向性臨床研究を推進するためのパーキンソン病オンラインレジストリの構築**
            ：PROSPER (Parkinson's Registry and Open Science Platform for Empowering Research)\n
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
            """)
        # checkbox
        agreement=st.checkbox('上記項目について、説明文書を読んで理解しました。')

        
        # registration step2
        # input email and password
        if agreement:


            st.markdown('メンバー登録に使用するEメールと、ご希望のパスワードを入力してください。')
            email = st.text_input('Eメール')
            email2 = st.text_input('Eメールを確認のためもう一度入力してください')
            password = st.text_input('パスワード',type='password')
            password_2 = st.text_input("パスワードをもう一度いれてください",type='password')


            if email != email2:
                st.warning('Eメールが一致しません')
            elif password != password_2:
                st.warning('パスワードが一致しません')
            else:
                if st.button('メンバー登録', key='registration_step2'):
                    user = auth.create_user(email = email, password = password)
                    st.balloons()
                    st.success(f'{email}に確認メールを送信しました。メール内容にそって、メンバー登録を完了してください。')
                    elink=auth.generate_email_verification_link(email, action_code_settings=None, app=None)
                    st.text(elink)
                    # send_verification_email(email)
                    