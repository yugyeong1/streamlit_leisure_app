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

    with st.expander('columns 설명 : ') :
        st.text('id : 응답자ID')
        st.text('gender : 성별구분')
        st.text('age : 연령대구분')
        st.text('area : 답변자거주지역명')
        st.text('income_degree : 가구소득정도')
        st.text('inspection_day : 조사시작일자')
        st.text('workday_leisure_avg : 평일일평균레저시간값')
        st.text('weekend_leisure_avg : 주말일평균레저시간값')
        st.text('one_week_total_leisure : 1주총레저시간값')
        st.text('rest_rcrt_rate : 레저시간휴식오락사용비율')
        st.text('hobby_rate : 레저시간취미사용비율')
        st.text('self_impt_rate : 레저시간본인계발사용비율')
        st.text('human_relationship_rate : 레저시간대인관계교제사용비율')
        st.text('etc_rate : 레저시간기타사용비율')