import streamlit as st
if st.button("결과 확인하기기"):
    st.write(f"{st.session_state.name}님의 점수는{st.session_state.vote.score}입니다.")