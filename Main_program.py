import streamlit as st  

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
