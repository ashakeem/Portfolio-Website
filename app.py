import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Ayomide's Portfolio", page_icon=":briefcase:", layout = "wide")

#functions
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("style/style.css")

#Assets

lottie_anim = load_lottie("https://lottie.host/389d64e9-b60e-4d28-9853-9fdea724fcc0/ogmxsE9Eyd.json")

img_ryan_gpt = Image.open("images/RyanGPT.png")
img_algo_vis = Image.open("images/AlgoVis.png")

link_html_1 = '''

<div class = 'l'>
<a  href='https://github.com/ashakeem/AlgoVis' style = 'color: white '>View Project</a>
</div>

'''
link_html_2 = '''
<div class = 'l'> 
<a  href='https://github.com/ashakeem/RyanGPT' style = 'color: white '>View Project</a>
</div>

'''

contact_html = '''


<a href='mailto:ayomidesuleimanh@gmail.com' style = 'color: white '>Contact Me</a>
<a href='https://www.linkedin.com/in/ayomidehakeem/' style = 'color: white'>LinkedIn</a>
<a  class = 'git' href='https://github.com/ashakeem/' style = 'color: white' >GitHub</a>


'''








# Header
with st.container():

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Hi!, I'm Ayomide.  :wave: ")
        st.title(
            "I'm a student at California State Polytechnic University Pomona."
            )
        st.write(
            "I am majoring in Computer Engineering with a primary focus is in Software Engineering."
            )
        
        st.markdown(contact_html,  unsafe_allow_html=True)

        
    with right_column:
        st_lottie(lottie_anim, height=300 , key="anim" )



#Body

st.write("---") 

st.markdown(
        "<h2 style='text-align: center; text-decoration: underline;'>Featured Projects</h2>", unsafe_allow_html=True
        )

st.write("##")


with st.container():
    image_column, text_column = st.columns(2)
    with image_column:
       
       st.image(img_ryan_gpt,)

    with text_column:

        st.image(img_algo_vis)
        
        
with st.container():

    image_column, text_column = st.columns(2)
    with image_column:
       
         st.markdown(
        "<h2 style='text-align: center;  '>RyanGPT</h2>", unsafe_allow_html=True
        )
         st.write(
            "Developed an interactive chatbot application by integrating the OpenAI GPT-3 language model API with a user interface in Python, Streamlit, HTML, CSS, and JavaScript to simulate conversations and monitor resource consumption using Langchain." 
                 )
         st.markdown(link_html_2, unsafe_allow_html=True)

    with text_column:
   
        st.markdown(
        "<h2 style='text-align: center;'>AlgoVis</h2>", unsafe_allow_html=True
        )
        st.write(

            " Developed an Algorithm Visualizer in Python using the Tkinter GUI, enabling random data generation for Merge Sort, Quick Sort, and Dijkstra's Algorithms, providing step-by-step execution, significantly improving algorithm comprehension."
            )
        

        st.markdown(link_html_1, unsafe_allow_html=True)


        
    
