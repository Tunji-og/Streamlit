import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title ="My Webpage", page_icon =":relieved:",layout = "wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- Assets ----
animation  = load_lottie("https://assets1.lottiefiles.com/packages/lf20_3rqwsqnj.json")

# ----- Header -----
with st.container():
    st.subheader("Hi, I am Tunji :wave:")
    st.title("I am a Nigerian Data Analyst")
    st.write("I am passionate about finding ways to use Data Analysis(Python) in businesses")
    st.write("[Learn More about me >](https://github.com/Tunji-og)")
    
    
# __ who am i __
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            I am Interested in:
            - Looking for ways to leverage the power of python in my daily activities
            - Learning more about Data Analysis and Data Science For impactful analyses
            - working with others to gain more knowledge and skillset
            - Finding a stable source of income using my knowledge of python
            - Machine Learning And AI
            """
        )
    with right_column:
            st_lottie(animation, height = 300, key ="coding")
with st.container():
    st.write("---")
    st.header("Get In Touch With Me ")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/adetunjiogunsusi@gmail.com " method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
