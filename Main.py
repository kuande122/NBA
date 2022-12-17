import streamlit as st  
import xlrd 
import openpyxl
import pandas as pd
import plost
import matplotlib.pyplot as plt
import teams_information
import teams_map

st.set_page_config(layout="wide")
st.title('NBA資訊面板系統')

st.sidebar.header('請選擇區域及球隊')
area_list={'Atlantic','Central','Southeast','Northwest','Pacific','Southwest'}
option_area = st.sidebar.selectbox('選擇球隊？',area_list)

def area():
  if option_area=='Atlantic':
      teams_list = {'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'}
  if option_area=='Central':
      teams_list = {'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks'} 
  if option_area=='Southeast':   
      teams_list = {'Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'}
  if option_area=='Northwest':   
      teams_list = {'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder','Portland Trail Blazers','Utah Jazz'}
  if option_area=='Pacific':   
      teams_list = {'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'}    
  if option_area=='Southwest':   
      teams_list = {'Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'}
  return teams_list
teams_list=area()
option = st.sidebar.selectbox('選擇球隊？',teams_list)

teams_information.teams_information(option)
teams_map.teams_map(option)


team_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=option)
col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊戰績')
  st.dataframe(teams_data)
with col2: 
  dount_chart_df = pd.read_excel("nbateamsdata(dount_chart).xlsx",sheet_name=option)
  st.markdown('### 年度戰績Donut chart')
  donut_theta = st.selectbox('選擇年度', ('14-15年', '15-16年','16-17年','17-18年','18-19年','19-20年','20-21年','21-22年'))
  plost.donut_chart(
              data=dount_chart_df ,
              theta=donut_theta,
              color='項目',
              legend='bottom',
              use_container_width=True)
st.markdown('### 2021-22球員戰績')
players_data=pd.read_excel("21-22playersdata.xlsx",sheet_name=option)
st.dataframe(players_data)
col1,col2=st.columns((5,5))
with col2:
  #teamsPitching_Brothers=pd.read_excel("teamsPitching.xlsx",sheet_name=option) 
      plt.style.use("ggplot")
      plt.plot(teams_data.年度, teamsPitching_Brothers.防禦率,'.-' ,color='yellow') 
      plt.plot(teamsPitching_Unilions.年度, teamsPitching_Unilions.防禦率,'.-' ,color='darkorange')
      plt.plot(teamsPitching_Dragons.年度, teamsPitching_Dragons.防禦率, '.-',color='red')
      plt.plot(teamsPitching_Guardians.年度, teamsPitching_Guardians.防禦率,'.-', color='darkblue')
      plt.plot(teamsPitching_Rakuten.年度, teamsPitching_Rakuten.防禦率,'.-', color='maroon')
      plt.plot(teamsPitching_TSGHAWKS.年度, teamsPitching_TSGHAWKS.防禦率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.ylabel('ERA',fontsize="10")
      plt.title('ERA')
      plt.legend(labels=["Brothers Pitching", "Unilions Pitching","Dragons Pitching","Guardians Pitching","Rakuten Pitching","TSGHAWKS Pitching"], loc = 'best')
      st.pyplot(plt) 





