import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import plost            #plost套件(甜甜圈圖)
from PIL import Image   #圖片套件
import matplotlib.pyplot as plt #matplotlib(資料繪圖)
import seaborn as sns
import teams_information
import teams_map
import analysis_chart

#-----Set up-----------------------------------------------------
st.set_page_config(page_title="NBA Dashboard",
                   page_icon='🏀',
                   layout="wide")
st.title('NBA資訊面板系統')


#-----Sidebar----------------------------------------------------
image=Image.open('NBA logo.png')
st.sidebar.image(image)
st.sidebar.title('請選擇區域及球隊')
area_list={'Atlantic':{'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'},
           'Central':{'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks'},
           'Southeast':{'Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'},
           'Northwest':{'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder','Portland Trail Blazers','Utah Jazz'},
           'Pacific':{'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'},
           'Southwest':{'Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'}}
option_area = st.sidebar.selectbox('選擇區域？',area_list)
option_teams = st.sidebar.selectbox('選擇球隊？',area_list[option_area])


#-----teams_information&teams_map-----------------------------------------
teams_information.teams_information(option_teams)
teams_map.teams_map(option_teams)


#-----statement_court------------------------------------------------------
st.markdown('### 主場地板視覺')
image = Image.open('statement_court'+'/'+option_teams+'.png')
st.image(image)  
  
  
#-----球隊戰績-------------------------------------------------------------
col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊年度戰績')
  teams_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name=option_teams,index_col='年度')
  st.dataframe(teams_data)
with col2: 
  dount_chart_df = pd.read_excel("data/nbateamsdata(dount_chart).xlsx",sheet_name=option_teams)
  st.markdown('### 年度戰績Donut chart')
  donut_theta = st.selectbox('選擇年度', ('14-15年','15-16年','16-17年','17-18年','18-19年','19-20年','20-21年','21-22年'))
  plost.donut_chart(data=dount_chart_df ,
                    theta=donut_theta,
                    color='項目',
                    legend='bottom',
                    use_container_width=True)
  
  
#-----analysis_chart---------------------------------------------------
st.markdown('### 球隊數據分析')
analysis_chart.analysis_chart(option_teams)


#-----2021-22球員戰績---------------------------------------------------
st.markdown('### 2021-22球員戰績')
players_data=pd.read_excel("data/21-22playersdata.xlsx",sheet_name=option_teams,index_col='Player')
st.dataframe(players_data)


#-----三大傳奇球星成績--------------------------------------------------
legend_list={'Boston Celtics':{'Bill Russell','Larry Bird','Paul Pierce'},'Brooklyn Nets':{'Julius Erving','Jason Kidd','Derrick Coleman'},'New York Knicks':{'Walt Frazier','Patrick Ewing','Willis Reed'},
            'Philadelphia 76ers':{'Charles Barkley','Allen Iverson','Wilt Chamberlain'},'Toronto Raptors':{'Kyle Lowry','Chris Bosh','Vince Carter'},'Chicago Bulls':{'Michael Jordan','Dennis Rodman','Scottie Pippen'},
            'Cleveland Cavaliers':{'LeBron James','Kevin Love','Kyrie Irving'},'Detroit Pistons':{'Isiah Thomas','Ben Wallace','Grant Hill'},'Indiana Pacers':{'Reggie Miller','Metta World Peace','Chuck Person'},
            'Milwaukee Bucks':{'Sidney Moncrief','Giannis Antetokounmpo','Glenn Robinson'},'Golden State Warriors':{'Tim Hardaway','Klay thompson','Stephen Curry'},'Los Angeles Clippers':{'Bob McAdoo','Blake Griffin','Elton Brand'},
            'Los Angeles Lakers':{'Magic Johnson',"Shaquille O'Neal",'Kobe Bryant'},'Phoenix Suns':{"Amar'e Stoudemire",'Steve Nash','Shawn Marion'},'Sacramento Kings':{'Chris Webber','Oscar Robertson','Doug Christie'},
            'Dallas Mavericks':{'Dirk Nowitzki','Derek Harper','Rolando Blackman'},'Houston Rockets':{'Hakeem Olajuwon','Moses Malone','Yao Ming'},'Memphis Grizzlies':{'Zach Randolph','Marc Gasol','Mike Miller'},
            'New Orleans Pelicans':{'Pete Maravich','Chris Paul','Anthony Davis'},'San Antonio Spurs':{'Tim Duncan','David Robinson','Manu Ginóbili'},'Atlanta Hawks':{'Bob Pettit','Dikembe Mutombo','Jamal Crawford'},
            'Charlotte Hornets':{'Kemba Walker','Dell Curry','Larry Johnson'},'Miami Heat':{'Alonzo Mourning','Dwyane Wade','Grant Long'},'Washington Wizards':{'Wes Unseld','Elvin Hayes','Earl Monroe'},
            'Denver Nuggets':{'Fat Lever','Dan Issel','David Thompson'},'Minnesota Timberwolves':{'Kevin Garnett','Sam Mitchell','Sam Cassell'},'Oklahoma City Thunder':{'Russell Westbrook','Gary Payton','Kevin Durant'},
            'Portland Trail Blazers':{'Bill Walton','Buck Williams','Clifford Robinson'},'Utah Jazz':{'Karl Malone','Darrell Griffith','John Stockton'},'Orlando Magic':{'Dwight Howard','Darrell Armstrong',"Nick Anderson"}}
st.markdown('### 三大傳奇球星成績')
col1,col2=st.columns(2)
with col1:
   option_legendplayer = st.selectbox('選擇球員？',legend_list[option_teams])
   legendplayer_data = pd.read_excel("data/teams_legendplayerdata.xlsx",index_col='球員')      
   legendplayer_data=legendplayer_data.loc[option_legendplayer]
   legendplayer_data=legendplayer_data.reset_index(drop=False)
   st.dataframe(legendplayer_data.T)
with col2:
   image = Image.open('legendplayer'+'/'+option_legendplayer+'.jpg')
   st.image(image)  


#-----TOP 10 RANK👑-------------------------------------------------------------
st.markdown('### TOP 10 RANK👑')
col1,col2=st.columns(3)
with col1:
  rank_data = pd.read_excel("data/Rank.xlsx",sheet_name=option_teams,usecols='B,C')
  rank_data = rank_data[0:10]
  rank_data.sort_values(by='Games',inplace=True,ascending=False)
  fig, ax = plt.subplots()
  ax = sns.barplot(x=rank_data.Games, y=rank_data.PLAYER)
  ax.set_title(option_teams+' TOP 10 Rank to Games')
  st.pyplot(fig)

with col2:
  rank_data = pd.read_excel("data/Rank.xlsx",sheet_name=option_teams,usecols='F,G')
  rank_data = rank_data[0:10]
  rank_data.sort_values(by='Minutes Played',inplace=True,ascending=False)
  fig, ax = plt.subplots()
  ax = sns.barplot(x=rank_data.Games, y=rank_data.Minutes+"Played")
  ax.set_title(option_teams+' TOP 10 Rank to Minutes Played')
  st.pyplot(fig)



