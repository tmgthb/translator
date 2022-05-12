import openai
import os
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]
st.title('Traductor - español-finés')
prompt_text = st.text_input()
response = openai.Edit.create(engine="text-davinci-edit-001", input=prompt_text, instruction="Translate to Finnish", temperature=0.3, top_p=1)
st.text(response["choices"][0]["text"])
