# Probably the most inefficient way to convert ASCII to Binary


from redis2streamlit.redis2streamlit import Redis2Streamlit
import streamlit as st
import os

dbhost = os.environ['DBHOST']
dbusername = os.environ['DBUSERNAME']
dbpassword = os.environ['DBPASSWORD']

dbconnection = st.experimental_connection(name="Text2Binary", type=Redis2Streamlit)
dbconnection._connect(host=dbhost, username=dbusername, password=dbpassword, port=10875)
a2b = dbconnection.get("a2b", "json")


def ascii2binary(inp):
  result = ""
  for i in inp:
    try:
        if i == " ": i = "space" # these 2 lines because my Redis DB wont allow spaces and double quotes
        if i == '"': i = "sq" # these 2 lines because my Redis DB wont allow spaces and double quotes
        result += a2b[str(i)] + " "
    except Exception as e:
        return f"Cannot process input; invalid character: {str(e)[1]}"
  return result


st.title('Streamlit Connections Hackathon')
st.header('Text2Binary - Redis2Streamlit')
st.write('Probably the most inefficient way to make a Text to Binary Converter')
st.write('')
text = st.text_input('Text here', placeholder="Enter text...")
st.write("Binary:")
binary = st.code(ascii2binary(text))
