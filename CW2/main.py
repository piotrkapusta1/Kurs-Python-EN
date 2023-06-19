import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Gruby")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras bibendum, dolor ut viverra facilisis, diam diam congue metus, in vestibulum magna urna vitae quam.
    In at consectetur mauris. In at metus vel velit dictum dignissim non vitae nisl. Duis eget lectus auctor, feugiat purus ac, feugiat elit. Nullam at sagittis mi, ut efficitur nulla.
    Maecenas volutpat commodo orci, vel tristique diam faucibus a. Donec est lectus, mollis et magna non, volutpat convallis libero. 
    """
    st.info(content)

st.write("""Below tou can find some of the apps I have built in Python.""")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
