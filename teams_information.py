import streamlit as st  
from PIL import Image  
teams_list = {'Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors','Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks',
              'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings','Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans',
              'San Antonio Spurs','Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards','Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 
              'Portland Trail Blazers','Utah Jazz'}
option = st.sidebar.selectbox('選擇球隊？',teams_list)
def teams_information(option):
  if option=="Boston Celtics":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/BostonCeltics.png')
      st.image(image) 
    with col2:
       st.write("""# Boston Celtics""")   
       st.write("""##### 老闆:Wyc Grousbeck""")
       st.write("""##### GM:Juka Mcehaic""")
       st.write("""##### 總教練:Joe Mazzulla (臨時)""")
    st.write('波士頓塞爾提克(1946年-至今)') 
    st.write('波士頓塞爾蒂克隊的英文隊名為Boston Celtics，成立於1946年，目前所在地區是美國麻塞諸塞州波士頓市，主場為TD北岸花園球館，為美國職籃史上獲得總冠軍次數最多的球隊。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "17  次")
    col2.metric("分組冠軍🏆", "22  次")   
  if option=="Brooklyn Nets"
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/BrooklynNets.png')
      st.image(image) 
    with col2:
       st.write("""# Brooklyn Nets""")
       st.write("""##### 老闆:John Abbamondi""")
       st.write("""##### GM:Sean Marks""")
       st.write("""##### 總教練:Jacque Vaughn""")  
    st.write('紐澤西美洲人（ABA）(1967年-1968年)-紐約籃網（ABA）(1968年-1976年)-紐約籃網（NBA）(1976年-1977年)-紐澤西籃網(1977年-2012年)-布魯克林籃網(2012年-至今)') 
    st.write('布魯克林籃網隊的英文隊名為Brooklyn Nets，球隊成立於1967年，目前所在城市是美國紐約州布魯克林(Brooklyn, New York)，主場為大陸航空中心體育館(Prudential Center)。球隊原名紐澤西籃網隊（New Jersey Nets），2012年球隊遷至紐約布魯克林，4月底更名為「布魯克林籃網隊（Brooklyn Nets）。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "2  次")  
