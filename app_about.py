import streamlit as st
import pandas as pd
import numpy as np



def run_about_app() :
    st.text('')
    st.markdown('##### 분석할 때 이용한 데이터프레임')
    st.text('')
    st.info('온라인(PC/모바일) 소비자의 여가관련 지출 동향 및 의향 데이터')
    sp_tre1 = pd.read_csv('data/spending_trends/sp_tre1.csv')
    st.dataframe(sp_tre1.head(3))
    st.text('')


    st.info('온라인(PC/모바일) 소비자의 여가관련 지출 동향 및 의향')
    avg_leisure2 = pd.read_csv('data/avg_leisure/avg_leisure2.csv')
    st.dataframe(avg_leisure2.head(3))

