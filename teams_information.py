import streamlit as st  
from PIL import Image  
def teams_information(option,teams):
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
    teams="Boston Celtics"
    return teams

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
    
  if option=="Golden State Warriors":   #勇士
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Golden_State_Warriors.png')
      st.image(image) 
    with col2:
       st.write("""# Golden State Warriors""")
       st.write("""##### 老闆:Joe Lacob & Peter Guber""")
       st.write("""##### GM:Robert Michael "Bob" Myers""")
       st.write("""##### 總教練:Stephen Douglas "Steve" Kerr""")     
    st.write('費城勇士（1946年-1962年）-舊金山勇士（1962年-1971年）-金州勇士（1971年-至今）') 
    st.write('勇士成立於1946年，位於美國加利福尼亞州舊金山的美國職業籃球隊，分屬於NBA聯盟西區聯盟的太平洋組，主場球館為大通銀行中心。球隊的格言為「全隊即為一城」（The whole team is a city）。勇士隊是現今北美職業體育聯賽裡，少有的名稱不包含主場所在城市的隊伍')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "7  次")
    col2.metric("區冠軍🏆", "12  次")  
  
  if option=="Los Angeles Clippers":   #快艇
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Los_Angeles_Clippers.png')
      st.image(image) 
    with col2:
      st.write("""# Los Angeles Clippers""")
      st.write("""##### 老闆:Steve Anthony Ballmer""")
      st.write("""##### GM:Michael Winger""")
      st.write("""##### 總教練:Tyronn Jamar Lue""") 
    st.write('水牛城勇士（1970年-1978年）-聖地牙哥快艇（1978年-1984年）-洛杉磯快艇（1984年-至今）')
    st.write('快艇成立於1970年，位於美國加利福尼亞州洛杉磯的NBA籃球隊，分屬於西區的太平洋組，主場為加密貨幣網體育館，預計2024年將遷往英格伍德。球隊在1970年成立於水牛城，1978年遷至聖地牙哥，1984年再遷至現今的洛杉磯。2014年8月13日，由於前任老闆在該年季後賽期間的言論爭議，前微軟CEOSteve Anthony Ballmer成功收購洛杉磯快艇，正式接替Donald Sterling成為球隊新任老闆')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "0  次")
    col2.metric("區冠軍🏆", "0  次")
  
  if option=="Los Angeles Lakers":   #湖人
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Los_Angeles_Lakers.png')
      st.image(image) 
    with col2:
      st.write("""# Los Angeles Lakers""")
      st.write("""##### 老闆:Jerry Buss & Todd Boehly & Patrick Soon-Shiong""")
      st.write("""##### GM:Robert Todd Pelinka Jr.""")
      st.write("""##### 總教練:Darvin Ham""") 
    st.write('底特律寶石(1946年-1947年)-明尼亞波利斯湖人(1947年-1959年)-洛杉磯湖人(1960年-至今')
    st.write('湖人成立於1946年，位於美國加利福尼亞州洛杉磯的職業籃球隊，隸屬於NBA西區太平洋組，主場為加密貨幣網體育館。球隊前身為「明尼亞波利斯湖人」（Minneapolis Lakers）。至今共奪得17次總冠軍，與東區球隊波士頓塞爾提克並列NBA第一。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "17  次")
    col2.metric("區冠軍🏆", "32  次")

  if option=="Phoenix Suns":   #太陽
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Phoenix_Suns.png')
      st.image(image) 
    with col2:
      st.write("""# Phoenix Suns""")
      st.write("""##### 老闆:Robert Gary Sarver""")
      st.write("""##### GM:James Jones""")
      st.write("""##### 總教練:Montgomery Eli Williams""") 
    st.write('鳳凰城太陽（1968-至今）')
    st.write('太陽成立於1968年，位於美國亞利桑那州鳳凰城的職業籃球隊，分屬於NBA西區太平洋組，是該組唯一不在加利福尼亞州的球隊，主場為足跡中心。共有10位入選籃球名人堂的球員曾效力過太陽，其中Charles Wade Barkley及Stephen John Nash更在效力期間榮獲最有價值球員。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "0  次")
    col2.metric("區冠軍🏆", "3  次")

  if option=="Sacramento Kings":   #國王
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Sacramento_Kings.png')
      st.image(image) 
    with col2:
      st.write("""# Sacramento Kings""")
      st.write("""##### 老闆:Vivek Ranadivé""")
      st.write("""##### GM:Monte McNair""")
      st.write("""##### 總教練:Michael “Mike” Brown""") 
    st.write('羅徹斯特皇家(1945年-1957年)-辛辛那提皇家(1957年-1972年)-堪薩斯城•奧馬哈國王(1972年-1975年)-堪薩斯城國王(1975年-1985年)-沙加緬度國王(1950年-至今)')
    st.write('國王成立於1950年，位於美國加利福尼亞州沙加緬度的NBA籃球隊，分屬於西區的太平洋組。國王隊於2016-17 NBA賽季遷入位於沙加緬度市中心的新主場金州第一中心。沙加緬度市已經是國王隊駐紮過的第5座城市，而國王隊於2012年可能又要考慮遷移主場去洛杉磯地區，但是遭到了洛杉磯湖人和洛杉磯快艇的強烈抵制')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "1  次")
    col2.metric("區冠軍🏆", "1  次")
    
  if option=="Atlanta Hawks":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Atlanta_Hawks.png')
      st.image(image) 
    with col2:
       st.write("""### Atlanta Hawks""")
       st.write("""##### 老闆:Tony Ressler""")
       st.write("""##### GM:Landry Fields""")
       st.write("""##### 總教練:Nate McMillan""")     
    st.write('水牛城野牛（1946年）三城黑鷹（1946年-1951年）密爾瓦基老鷹（1951年-1955年）聖路易斯老鷹（1955年-1968年）亞特蘭大老鷹（1968年-至今）') 
    st.write('亞特蘭大老鷹的英文隊名為Atlanta Hawks，老鷹隊之名象徵著速度和進攻，球隊成立於1946年，在1949年加入NBA，是NBA的元老之一。目前所在城市是美國喬治亞州亞特蘭大市(Atlanta, Georgia)，主場為飛利浦球場(Philips Arena)。球隊最初名為「三城黑鷹隊」，1951年主場遷移到密爾瓦基市，改名「密爾瓦基鷹隊」，直到1968年主場移到亞特蘭大後才改成現在的亞特蘭大老鷹隊。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "4  次")   
    
  if option=="Charlotte Hornets":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Charlotte Hornets.png')
      st.image(image) 
    with col2:
       st.write("""### Charlotte Hornets""")
       st.write("""##### 老闆:Michael Jordan""")
       st.write("""##### GM:Mitch Kupchak""")
       st.write("""##### 總教練:Steve Clifford""")     
    st.write('夏洛特黃蜂（1988年–2002年）夏洛特山貓（2004年–2014年）夏洛特黃蜂（1988年–2002年、2014年–至今）') 
    st.write('夏洛特黃蜂隊的英文隊名為Charlotte Hornets，球隊成立於2004年，目前所在城市是美國北卡羅來納州夏洛特市(Charlotte, North Carolina)，主場為時代華納中心球館(Time Warner Cable Arena)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "0  次")   
    
  if option=="Miami Heat":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Miami Heat.png')
      st.image(image) 
    with col2:
       st.write("""### Miami Heat""")
       st.write("""##### 老闆:Micky Arison""")
       st.write("""##### GM:Andy Elisburg""")
       st.write("""##### 總教練:	Erik Spoelstra""")     
    st.write('邁阿密熱火(1988年--至今）') 
    st.write('邁阿密熱火的英文隊名為Miami Heat，成立於1988年，目前所在地區是美國佛羅里達州邁阿密市(Miami, Florida)，主場為美國航空競技館(American Airlines Arena)，熱火隊的三巨頭分別是Dwyane Wade、LeBron James和Chris Bosh。1988年才加入NBA的年輕隊伍，在2005年-06年賽季首度通過東部決賽，打入總冠軍賽，在面對達拉斯小牛隊時原本連輸兩局，但最終倒贏小牛隊以4：2逆轉擊敗而奪冠。直到2011年再度打入NBA總決賽，對手同樣是2006年時遇到的小牛隊，這次邁阿密熱火隊以2：4未能奪得總冠軍，不過2012年再度打入NBA總決賽，對手是奧克拉荷馬雷霆隊，這次邁阿密熱火隊以4：1奪得總冠軍。2013年三度打入NBA總決賽，對手是拿過四次NBA總冠軍的聖安東尼奧馬刺隊，經過激戰七場，邁阿密熱火隊以4：3奪得總冠軍完成二連霸。2014年熱火再次於總決賽和馬刺隊碰頭，然而最終以1：4終止三連霸美夢。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "3  次")
    col2.metric("分組冠軍🏆", "6  次")   
  if option=="Orlando Magic":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Orlando Magic.png')
      st.image(image) 
    with col2:
       st.write("""### Orlando Magic""")
       st.write("""##### 老闆:RDV Sports, Inc.(Dan DeVos, chairman)""")
       st.write("""##### GM:John Hammond""")
       st.write("""##### 總教練:Jamahl Mosley""")     
    st.write('奧蘭多魔術(1989年-至今)') 
    st.write('奧蘭多魔術隊的英文隊名為Orlando Magic，球隊成立於1989年，所在地區是美國佛羅里達州奧蘭多市(Orlando, Florida)，主場為安利中心(Amway Center)。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "0  次")
    col2.metric("分組冠軍🏆", "2  次")    
    
  if option=="Washington Wizards":
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Washington Wizards.png')
      st.image(image) 
    with col2:
       st.write("""### Washington Wizards""")
       st.write("""##### 老闆:Monumental Sports & Entertainment""")
       st.write("""##### GM:Tommy Sheppard""")
       st.write("""##### 總教練:Wes Unseld Jr.""")     
    st.write('芝加哥包裝工(1961年-1962年)芝加哥西風(1962年-1963年)巴爾的摩子彈(1963年-1972年)首都子彈(1973年-1974年)華盛頓子彈(1974年-1997年)華盛頓巫師(1997年-)') 
    st.write('華盛頓巫師隊的英文隊名為Washington Wizards，球隊成立於1961年，目前所在城市是美國華盛頓特區(Washington, D.C.)，現在主場為Verizon Center(原MIC中心球館 MCI Center)。巫師隊是隊名變化最頻繁的一支球隊，在1961年加入NBA時主場在芝加哥所以取名芝加哥包裝工隊，第二年改名芝加哥和風隊，第三年因為主場遷移到工業城市巴爾的摩，而改名巴爾的摩子彈隊，後來主場又移到華盛頓，隊名更動為華盛頓子彈隊，在1997年-1998年賽季則改為現在的華盛頓巫師隊。')
    col1, col2= st.columns(2)
    col1.metric("聯盟冠軍🏆", "1  次")
    col2.metric("分組冠軍🏆", "4  次")   
  
  if option=="Dallas Mavericks":   #獨行俠
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Dallas_Mavericks.png')
      st.image(image) 
    with col2:
       st.write("""# Dallas Mavericks""")
       st.write("""##### 老闆:Mark Cuban""")
       st.write("""##### GM:Nico Harrison""")
       st.write("""##### 總教練:Jason Frederick kidd""")     
    st.write('達拉斯獨行俠(1980年-至今)') 
    st.write('獨行俠最初由唐・卡特和Norm Sonju於1979年創辦。他們請求NBA聯盟准許於德克薩斯州建立一隊NBA球隊。達拉斯城的最後一隊職業籃球隊是美國籃球協會（ABA，後併入NBA）的達拉斯叢林隊，但由於ABA併入NBA，達拉斯叢林隊在1973年改組成為現今的聖安東尼奧馬刺隊而且把主場遷移到聖安東尼奧。從此，達拉斯城就沒有職業籃球隊伍了。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "1  次")
    col2.metric("區冠軍🏆", "2  次")  
  
  if option=="Houston Rockets":   #火箭
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Houston_Rockets.png')
      st.image(image) 
    with col2:
      st.write("""# Houston Rockets""")
      st.write("""##### 老闆:Tilman Fertitta""")
      st.write("""##### GM:Rafel Stone""")
      st.write("""##### 總教練:Stephen Silas""") 
    st.write('聖地牙哥火箭（1967年-1971年）-休士頓火箭（1971年-至今）')
    st.write('火箭隊成立於1967年，目前所在地區是美國德克薩斯州休士頓市，主場為豐田中心球館。休士頓因為有NASA的存在，讓人容易聯想到「火箭隊」這名稱是否和太空有瓜葛，但其實火箭隊最開始的主場在聖地牙哥，而火箭的涵意則是代表著速度和高遠的意思。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "0  次")
    col2.metric("區冠軍🏆", "0  次")

  if option=="Memphis Grizzlies":   #灰熊
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/Memphis_Grizzlies.png')
      st.image(image) 
    with col2:
      st.write("""# Memphis Grizzlies""")
      st.write("""##### 老闆:Robert Pera""")
      st.write("""##### GM:Zach Kleiman""")
      st.write("""##### 總教練:Taylor Vetter Jenkins""") 
    st.write('溫哥華灰熊(1995年-2001年)-曼非斯灰熊(2001年-至今)')
    st.write('灰熊成立於1995年，位於美國田納西州曼非斯的NBA籃球隊，分屬於西區的西南組，主場為聯邦快遞廣場。現任總教練為Taylor Vetter Jenkins。1995年，球隊創立於溫哥華，命名溫哥華灰熊（Vancouver Grizzlies），是第二支非美國本土的NBA球隊（第一支是多倫多暴龍）。2001年，球隊遷至美國曼非斯，更名為現今的曼非斯灰熊。因此，灰熊不再是非美國本土的NBA球隊。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "0  次")
    col2.metric("區冠軍🏆", "0  次")
  
  if option=="New Orleans Pelicans":   #鵜鶘
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/New_Orleans_Pelicans.png')
      st.image(image) 
    with col2:
      st.write("""# New Orleans Pelicans""")
      st.write("""##### 老闆:Gayle Benson""")
      st.write("""##### GM:Trajan Shaka Langdon""")
      st.write("""##### 總教練:Willie J. Green""") 
    st.write('紐奧良黃蜂(2002年-2005年)(2007年-2013年)-紐奧良/奧克拉荷馬市黃蜂(2005年-2007年)-紐奧良鵜鶘(2013年-至今)')
    st.write('鵜鶘成立於2002年，位於美國路易斯安那州紐奧良的NBA籃球隊，分屬於西區的西南組，主場為冰沙國王中心。目前球隊的擁有者是汽車業界大亨Gayle Benson，現任總教練是Willie J. Green。紐奧良鵜鶘的前身為紐奧良黃蜂（New Orleans Hornets），為2002年夏洛特黃蜂遷至紐奧良時所改名成立的。2005年，由於紐奧良受到颶風卡崔娜侵襲而嚴重損毀，球隊一度遷移主場至奧克拉荷馬市，直到2007年才重返紐奧良。2013年4月，球隊更名為現今的紐奧良鵜鶘。2014年，球隊將原先所擁有的夏洛特黃蜂隊名與1988年至2002年的球季記錄，回歸至夏洛特，由夏洛特黃蜂接收。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "0  次")
    col2.metric("區冠軍🏆", "0  次")

  if option=="San Antonio Spurs":   #馬刺
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams logo/San_Antonio_Spurs.png')
      st.image(image) 
    with col2:
      st.write("""# San Antonio Spurs""")
      st.write("""##### 老闆:Spurs Sports & Entertainment""")
      st.write("""##### GM:Brian Wright""")
      st.write("""##### 總教練:Gregg Popovich""") 
    st.write('達拉斯矮樹叢(1967年-1970年)(1971年–1973年)-德克薩斯矮樹叢(1970年-1971年)-聖安東尼奧馬刺(1973年-1976年)-聖安東尼奧馬刺(1976年-至今)')
    st.write('馬刺成立於1967年，位於美國德克薩斯州聖安東尼奧國家籃球協會（NBA聯盟）旗下職業球隊，分屬於西區西南賽區，球隊主場為AT&T中心。目前球隊之所有人為Peter John Holt，總教練則是Gregg Popovich。球隊最初是美國籃球協會（ABA）達拉斯叢林隊，也是ABA與NBA合併後，獲得過NBA總冠軍前ABA球隊。馬刺一共先後於1998–99賽季、2002–03賽季、2004–05賽季、2006–07賽季、2013–14賽季獲得過5次總冠軍，而且馬刺奪下5次總冠軍中「石佛」Timothy Theodore Duncan就拿下了3次FMVP。')
    col1, col2= st.columns(2)
    col1.metric("總冠軍🏆", "5  次")
    col2.metric("區冠軍🏆", "6  次")
st.write(teams)
