import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.title("The Best Company")
content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras bibendum, dolor ut viverra facilisis, diam diam congue metus, in vestibulum magna urna vitae quam.
    In at consectetur mauris. In at metus vel velit dictum dignissim non vitae nisl. Duis eget lectus auctor, feugiat purus ac, feugiat elit. Nullam at sagittis mi, ut efficitur nulla.
    Maecenas volutpat commodo orci, vel tristique diam faucibus a. Donec est lectus, mollis et magna non, volutpat convallis libero. 
"""
st.write(content)
st.header("Our Team")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv", sep=",")

with col1:
     for index, row in df[:4].iterrows():
          st.header((row["first name"].capitalize() + " "
                      + row["last name"].capitalize()))
          st.write(row["role"])
          st.image("images/" + row["image"])
with col2:
     for index, row in df[4:8].iterrows():
          st.header((row["first name"].capitalize() + " "
                      + row["last name"].capitalize()))
          st.write(row["role"])
          st.image("images/" + row["image"])
with col3:
     for index, row in df[8:].iterrows():
          st.header((row["first name"].capitalize() + " "
                      + row["last name"].capitalize()))
          st.write(row["role"])
          st.image("images/" + row["image"])