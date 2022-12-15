import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
import altair as alt

# 한글 처리를 위한 코드
# %matplotlib inline
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')




def run_eda_app():
    # 여가관련 지출 동향 및 의향 데이터
    sp_tre1 = pd.read_csv('data/spending_trends/sp_tre1.csv')
    sp_tre2 = pd.read_csv('data/spending_trends/sp_tre2.csv')
    sp_tre3 = pd.read_csv('data/spending_trends/sp_tre3.csv')
    sp_tre4 = pd.read_csv('data/spending_trends/sp_tre4.csv')
    sp_tre5 = pd.read_csv('data/spending_trends/sp_tre5.csv')

    # 여가관련 지출 동향 및 의향 데이터 합치기
    spending_trend = pd.concat([sp_tre1, sp_tre2, sp_tre3, sp_tre4, sp_tre5])

    # 컬럼명 바꾸기
    spending_trend = spending_trend.rename( columns = {'RESPOND_ID':'id', 'EXAMIN_BEGIN_DE':'inspection_day' , 'SEXDSTN_FLAG_CD':'gender', 
                                    'AGRDE_FLAG_NM':'age', 'ANSWRR_OC_AREA_NM':'area', 'HSHLD_INCOME_DGREE_NM': 'income_degree', 
                                    'LSR_CT_EXPNDTR_TNDCY_VALUE':'now_leisure_spend','LSR_CT_EXPNDTR_INTEN_VALUE':'willingness_to_spending'})

    # 하루 평균 여가문화 시간 및 사용 비중 데이터
    avg_leisure1 = pd.read_csv('data/avg_leisure/avg_leisure1.csv')
    avg_leisure2 = pd.read_csv('data/avg_leisure/avg_leisure2.csv')
    avg_leisure3 = pd.read_csv('data/avg_leisure/avg_leisure3.csv')
    avg_leisure4 = pd.read_csv('data/avg_leisure/avg_leisure4.csv')
    avg_leisure5 = pd.read_csv('data/avg_leisure/avg_leisure5.csv')

    # 하루 평균 여가문화 시간 및 사용 비중 데이터 합치기
    avg_leisure = pd.concat([avg_leisure1, avg_leisure2, avg_leisure3, avg_leisure4, avg_leisure5])

    # 컬럼명 바꾸기
    avg_leisure = avg_leisure.rename( columns = {'RESPOND_ID':'id', 'EXAMIN_BEGIN_DE':'inspection_day' , 'SEXDSTN_FLAG_CD':'gender','AGRDE_FLAG_NM':'age',
                                'ANSWRR_OC_AREA_NM':'area', 'HSHLD_INCOME_DGREE_NM': 'income_degree', 'WORKDAY_DAY_AVRG_LSR_TIME_VALUE':'workday_leisure_avg', 'WKEND_DAY_AVRG_LSR_TIME_VALUE' : 'weekend_leisure_avg',
                                'ONE_WEEK_TOT_LSR_TIME_VALUE':'one_week_total_leisure', 'LSR_TIME_REST_RCRT_USE_RATE' : 'rest_rcrt_rate',
                                'LSR_TIME_HOBBY_USE_RATE': 'hobby_rate', 'LSR_TIME_SELF_IMPT_USE_RATE':'self_impt_rate',
                                'LSR_TIME_TWDPSN_RLTN_FLWSP_USE_RATE': 'human_relationship_rate', 'LSR_TIME_ETC_USE_RATE':'etc_rate'})


    # 데이터 가공

    # spendint_trend 데이터와 avg_leisure 데이터가 겹치는 컬럼을 avg_leisure 데이터프레임에서 제거
    avg_leisure = avg_leisure.drop(['inspection_day','gender','age','area','income_degree'], axis= 1)

    # 데이터프레임 두개를 merge
    leisure_data = pd.merge(spending_trend, avg_leisure, on = 'id', how= 'left')

    leisure_data.loc[leisure_data['income_degree'] == '300만원 미만','income_degree'] = 200
    leisure_data.loc[leisure_data['income_degree'] == '300이상500만원 미만','income_degree'] = 400
    leisure_data.loc[leisure_data['income_degree'] == '500이상700만원 미만','income_degree'] = 600
    leisure_data.loc[leisure_data['income_degree'] == '700만원 이상','income_degree'] = 700

    leisure_data = leisure_data[~leisure_data['income_degree'].isin(['무응답'])]
    leisure_data['income_degree'] = leisure_data['income_degree'].astype(float)

    st.text(' ')
    st.text(' ')
    st.markdown('##### 온라인 소비자의 여가 문화 분석 데이터프레임')

    # 유저가 컬럼을 선택하면, 해당 컬럼을 화면에 보여주고,
    # 유저가 아무컬럼도 선택하지 않으면, 데이터프레임 보여주지 않는다.

    selected_list = st.multiselect('원하는 컬럼을 선택하세요', leisure_data.columns)
    
    if selected_list :
        st.dataframe(leisure_data[selected_list].head(5)) 

    else :
        st.text('')
    


    leisure_menu = ['연령대별 가구소득정도', '현재 여가활동 지출정도', '앞으로의 여가활동 지출정도 예상' ,'가장 활발한 여가활동']
    my_choice = st.sidebar.selectbox('여가활동 분석', leisure_menu)


    if my_choice == '연령대별 가구소득정도' :
        st.text(' ')
        st.text(' ')
        st.text(' ')

       

        # 연령대별 가구소득 정보 차트  
        fig = plt.figure()
        leisure_data.groupby('age')['income_degree'].mean().sort_values().plot(kind= 'bar')
        plt.xticks(rotation= 45)
        plt.title('연령대별 가구소득정도')
        plt.ylabel('income')
        st.pyplot(fig)


    # 현재 여가활동 지출정도 파이차트로 나타내기 - 남녀별 / 나이대별로
    #plotly pie차트
    elif my_choice == '현재 여가활동 지출정도' :

        st.text(' ')
        st.text(' ')
        st.info('소비자의 연령대 또는 남녀별로 현재 여가활동 지출 정도를 나타내줍니다.')
        st.text(' ')

        age_choice= st.selectbox('연령대 선택',leisure_data['age'].unique())

        data1= leisure_data[leisure_data['age'] == age_choice].sort_values('now_leisure_spend')
        fig2 = px.pie(data1, names='now_leisure_spend', title= age_choice +' 현재 여가활동 지출 정도')
        st.plotly_chart(fig2)
        
        st.text(' ')
        st.text(' ')


       
        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    
        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'

        data2= leisure_data[leisure_data['gender'] == gender_choice2].sort_values('now_leisure_spend')
        fig3 = px.pie(data2, names='now_leisure_spend', title= gender_choice +' 현재 여가활동 지출 정도')
        st.plotly_chart(fig3)


    elif my_choice == '앞으로의 여가활동 지출정도 예상':

        st.text(' ')
        st.text(' ')
        st.info('소비자의 연령대 또는 남녀별로 앞으로의 여가활동 지출정도 예상치를 나타내줍니다.')
        st.text(' ')

        age_choice= st.selectbox('연령대 선택',leisure_data['age'].unique())

        data1= leisure_data[leisure_data['age'] == age_choice].sort_values('willingness_to_spending')
        fig4 = px.pie(data1, names='willingness_to_spending', title= age_choice +' 앞으로의 여가활동 지출정도')
        st.plotly_chart(fig4)
        
        st.text(' ')
        st.text(' ')


       
        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    
        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'

        data2= leisure_data[leisure_data['gender'] == gender_choice2].sort_values('willingness_to_spending')
        fig5 = px.pie(data2, names='willingness_to_spending', title= gender_choice +'별 앞으로의 여가활동 지출정도')
        st.plotly_chart(fig5)



    elif my_choice == '가장 활발한 여가활동' :
        # 연령별 가장 활발한 여가활동을 히트맵으로 나타내기
        st.text(' ')
        st.info('연령별 또는 남녀별 어떤 여가활동이 활발했는지 보여줍니다.')
        st.text(' ')
        st.text(' ')
        column_list = leisure_data[['rest_rcrt_rate','hobby_rate','self_impt_rate','human_relationship_rate','etc_rate']].columns
        selected_list = st.multiselect('원하는 컬럼을 선택하세요! 선택한 컬럼들로 히트맵을 그려집니다.', column_list)
        if selected_list :
            data = leisure_data.groupby('age')[selected_list].mean()
            fig6 = plt.figure()
            sb.heatmap(data, cmap='coolwarm', annot= True, fmt='.1f', linewidths= 0.7)
            plt.title('연령별 가장 활발한 여가활동')
            plt.xticks(rotation= 45)
            plt.yticks(rotation= 360)
            st.pyplot(fig6)

        else :
            st.text('')





        # 성별로 활발한 
        gender_choice= st.selectbox('성별 선택', ['여성','남성'])
    
        if gender_choice == '여성' :
            gender_choice2 = 'F'

        elif gender_choice == '남성' :
            gender_choice2 = 'M'


        x = leisure_data[leisure_data['gender']==gender_choice2][['rest_rcrt_rate','hobby_rate','self_impt_rate','human_relationship_rate','etc_rate']].mean()
        fig7 = plt.figure()
        plt.plot(x)
        plt.xticks(rotation= 45)
        plt.title( gender_choice +'이 주로 즐기는 여가 종류')
        plt.xlabel('type of leisure')
        plt.ylabel('average of numbers')
        st.pyplot(fig7)


