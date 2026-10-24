import streamlit as st

tab1,tab2,tab3 = st.tabs(["tab 1","tab 2","tab 3"])

with tab1:
    st.header("content of tab 1")
    st.button("click")

with tab2:
    st.header("content of tab 2")
    st.button("Welcome")

with tab3:
    st.header("content of tab 3")
    st.button("Hello there")
