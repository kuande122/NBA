import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import teams_information
import teams_map


#-----Set up-----------------------------------------------------
st.set_page_config(page_title="NBA Dashboard",
                   page_icon='🏀',
                   layout="wide")
st.title('NBA資訊面板系統')


#-----Sidebar----------------------------------------------------
st.sidebar.title('請選擇區域及球隊')
area_list={'Atlantic':['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'],
           'Central':['Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks'],
           'Southeast':['Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'],
           'Northwest':['Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder','Portland Trail Blazers','Utah Jazz'],
           'Pacific':['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'],
           'Southwest':['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs']}
option_area = st.sidebar.selectbox('選擇區域？',area_list)
option_teams = st.sidebar.selectbox('選擇球隊？',area_list[option_area])


#-----teams_information&teams_map-----------------------------------------
teams_information.teams_information(option_teams)
teams_map.teams_map(option_teams)


#-----球隊戰績-------------------------------------------------------------
col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊戰績')
  teams_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name=option)
  st.dataframe(teams_data)
with col2: 
  dount_chart_df = pd.read_excel("data/nbateamsdata(dount_chart).xlsx",sheet_name=option)
  st.markdown('### 年度戰績Donut chart')
  donut_theta = st.selectbox('選擇年度', ('14-15年','15-16年','16-17年','17-18年','18-19年','19-20年','20-21年','21-22年'))
  plost.donut_chart(
              data=dount_chart_df ,
              theta=donut_theta,
              color='項目',
              legend='bottom',
              use_container_width=True)
  

#-----2021-22球員戰績---------------------------------------------------
st.markdown('### 2021-22球員戰績')
players_data=pd.read_excel("data/21-22playersdata.xlsx",sheet_name=option)
st.dataframe(players_data)

