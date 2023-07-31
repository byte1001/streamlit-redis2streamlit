# Streamlit Connections Hackathon - `Redis2Streamlit`
A simple Redis database connector for Streamlit.

Use this by importing `Redis2Streamlit` from `redis2streamlit`.
```python
from redis2streamlit import Redis2Streamlit
```

# Installation
`pip install git+https://github.com/byte1001/streamlit-redis2streamlit`

# Functions/Methods

`_connect(host, username, password, port)`  
Connect to a Redis DB. Requires Redis host URL and Database username + password. Port defaults to 6379.
  
    
`get(key, keytype, start, end)`  
Get data from the database. Requires `key` and `keytype`. `keytype` defaults to `string`.
The `start` and `end` arguments are used for keytype `list` and `sorted_set`.  

# Examples  
```python
from redis2streamlit import Redis2Streamlit
```
