# Probably the most inefficient way to convert ASCII to Binary


from redis2streamlit.redis2streamlit import Redis2Streamlit
import streamlit as st
import os

dbhost = os.environ['DBHOST']
dbusername = os.environ['DBUSERNAME']
dbpassword = os.environ['DBPASSWORD']

ascii2binary = st.experimental_connection(name="ASCII2Binary", type=Redis2Streamlit)
ascii2binary._connect(host=dbhost, username=dbusername, password=dbpassword, port=10875)
a2bDB = ascii2binary.get("a2b-string", "json")
a2bSymbol = ascii2binary.get("a2b-symbols", "json")
a2bDB.update(a2bSymbol)

def a2b(inp):
  res = ""
  for i in inp:
    res += a2bDB[i] + " "
  return res

st.title('Streamlit Connections Hackathon')
st.header('ASCII2Binary - Redis2Streamlit')
st.write('Probably the most inefficient way to make an ASCII to Binary Converter')
st.write('')
ascii = st.text_input('ASCII here')
st.write("Binary:")
binary = st.code(a2b(ascii))
