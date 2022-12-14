import streamlit as st  
import xlrd 
import openpyxl
import pandas as pd
st.set_page_config(layout="wide")
st.title('NBA資訊面板系統')
teams_list = {'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors','Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks',
              'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings','Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans',
              'San Antonio Spurs','Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards','Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 
              'Portland Trail Blazers','Utah Jazz'}
st.sidebar.header('請選擇球隊及想查看數據')
option = st.sidebar.selectbox('選擇球隊？',teams_list)

st.markdown('### 球隊戰績')
df = pd.read_excel("nbateamsdata.xlsx",sheet_name=option)
st.dataframe(df)
