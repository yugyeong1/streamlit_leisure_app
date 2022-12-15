
import streamlit as st
from PIL import Image
from app_eda import run_eda_app
from app_home import run_home_app
from app_about import run_about_app
 
def main() :
    st.title('온라인 소비자의 여가 문화 분석')
    menu = ['Home', 'EDA', 'About']
 
    choice = st.sidebar.selectbox('메뉴', menu)
    img = st.sidebar.image('https://t1.daumcdn.net/cfile/tistory/252A0E475462E85A24')
 
    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'About' :
        run_about_app()


if __name__ == '__main__' :
    main()