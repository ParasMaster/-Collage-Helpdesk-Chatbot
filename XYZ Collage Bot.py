import streamlit as st
import google.generativeai as gi
am=open("instructions.txt","r")
tr=am.read()
am.close()
ap=open("api.txt","r")
api_text = ap.read()
ap.close()
st.set_page_config(page_title="XYZ College Help Desk", page_icon="🎓")
st.title("XYZ College Name")
st.write("How may I help you? Type 'exit' to quit.")
gi.configure(api_key=api_text)
if "model"not in st.session_state:
    model = gi.GenerativeModel("gemini-1.5-flash")
if "chat" not in st.session_state:
    ins="You are a XYZ College bot . Only answer based on the following:\n\n"
    ins=ins+tr
    st.session_state.chat = model.start_chat(history=[{"role": "user", "parts": [ins]}])
user_input = st.text_input("Enter your query:")
if "exit" in user_input.lower() or "quit" in user_input.lower():
    st.markdown("Bye ,I shall Assist You Next Time")
    st.stop() 
elif user_input == "":
    pass
else:
    st.success(st.session_state.chat.send_message(user_input).text)



