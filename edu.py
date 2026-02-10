# ---imports
import streamlit as st
from dotenv import load_dotenv
import study_temp.pdf_summary 
import study_temp.img_2_txt
import study_temp.chat_agent
import study_temp.flash_cards
import study_temp.video_tran
import study_temp.convo_summery
import study_temp.user_plan
import os


from langchain_openai import ChatOpenAI




load_dotenv()  # reads .env file



# ---user details 
user = st.sidebar.text_input("enter the your name:")




# ---slidebar (user information)
Sidebar = st.sidebar.write(f"wlelcome to the journey , {user}")
add = st.sidebar.button("add study material here")
if add :
    material = st.sidebar.text_input("material")


# ---make 2 column  
col1,col2 = st.columns(2)

# ---col1 select what to study (multi seslect) & day planner
with col1:
    Selection_box = st.selectbox("choose what to study today :" , ["maths","physic","english","chemistry","Biology","analog circuit","graphics","cad designing"])



# ---col1 available study templete 
#           0.study all
#           1.pdf summery
#           2.video summary
#           3.web scrapper 
#           4.flash cards 
#           5.simple search 
#           6.question bank 
#           7.more knowledge 
#           8.prarical/industrial use case 



# ---col2 output 
