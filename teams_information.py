import streamlit as st  
from PIL import Image  
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
  if option=="Brooklyn Nets":
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
  if option=="New York Knicks":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/NewYorkKnicks.png')
      st.image(image) 
    with col2:
      st.write("""# New York Knicks""")
      st.write("""##### 老闆:Leon Rose""")
      st.write("""##### GM:Scott Perry""")
      st.write("""##### 總教練:Tom Thibodeau""")     
    st.write('紐約尼克(1946年-至今)') 
    st.write('紐約尼克隊的英文隊名為New York Knicks，成立於1946年，目前所在地區是美國紐約州紐約市，主場為麥迪遜花園廣場(Madison Square Garden)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "2  次")
    col2.metric("分組冠軍🏆", "8  次")   
 if option=="Philadelphia 76ers":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Philadelphia76ers.png')
      st.image(image) 
    with col2:
       st.write("""# Philadelphia 76ers""")
       st.write("""##### 老闆:Tad Brown""")
       st.write("""##### GM:Elton Brand""")
       st.write("""##### 總教練:Doc Rivers""")     
    st.write('雪城國民(1946年-1963年)-費城76人(1963年-至今)')
    st.write('費城76人隊的英文隊名為Philadelphia 76ers，成立於1939年，目前所在地區是美國賓夕法尼亞州費城(Philadelphia, Pennsylvania)，主場為富國中心球館(Wells Fargo Center)')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "3  次")
    col2.metric("分組冠軍🏆", "9  次")   
 if option=="TorontoRaptors":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/TorontoRaptors.png')
      st.image(image) 
    with col2:
       st.write("""# Toronto Raptors""")
       st.write("""##### 老闆:Masai Ujiri""")
       st.write("""##### GM:Bobby Webster""")
       st.write("""##### 總教練:Nick Nurse""")     
    st.write('多倫多暴龍(1995年-至今)')
    st.write('多倫多暴龍隊的英文隊名為Toronto Raptors，球隊成立於1994年，目前所在城市是加拿大安大略省多倫多(Toronto, Ontario, Canada)，主場為加拿大航空中心(Air Canada Centre)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "1  次")   
