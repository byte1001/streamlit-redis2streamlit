from streamlit.connections import ExperimentalBaseConnection
import streamlit as st
import redis as r

class Redis2Streamlit(ExperimentalBaseConnection):
  def _connect(self, **kwargs):

    self.host = kwargs.get("host", "No host provided.")
    self.port = kwargs.get("port", 6379)
    self.username = kwargs.get("username", "No username provided.")
    self.password = kwargs.get("password", "No password provided.")
    
    self.db = r.Redis(host=self.host, 
                      port=self.port, 
                      username=self.username, 
                      password=self.password)
    return self.db
  
  def get(self, key, keytype="string", start=0, end=-1,ttl=None):
    @st.cache_data(ttl=ttl)
    def _get():
      nonlocal keytype
      keytype = keytype.lower()
      if keytype == "string":
        return self.db.get(key).decode()
      elif keytype == "list":
        return self.db.lrange(key, start, end)
      elif keytype == "set":
        return self.db.smembers(key)
      elif keytype == "sorted_set":
        return self.db.zrange(key, start, end)
      elif keytype == "json":
        return self.db.json().get(key)
      elif keytype == "hash":
        return self.db.hgetall(key)
      else:
        return "Value type is incorrect."
    return _get()
