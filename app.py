
import streamlit as st
from app_eda import run_eda_app
from app_home import run_home_app
 
def main() :
    st.title('온라인 소비자의 여가 문화 분석')
    menu = ['Home', 'EDA', 'About']
 
    choice = st.sidebar.selectbox('메뉴', menu)
 
    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'About' :
        pass


if __name__ == '__main__' :
    main()