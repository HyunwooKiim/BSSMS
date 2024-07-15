import streamlit as st

name=st.text_input("학번이름")
if st.button("입력"):
    st.write('당신의 학번이름은 ' + name + ' 입니다.')