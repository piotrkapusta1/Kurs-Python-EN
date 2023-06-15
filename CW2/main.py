import streamlit as st

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