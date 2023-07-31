from redis2streamlit import Redis2Streamlit
import streamlit as st
import os

dhost = "redis-10875.c309.us-east-2-1.ec2.cloud.redislabs.com"
dusername = "connections-hackathon"
dpassword = "Redis@Streamlit2023"

testdb = st.experimental_connection(name="Test", type=Redis2Streamlit)
testdb._connect(host=dhost, username=dusername, password=dpassword, port=10875)
y = testdb.get("test", "string")
st.write(y)
