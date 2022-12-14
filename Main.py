import streamlit as st  
import xlrd 
import openpyxl
import pandas as pd
import plost
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
st.title('NBA資訊面板系統')
teams_list = {'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors','Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks',
              'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings','Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans',
              'San Antonio Spurs','Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards','Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 
              'Portland Trail Blazers','Utah Jazz'}
st.sidebar.header('請選擇球隊及想查看數據')
option = st.sidebar.selectbox('選擇球隊？',teams_list)
col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊戰績')
  df = pd.read_excel("nbateamsdata.xlsx",sheet_name=option)
  st.dataframe(df)
with col2: 
  dount_chart_df = pd.read_excel("teamsdata(dountchart).xlsx",sheet_name=option)
  st.markdown('### 2021-22年全年度戰績Donut chart')
  donut_theta = st.selectbox('Select data', ('14-15戰績', '15-16戰績'))
  plost.donut_chart(
              data=dount_chart_df ,
              theta='dount_theta',
              color='項目',
              legend='bottom',
              use_container_width=True)


