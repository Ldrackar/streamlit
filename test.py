import time
import streamlit as st

with st.spinner('Waiting .. '):
    time.sleep(3)
st.write("Time out")
