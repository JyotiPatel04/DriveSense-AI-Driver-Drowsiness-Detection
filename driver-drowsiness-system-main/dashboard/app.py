import streamlit as st
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["driver_db"]
collection = db["drowsiness"]

st.title("Driver Drowsiness Dashboard")

data = list(collection.find())

if data:
    df = pd.DataFrame(data)
    st.line_chart(df["score"])
    st.write(df)
else:
    st.write("No data yet")