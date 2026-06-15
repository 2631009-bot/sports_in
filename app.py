import streamlit as st

st.set_page_config(page_title="스포츠인(Sports_In)", page_icon="🏀")

st.title("🏀 Hidden Sports Places")
st.subheader("우리 동네 숨겨진 스포츠 시설 찾기")

sport = st.selectbox(
    "스포츠 종목 선택",
    ["농구", "배드민턴", "풋살"]
)

region = st.text_input("지역 검색")

date = st.date_input("대관 날짜 선택")

time = st.selectbox(
    "시간 선택",
    ["09:00~11:00", "13:00~15:00", "18:00~20:00"]
)

if st.button("시설 검색"):
    st.success("검색 완료!")

    st.image(
        "https://images.unsplash.com/photo-1546519638-68e109498ffc",
        width=400
    )

    st.write("### 부산 스포츠 센터")
    st.write(f"종목: {sport}")
    st.write("위치: 부산광역시")
    st.write("시설 상태 우수, 주차 가능")

    favorite = st.toggle("즐겨찾기")

    if favorite:
        st.info("즐겨찾기에 저장되었습니다.")

    if st.button("예약하기"):
        st.success("예약이 완료되었습니다!")
