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

legend_list={'Boston Celtics':{'Bill Russell','Larry Bird','Paul Pierce'},'Brooklyn Nets':{'Julius Erving','Jason Kidd','Derrick Coleman'},'New York Knicks':{'Walt Frazier','Patrick Ewing','Willis Reed'},
            'Philadelphia 76ers':{'Dikembe Mutombo','Allen Iverson','Wilt Chamberlain'},'Toronto Raptors':{'Kyle Lowry','Chris Bosh','Vince Carter'},'Chicago Bulls':{'Michael Jordan','Dennis Rodman','Scottie Pippen'},
            'Cleveland Cavaliers':{'LeBron James','Kevin Love','Kyrie Irving'},'Detroit Pistons':{'Isiah Thomas','Ben Wallace','Grant Hill'},'Indiana Pacers':{'Reggie Miller','Metta World Peace','Chuck Person'},
            'Milwaukee Bucks':{'Sidney Moncrief','Giannis Antetokounmpo','Glenn Robinson'},'Golden State Warriors':{'Tim Hardaway','Klay thompson','Stephen Curry'},'Los Angeles Clippers':{'Bob McAdoo','Blake Griffin','Chris Paul'},
            'Los Angeles Lakers':{'Magic Johnson',"Shaquille O'Neal",'Kobe Bryant'},'Phoenix Suns':{"Amar'e Stoudemire",'Steve Nash','Shawn Marion'},'Sacramento Kings':{'Chris Webber','Derek Harper','Rolando Blackman'},
            'Dallas Mavericks':{'Dirk Nowitzki','Derek Harper','Rolando Blackman'},'Houston Rockets':{'Hakeem Olajuwon','Moses Malone','Yao Ming'},'Memphis Grizzlies':{'Zach Randolph','Marc Gasol','Mike Miller'},
            'New Orleans Pelicans':{'Pete Maravich','Chris Paul','Anthony Davis'},'San Antonio Spurs':{'Tim Duncan','David Robinson','Manu Ginóbili'},'Atlanta Hawks':{'Bob Pettit','Dikembe Mutombo','Jamal Crawford'},
            'Charlotte Hornets':{'Kemba Walker','Dell Curry','Larry Johnson'},'Miami Heat':{'Alonzo Mourning','Dwyane Wade','LeBron James'},'Washington Wizards':{'Wes Unseld','Elvin Hayes','Earl Monroe'},
            'Denver Nuggets':{'Fat Lever','Dan Issel','David Thompson'},'Minnesota Timberwolves':{'Kevin Garnett','Sam Mitchell','Sam Cassell'},'Oklahoma City Thunder':{'Russell Westbrook','Gary Payton','Kevin Durant'},
            'Portland Trail Blazers':{'Bill Walton','Buck Williams','Clifford Robinson'},'Utah Jazz':{'Karl Malone','Darrell Griffith','John Stockton'},'Orlando Magic':{'Dwight Howard','Darrell Armstrong',"Shaquille O'Neal"}}











option = st.sidebar.selectbox('選擇球隊？',teams_list)

teams_information.teams_information(option)
teams_map.teams_map(option)



col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊戰績')
  teams_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=option)
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

st.markdown('### 傳奇球星成績')
col1,col2=st.columns(2)
with col1:
   option_legendplayer = st.selectbox('選擇球員？',legend_list[option])
   legendplayer_data = pd.read_excel("teams_legendplayerdata.xlsx",index_col='球員')      
   legendplayer_data=legendplayer_data.loc[option_legendplayer]
   legendplayer_data=legendplayer_data.reset_index(drop=False)
   st.dataframe(legendplayer_data.T)



