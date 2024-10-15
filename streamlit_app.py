import streamlit as st
from openai import OpenAI
import os

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key


### Request the answer to the question "Damascus is a"
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": "Barcelona is a"}
  ],
  n=10,
  max_tokens=20
)

### Print all 10 completions:
for i in range(10):
  original_title = '<p style="font-family:Courier; color:Red; font-size: 20px;">'+response.choices[i].message.content+'</p>'
  st.markdown(original_title, unsafe_allow_html=True)
