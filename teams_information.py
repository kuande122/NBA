import streamlit as st  
from PIL import Image  
def teams_information(option):
  if option==option:
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
  if option=="Toronto Raptors":
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
  if option=="Chicago Bulls":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Chicago Bulls.png')
      st.image(image) 
    with col2:
       st.write("""# Chicago Bulls""")
       st.write("""##### 老闆:Michael Reinsdorf""")
       st.write("""##### GM:Marc Eversley""")
       st.write("""##### 總教練:Billy Donovan""")     
    st.write('芝加哥公牛(1966年-至今)') 
    st.write('芝加哥公牛隊的英文隊名為Chicago bulls，成立於1966年，目前所在城市是美國伊利諾州芝加哥（Chicago, Illinois），主場為聯合中心球館（United Center）。芝加哥是肉食加工業發達的城市，公牛對人們來說是力量的象徵，所以球隊以此命名。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "6  次")
    col2.metric("分組冠軍🏆", "6  次")   
  if option=="Cleveland Cavaliers":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Cleveland Cavaliers.png')
      st.image(image) 
    with col2:
       st.write("""# Cleveland Cavaliers""")
       st.write("""##### 老闆:Koby Altman""")
       st.write("""##### GM:Mike Gansey""")
       st.write("""##### 總教練:J.B.Bickerstaff""")     
    st.write('克里夫蘭騎士(1970年-至今)') 
    st.write('克里夫蘭騎士隊的英文隊名為Cleveland Cavaliers，球隊成立於1970年，目前所在城市是美國俄亥俄州克里夫蘭市(Cleveland, Ohio)，主場為速貸球館(Quicken Loans Arena)')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "5  次")   
  if option=="Detroit Pistons":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Detroit Pistons.png')
      st.image(image) 
    with col2:
       st.write("""# Detroit Pistons""")
       st.write("""##### 老闆:Ed Stefanski""")
       st.write("""##### GM:Troy Weaver""")
       st.write("""##### 總教練:Dwane Casey""")     
    st.write('韋恩堡左納活塞（NBL）(1941年–1948年)-韋恩堡活塞（BAA）(1948年–1949年)-韋恩堡活塞（NBA）(1949年–1957年)-底特律活塞(1957年–至今)') 
    st.write('底特律活塞隊的英文隊名為Detroit Pistons，成立於1946年，目前所在地區是美國密歇根州底特律，主場為奧本山宮殿球場。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "3  次")
    col2.metric("分組冠軍🏆", "7  次")   
  if option=="Indiana Pacers":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Indiana Pacers.png')
      st.image(image) 
    with col2:
       st.write("""# Indiana Pacers""")
       st.write("""##### 老闆:Kevin Pritchard""")
       st.write("""##### GM:Chad Buchanan""")
       st.write("""##### 總教練:Rick Carlisle""")     
    st.write('印第安納溜馬（ABA）(1967年-1976年)-印第安納溜馬（NBA）(1976年-至今)')
    st.write('印第安那溜馬隊的英文隊名為Indiana Pacers，球隊成立於1976年，目前所在城市是美國印第安那州印第安納波里斯(Indianapolis, Indiana)，主場為銀行家生活球館(Bankers Life Fieldhouse)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "1  次")   
  if option=="Milwaukee Bucks":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Milwaukee Bucks.png')
      st.image(image) 
    with col2:
       st.write("""# Milwaukee Bucks""")
       st.write("""##### 老闆:Peter Feigin""")
       st.write("""##### GM:Jon Horst""")
       st.write("""##### 總教練:Mike Budenholzer""")     
    st.write('密爾瓦基公鹿(1968年-至今)')
    st.write('密爾瓦基公鹿隊的英文隊名為Milwaukee Bucks，球隊成立於1968年，目前所在城市是美國威斯康辛州密爾瓦基市(Milwaukee, Wisconsin)，主場為布蘭德利中心球場(Bradley Center)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "2  次")
    col2.metric("分組冠軍🏆", "3  次")   
  if option=="Denver Nuggets":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Denver Nuggets.png')
      st.image(image) 
    with col2:
       st.write("""# Denver Nuggets""")
       st.write("""##### 老闆:Kroenke Sports & Entertainment""")
       st.write("""##### GM:Calvin Booth""")
       st.write("""##### 總教練:Michael Malone""")
    st.write('丹佛火箭（ABA）(1967年-1974年)丹佛金塊（ABA）(1974年-1976年)丹佛金塊（NBA）(1976年-)') 
    st.write('丹佛金塊隊的英文隊名為Denver Nuggets，球隊成立於1967年，所在地區是美國科羅拉多州丹佛市(Denver, Colorado)，主場為百事中心。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "0  次")   
  if option=="Minnesota Timberwolves":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Minnesota Timberwolves.jpeg')
      st.image(image) 
    with col2:
       st.write("""# Minnesota Timberwolves""")
       st.write("""##### 老闆:Glen Taylor""")
       st.write("""##### GM:Tim Connelly""")
       st.write("""##### 總教練:Chris Finch""")     
    st.write('明尼蘇達灰狼(1989年-–至今）') 
    st.write('明尼蘇達灰狼隊的英文隊名為Minnesota Timberwolves，球隊成立於1989年，所在地區是美國明尼蘇達州明尼阿波利斯市(Minneapolis, Minnesota)，主場為標靶中心球館(Target Center)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "0  次")   
  if option=="Oklahoma City Thunder":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Oklahoma City Thunder.png')
      st.image(image) 
    with col2:
       st.write("""# Oklahoma City Thunder""")
       st.write("""##### 老闆:Professional Basketball Club LLC (Clay Bennett, Chairman)""")
       st.write("""##### GM:Sam Presti""")
       st.write("""##### 總教練:Mark Daigneault""")     
    st.write('西雅圖超音速(1967年-2008年)俄克拉何馬城雷霆(2008年-現今)') 
    st.write('奧克拉荷馬雷霆隊的英文隊名為Oklahoma City Thunder，球隊成立於1967年，原名為西雅圖超音速隊，目前所在地區是美國奧克拉荷馬州奧克拉荷馬城(Oklahoma City, Oklahoma)，主場為切薩皮克能源球場(Chesapeake Energy Arena)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "4  次")   
  if option=="Portland Trail Blazers":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Portland Trail Blazers.png')
      st.image(image) 
    with col2:
       st.write("""# Portland Trail Blazers""")
       st.write("""##### 老闆:Paul G. Allen Trust (Jody Allen, chairwoman)""")
       st.write("""##### GM:Joe Cronin""")
       st.write("""##### 總教練:Chauncey Billups""")     
    st.write('波特蘭开拓者 (1970–-至今)') 
    st.write('波特蘭拓荒者隊的英文隊名為Portland Trail Blazers，球隊成立於1970年，所在地區是美國俄勒岡州波特蘭市(Portland, Oregon)，主場為摩達中心(Moda Center)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "3  次")    
  if option=="Utah Jazz":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Utah Jazz.jpeg')
      st.image(image) 
    with col2:
       st.write("""# Utah Jazz""")
       st.write("""##### 老闆:Ryan Smith""")
       st.write("""##### GM:Justin Zanik""")
       st.write("""##### 總教練:Will Hardy""")     
    st.write('紐奧良爵士(1974–1979)猶他爵士(1979年–-)') 
    st.write('猶他爵士隊的英文隊名為Utah Jazz，球隊成立於1974年，所在地區是美國猶他州鹽湖城，主場為能源方案球館。成立之初主場在紐奧良，是爵士樂的發源地，球隊也因此命名。1979年爵士隊主場移到猶他州鹽湖城，而隊名則繼續沿用至今。球隊剛建立的幾個賽季表現都不如人意，到1976年Elgin Baylor成為總教練後表現開始回穩，1983-1984年賽季爵士隊第一次打入季後賽，這一季中Adrian Delano Dantley球946次中投進813球，成為NBA史上第一位在第四節罰球得分超過800分的球員，至此以後爵士隊水準發揮穩定。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "2  次")   
