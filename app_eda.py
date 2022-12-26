import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_eda_app():

    leisure_data = pd.read_csv('leisure_data.csv')

    st.text(' ')
    st.text(' ')


    leisure_menu = ['연령대별 가구소득정도', '현재 여가활동 지출정도', '앞으로의 여가활동 지출정도 예상' ,'가장 활발한 여가활동']
    my_choice = st.sidebar.selectbox('여가활동 분석', leisure_menu)


    if my_choice == '연령대별 가구소득정도' :
        st.markdown('##### 온라인 소비자의 여가 문화 분석 데이터프레임')

        # 유저가 컬럼을 선택하면, 해당 컬럼을 화면에 보여주고,
        # 유저가 아무컬럼도 선택하지 않으면, 기본컬럼들만 보여준다.

        selected_list = st.multiselect('원하는 컬럼을 선택하세요', leisure_data.columns)
        
        if selected_list :
            st.dataframe(leisure_data[selected_list].head(5)) 

        else :
            st.dataframe(leisure_data[['age','gender','income_degree','now_leisure_spend','willingness_to_spending']].head(5))

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
    
        st.text(' ')
        st.text(' ')
        st.text(' ')


        df1= leisure_data.groupby(by='age')['income_degree'].mean().reset_index()
        df_sorted = df1.sort_values('age', ascending= False)
        fig7 = px.bar(df_sorted, x= 'age', y= 'income_degree', title='연령대별 가구소득정도')
        st.plotly_chart(fig7)
        


    # 현재 여가활동 지출정도 파이차트로 나타내기 - 남녀별 / 나이대별로
    #plotly pie차트
    elif my_choice == '현재 여가활동 지출정도' :
        st.subheader('소비자의 현재 여가활동 지출정도')
        st.text('')
        st.info('소비자의 연령대 또는 남녀별로 현재 여가활동 지출 정도를 나타내줍니다.')
        st.text(' ')

        age_choice= st.selectbox('연령대 선택',leisure_data['age'].unique())

        tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

        with tab1:

            data1= leisure_data[leisure_data['age'] == age_choice].sort_values('now_leisure_spend')
            fig2 = px.pie(data1, names='now_leisure_spend', title= age_choice +' 현재 여가활동 지출 정도')
            st.plotly_chart(fig2)
        
        
        with tab2 :
            st.text('')
            now_leisure_data = leisure_data[leisure_data['age']== age_choice]['now_leisure_spend'].value_counts().to_frame()
            st.dataframe(now_leisure_data)
            st.text(' ')
        
        st.text('')
        st.text('')

       
        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    
        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'

        tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

        with tab1:

            data2= leisure_data[leisure_data['gender'] == gender_choice2].sort_values('now_leisure_spend')
            fig3 = px.pie(data2, names='now_leisure_spend', title= gender_choice +' 현재 여가활동 지출 정도')
            st.plotly_chart(fig3)

        with tab2 :
            st.text('')
            now_leisure_data = leisure_data[leisure_data['gender']== gender_choice2]['now_leisure_spend'].value_counts().to_frame()
            st.dataframe(now_leisure_data)
            st.text(' ')
            


    elif my_choice == '앞으로의 여가활동 지출정도 예상':
        st.subheader('소비자의 앞으로의 여가활동 지출정도 예상')
        st.info('소비자의 연령대 또는 남녀별로 앞으로의 여가활동 지출정도 예상치를 나타내줍니다.')
        st.text(' ')

        age_choice= st.selectbox('연령대 선택',leisure_data['age'].unique())

        tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

        with tab1:
            data1= leisure_data[leisure_data['age'] == age_choice].sort_values('willingness_to_spending')
            fig4 = px.pie(data1, names='willingness_to_spending', title= age_choice +' 앞으로의 여가활동 지출정도')
            st.plotly_chart(fig4)
        

        with tab2 :
            st.text('')
            st.text('')
            st.text('')
            willingness_to_spending_data = leisure_data[leisure_data['age']== age_choice]['willingness_to_spending'].value_counts().to_frame()
            st.dataframe(willingness_to_spending_data)
            st.text(' ')
        

        st.text('')
        st.text('')


        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    

        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'

        tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

        with tab1:

            data2= leisure_data[leisure_data['gender'] == gender_choice2].sort_values('willingness_to_spending')
            fig5 = px.pie(data2, names='willingness_to_spending', title= gender_choice +'별 앞으로의 여가활동 지출정도')
            st.plotly_chart(fig5)

        with tab2:
            st.text('')
            willingness_to_spending_data2 = leisure_data[leisure_data['gender']== gender_choice2]['willingness_to_spending'].value_counts().to_frame()
            st.dataframe(willingness_to_spending_data2)



    elif my_choice == '가장 활발한 여가활동' :


        st.markdown('#### 온라인 소비자의 평균 여가 문화 시간 데이터를 보여줍니다.')
        status = st.radio('', ['남녀별 평균 여가문화 시간', '나이대별 평균 여가문화 시간'] )

        st.text('')
        # 소비자의 평균 여가문화시간 데이터프레임        
        if status == '남녀별 평균 여가문화 시간' :
            leisure_use = leisure_data.groupby('gender')[['workday_leisure_avg','weekend_leisure_avg','one_week_total_leisure']].mean()
            leisure_use = leisure_use.reset_index()
            leisure_use['gender'] = ['여성', '남성']
            leisure_use = leisure_use.set_index('gender')
            st.text('')
            st.write(leisure_use)

        elif status == '나이대별 평균 여가문화 시간':
            
            age_avg = leisure_data.groupby('age')[['workday_leisure_avg','weekend_leisure_avg','one_week_total_leisure']].mean()
            st.dataframe(age_avg)
        


        # 연령별 가장 활발한 여가활동을 히트맵으로 나타내기
        st.text(' ')
        st.text(' ')
        st.text(' ')
        st.markdown('#### 연령별 또는 남녀별 어떤 여가활동이 활발했는지 보여줍니다.')
        column_list = leisure_data[['rest_rcrt_rate','hobby_rate','self_impt_rate','human_relationship_rate','etc_rate']].columns
                
        data = leisure_data.groupby('age')[['rest_rcrt_rate','hobby_rate','self_impt_rate','human_relationship_rate','etc_rate']].mean().reset_index()
        data = data.set_index('age')


        fig6 = plt.figure()
        sb.heatmap(data, cmap='coolwarm', annot= True, fmt='.1f', linewidths= 0.7)
        plt.title('연령별 가장 활발한 여가활동')
        plt.xticks(rotation= 45)
        plt.yticks(rotation= 360)
        st.pyplot(fig6)


        # 성별로 활발한 여가종류 데이터 확인
        st.text('')
        st.markdown('#### 남녀별 주로 즐기는 여가 종류')
        st.text('아래 차트는 남녀별로 주로 즐기는 여가종류의 비율을 차트로 나타낸 것 입니다.')

        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    
        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'


        x = leisure_data[leisure_data['gender']==gender_choice2][['rest_rcrt_rate','hobby_rate','self_impt_rate','human_relationship_rate','etc_rate']].mean()
        st.text('')
        fig7 = plt.figure()
        plt.plot(x)
        plt.title('남녀별 주로 즐기는 여가 활동')
        plt.xticks(rotation= 45)
        plt.xlabel('type of leisure')
        plt.ylabel('average of numbers')
        st.pyplot(fig7)

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


