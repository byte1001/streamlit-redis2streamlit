# Probably the most inefficient way to convert ASCII to Binary


from redis2streamlit.redis2streamlit import Redis2Streamlit
import streamlit as st
import os

dhost = os.environ['DBHOST']
dusername = os.environ['DBUSERNAME']
dpassword = os.environ['DBPASSWORD']

testdb = st.experimental_connection(name="Test", type=Redis2Streamlit)
testdb._connect(host=dhost, username=dusername, password=dpassword, port=10875)
y = testdb.get("test", "string")
st.write(y)
