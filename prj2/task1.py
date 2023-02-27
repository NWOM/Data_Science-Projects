import streamlit as st 
import requests
from PIL import Image
from pathlib import Path
from streamlit_lottie import st_lottie
cur_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic=cur_dir/ "assets" / "sagnik.jpg "

# Description
st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")
st.subheader("Hi,I am Sagnik Bhattacherjee :wave:")
st.title("Sophmore at Aliah University")
st.write("I am passionate about finding ways to use Python and JAVA")
st.write("[GitHub >](https://github.com/NWOM)")
st.write("[LinkedIn >](https://www.linkedin.com/in/sagnik-bhattacherjee-732b80227)")
def load_lottieurl(url):
	r=requests.get(url)
	if r.status_code !=200:
		return None 
	return r.json()	

#---LOAD ASSETS--
lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tno6cg2w.json")

#----WHAT I DO---
with st.container():
	st.write("---")
	left_column,right_column=st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##")
		st.write(
			"""
			I am a sophmore at Aliah University pursuing my B.TECH on Computer  Sciences 
			Currently acting as a Jr Data Science Intern At Innomatics Research Labs
			 -I harbour an avid interest in learning Machine Learning, NLP 
			 -I am also interested in exploring variety of algorithm and DSA learning enthusiasts
			 -I am currently learning about distributed Systems,cloud computing,coding and debugging such aplications
			 -Keen in finding ways and exploring JAVA and Python 
              """
			  )
		st.write("[LeetCode >](https://leetcode.com/sagnik5331/)")
		st.write("[KATTIS >](https://open.kattis.com/users/sagnik-bhattacherjee)")
	with right_column:
	 st_lottie(lottie_coding,height=400,key="coding")
#------PROJECTS----
with st.container():
	st.write("---")
	st.header("My Projects")
	
	st.subheader("client-server-messenger")
	st.write(
			"""

			A Basic Intro  to Socket Programming in JAVA .
			Simple Client-Server Communicator

			"""
			)
	st.write("[SERVER-CLIENT->](https://github.com/NWOM/client-server-messenger)")
	st.subheader("BOSTON-HOUSE-PRICE")
	st.write(
		"""
		A Supervised linear regression ML modelto predict the price of the house
		""")
	st.write("[BOSTON-HOUSE-PRICE->](https://github.com/NWOM/BOSTON-HOUSE-PRICE)")
	st.subheader("KEYLOGGER")
	st.write(
		"""
		Created a Keylogger for windows.Get user keypresses and store them in 
		a text file(pynput module should be installed)
        """
		   )
	st.write("[A-Keylogger->](https://github.com/NWOM/A-Keylogger)")
	st.subheader("TRAFFIC-SIMULATION")
	st.write("""
		     A simple traffic simulation is made using JAVA SWING and AWT
		     """
		     )
	st.write("[TRAFFIC-SIMULATION->](https://github.com/NWOM/TRAFFIC-SIMULATION)")
#----CONTACT----
with st.container():
	st.write("---")
	st.header("Get In Touch With Me!")
	st.write("##")

	contact_form="""
	     <form action="https://formsubmit.co/sagnikb5223@gmail.com" method="POST">
	     <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Yours Name" required>
         <input type="email" name="email" placeholder="Yourd email" required>
         <textarea name="message" placeholder="leave your message here" required></textarea>
         <button type="submit">Send</button>
</form>
"""
left_column,right_column=st.columns(2)
with left_column:
	st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()	

	


        