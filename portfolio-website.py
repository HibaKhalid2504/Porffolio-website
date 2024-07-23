import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]


genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Hiba Khalid")

with col2:
    st.image("images/hiba.png")

st.title(" ")

persona = """
        You are Hiba AI bot. You help people answer questions about your self (i.e Hiba)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Hiba: 

        Hiba Khalid is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        She runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Hiba obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). She is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Hiba's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Hiba's Email: hibakhalid2504@gmail.com 
        Hiba's Facebook: https://www.facebook.com/murtazasworkshop
        Hiba's Instagram: https://www.instagram.com/murtazasworkshop/
        Hiba's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Hiba's Github :https://github.com/murtazahassan
        """

st.title("Murtaza's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")

with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.title(" ")

st.title("My Setup")
#st.image("images/hiba.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.title("|col1")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")

with col2:
    st.title("|col2")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")

with col3:
    st.title("|col3")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")
    # st.image("images/hiba.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("hibakhalid2504@gmail.com")