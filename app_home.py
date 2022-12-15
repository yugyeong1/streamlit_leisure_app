import streamlit as st
from PIL import Image

def run_home_app() :    
    st.markdown('##### 온라인(PC/모바일) 소비자의 여가 문화를 분석하는 앱입니다.')
    st.text(' ')
    st.text(' ')

    st.text('온라인 소비자의 가구소득정도, 현재 여가활동에 얼만큼 쓰고있고, 앞으로 어느정도 쓸 예정인지')   
    st.text('어떤 여가활동이 가장 많았고, 평균 여가문화 시간 및 사용 비중에 대해서 분석한 앱입니다.')
    st.text(' ')
    st.text(' ')

    img = Image.open('여가생활.png')
    st.image(img)