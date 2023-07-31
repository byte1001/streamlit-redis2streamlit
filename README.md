# Streamlit Connections Hackathon - `Redis2Streamlit`
A simple Redis database connector for Streamlit.

Use this by importing `Redis2Streamlit` from `redis2streamlit`.
```python
from redis2streamlit import Redis2Streamlit
```

# Functions/Methods

`_connect(host, username, password, port)`  
Connect to a Redis DB. Requires Redis host URL and Database username + password. Port defaults to 6379.
  
    
`get(key, keytype, start, end)`  
Get data from the database. Requires `key` and `keytype`. `keytype` defaults to `string`.
The `start` and `end` arguments are used for keytype `list` and `sorted_set`.  

# Examples  
### `redis2streamlit.py` in the same directory
```python
from redis2streamlit import Redis2Streamlit
import streamlit as st

database_host = "mydatabase.cloud.redislabs.com"
database_username = "username"
database_password = "password"

database = st.experimental_connection(name="MyDatabase", type=Redis2Streamlit)
database._connect(host=database_host, username=database_username, password=database_password)
data = database.get("mykey", "string")
st.write(data)
```
