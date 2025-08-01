import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English"])

if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown('AI Interviewer - V0.1.2')
        st.markdown(""" 
        #### Powered by
        [OpenAI](https://openai.com/)
        [FAISS](https://github.com/facebookresearch/faiss)
        [Langchain](https://github.com/hwchase17/langchain)
        """)

    st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    
    selected = option_menu(
        menu_title= None,
        # Reordered options: Resume, Professional, Behavioral
        options=["Resume", "Professional", "Behavioral", "Customize!"],
        icons = ["cloud-upload", "cast", "cast"],
        default_index=0,
        orientation="horizontal",
    )
    
    # The if conditions must match the new order of the options
    if selected == 'Resume':
        st.info("""
            📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            # Use the corrected filename with underscore
            st.switch_page("pages/Resume Screen.py")
            
    if selected == 'Professional':
        st.info("""
            📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            # Use the corrected filename with underscore
            st.switch_page("pages/Professional Screen.py")
            
    if selected == 'Behavioral':
        st.info("""
            📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ 
            """)
        if st.button("Start Interview!"):
            # Use the corrected filename with underscore
            st.switch_page("pages/Behavioral Screen.py")
            
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own AI Interviewer and practice with it!
            - Configure AI Interviewer in different specialties.
            - Configure AI Interviewer in different personalities.
            - Different tones of voice.
            
            Coming at the end of July""")
            
    st.markdown("""\n""")
