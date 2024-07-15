import streamlit as st

title=st.text_input("문장'Hit the spot'을 해석하시오.(99)")
@st.experimental_dialog("정답 제출하기")
def vote(item):
    st.write(f"모든 문제를 푸셨습니까?")
    if st.button("제출하기"):
        st.session_state.vote = {"item": item}
        st.rerun()

if "vote" not in st.session_state:
    st.write("알파벳 'a'다음에 올 알파벳을 구하시오.(1)")
    if st.button("b"):
        vote("b")
    if st.button("c"):
        vote("c")
else:
    if "st.session_state.vote['item']" == 'b' :
        f"{st.session_state.vote['item']}"
        score = 1
    else :
        f"{st.session_state.vote['item']}"
        score = 0
    if title == "딱좋노" :
        "딱좋노"
        score = score + 99

    st.write(score)