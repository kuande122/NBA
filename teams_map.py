import streamlit as st  
import folium 
from PIL import Image  
from streamlit_folium import folium_static 

def teams_map(option_teams):
  if option_teams=="Boston Celtics":
    st.markdown('### 主場: TD Garden')
    col1,col2 = st.columns((6,4))
    with col1: 
        TDGarden= folium.Map(location=[42.36622394101576, -71.06214665765047], zoom_start=16)
              # add marker for Liberty Bell
        tooltip = "TD Garden"
        folium.Marker([42.36622394101576, -71.06214665765047], popup="TD Garden", tooltip=tooltip
        ).add_to(TDGarden)
        folium_static(TDGarden)
        st.markdown('#### 地址：100 Legends Way, Boston, MA 02114美國')
        st.markdown('#### 觀眾席數：18624席')
    with col2:
        image = Image.open('Home/TD Garden.jpg')
        st.image(image)              
        image1 = Image.open('Home/TD Garden1.jpg')
        st.image(image1)
        
        
  if option_teams=="Brooklyn Nets":
    st.markdown('### 主場: Barclays Center')
    col1,col2 = st.columns((6,4))
    with col1: 
        BarclaysCenter= folium.Map(location=[40.682725423383374, -73.97526212020857], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Barclays Center"
        folium.Marker([40.682725423383374, -73.97526212020857], popup="Barclays Center", tooltip=tooltip
        ).add_to(BarclaysCenter)
        folium_static(BarclaysCenter)  
        st.markdown('#### 地址：620 Atlantic Ave, Brooklyn, NY 11217美國')
        st.markdown('#### 觀眾席數：17732席')
    with col2:
        image = Image.open('Home/Barclays Center.jpg')       
        st.image(image)
        image1 =Image.open('Home/Barclays Center1.jpg')
        st.image(image1)
    
    
  if option_teams=="New York Knicks":
    st.markdown('### 主場: MSG The Garden')
    col1,col2 = st.columns((6,4))
    with col1: 
        MSGTheGarden= folium.Map(location=[40.7505, -73.99352], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "MSG The Garden"
        folium.Marker([40.7505, -73.99352], popup="MSG The Garden", tooltip=tooltip
        ).add_to(MSGTheGarden)
        folium_static(MSGTheGarden)
        st.markdown('#### 地址：4 Pennsylvania Plaza, New York, NY 10001美國')
        st.markdown('#### 觀眾席數：19812席') 
    with col2:
        image = Image.open('Home/MSGTheGarden.jpg')       
        st.image(image)
        image1 =Image.open('Home/MSGTheGarden1.jpg')
        st.image(image1)
    

  if option_teams=="Philadelphia 76ers":
    st.markdown('### 主場: Wells Fargo Center')
    col1,col2 = st.columns((6,4))
    with col1:   
        wellsfargocenter= folium.Map(location=[39.90130024709659, -75.17162545031324], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Wells Fargo Center"
        folium.Marker([39.90130024709659, -75.17162545031324], popup="Wells Fargo Center", tooltip=tooltip
        ).add_to(wellsfargocenter)
        folium_static(wellsfargocenter)
        st.markdown('#### 地址：3601 S Broad St, Philadelphia, PA 19148美國')
        st.markdown('#### 觀眾席數：21000席')
    with col2:
        image = Image.open('Home/wellsfargocenter.jpg')       
        st.image(image)      
        image1 =Image.open('Home/wellsfargocenter1.jpg')
        st.image(image1)
        
        
        
  if option_teams=="Toronto Raptors":
    st.markdown('### 主場: Scotiabank Arena')
    col1,col2 = st.columns((6,4))
    with col1:  
        ScotiabankArena= folium.Map(location=[43.643485488886185, -79.37908251728793], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Scotiabank Arena"
        folium.Marker([43.643485488886185, -79.37908251728793], popup="Scotiabank Arena", tooltip=tooltip
        ).add_to(ScotiabankArena)
        folium_static(ScotiabankArena)
        st.markdown('#### 地址：40 Bay St., Toronto, ON M5J 2X2加拿大')
        st.markdown('#### 觀眾席數：19800席')    
    with col2:
        image = Image.open('Home/ScotiabankArena.jpg')       
        st.image(image)
        image1 =Image.open('Home/ScotiabankArena1.jpg')
        st.image(image1)
        
        
  if option_teams=="Chicago Bulls":
    st.markdown('### 主場: United Center')
    col1,col2 = st.columns((6,4))
    with col1:
        UnitedCenter= folium.Map(location=[41.880708350972725, -87.67417027269533], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "United Center"
        folium.Marker([41.880708350972725, -87.67417027269533], popup="United Center", tooltip=tooltip
        ).add_to(UnitedCenter)
        folium_static(UnitedCenter)
        st.markdown('#### 地址：1901 W Madison St, Chicago, IL 60612美國')
        st.markdown('#### 觀眾席數：21879席')  
    with col2:    
        image = Image.open('Home/United Center.jpg')
        st.image(image)     
        image1 = Image.open('Home/United Center1.png')
        st.image(image1)   
        
        
  if option_teams=="Cleveland Cavaliers":
    st.markdown('### 主場: Quicken Loans Arena')
    col1,col2 = st.columns((6,4))
    with col1:  
        QuickenLoansArena= folium.Map(location=[41.49661457628494, -81.68800263971569], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Quicken Loans Arena"
        folium.Marker([41.49661457628494, -81.68800263971569], popup="Quicken Loans Arena", tooltip=tooltip
        ).add_to(QuickenLoansArena)
        folium_static(QuickenLoansArena)
        st.markdown('#### 地址：1 Center Court, Cleveland, OH 44115美國')
        st.markdown('#### 觀眾席數：20562席')
    with col2:
        image = Image.open('Home/Quicken Loans Arena.jpg')       
        st.image(image)
        image1 =Image.open('Home/Quicken Loans Arena1.jpg')
        st.image(image1)
    
    
  if option_teams=="Detroit Pistons":
    st.markdown('### 主場: Little Caesars Arena')
    col1,col2 = st.columns((6,4))
    with col1:  
        LittleCaesarsArena= folium.Map(location=[42.3412532527852, -83.05525657294322], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Little Caesars Arena"
        folium.Marker([42.3412532527852, -83.05525657294322], popup="Little Caesars Arena", tooltip=tooltip
        ).add_to(LittleCaesarsArena)
        folium_static(LittleCaesarsArena)
        st.markdown('#### 地址:2645 Woodward Ave, Detroit, MI 48201美國')
        st.markdown('#### 觀眾席數:21000席')
    with col2:   
        image = Image.open('Home/LittleCaesarsArena.jpg')       
        st.image(image)
        image1 =Image.open('Home/LittleCaesarsArena1.jpg')
        st.image(image1)
    

  if option_teams=="Indiana Pacers":
    st.markdown('### 主場: Gainbridge Fieldhouse')
    col1,col2 = st.columns((6,4))
    with col1:  
        GainbridgeFieldhouse= folium.Map(location=[39.76423306239759, -86.15505390428618], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Gainbridge Fieldhouse"
        folium.Marker([39.76423306239759, -86.15505390428618], popup="Gainbridge Fieldhouse", tooltip=tooltip
        ).add_to(GainbridgeFieldhouse)
        folium_static(GainbridgeFieldhouse)
        st.markdown('#### 地址：125 S Pennsylvania St, Indianapolis, IN 46204美國')
        st.markdown('#### 觀眾席數：17923席')

    with col2:
        image = Image.open('Home/GainbridgeFieldhouse.jpg')       
        st.image(image)
        image1 =Image.open('Home/GainbridgeFieldhouse1.jpg')
        st.image(image1)
   
  if option_teams=="Milwaukee Bucks":
    st.markdown('### 主場: Fiserv Forum')
    col1,col2 = st.columns((6,4))
    with col1:
        FiservForum= folium.Map(location=[43.0451977912526, -87.91697850606084], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Fiserv Forum"
        folium.Marker([43.0451977912526, -87.91697850606084], popup="Fiserv Forum", tooltip=tooltip
        ).add_to(FiservForum)
        folium_static(FiservForum)
        st.markdown('#### 地址：1111 Vel R. Phillips Ave, Milwaukee, WI 53203美國')
        st.markdown('#### 觀眾席數：17385席')      
   
    with col2:
        image = Image.open('Home/FiservForum.jpg')       
        st.image(image)
        image1 =Image.open('Home/FiservForum1.jpg')
        st.image(image1)
    

  if option_teams=="Atlanta Hawks":
    st.markdown('### 主場: State Farm Arena')
    col1,col2 = st.columns((6,4))
    with col1:
        StateFarmArena= folium.Map(location=[33.75737827997708, -84.39633513151331], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "State Farm Arena"
        folium.Marker([33.75737827997708, -84.39633513151331], popup="State Farm Arena", tooltip=tooltip
        ).add_to(StateFarmArena)
        folium_static(StateFarmArena)
        st.markdown('#### 地址：1 State Farm Dr, Atlanta, GA 30303美國')
        st.markdown('#### 觀眾席數：18371席')
       
    with col2:     
        image = Image.open('Home/State Farm Arena.jpeg')
        st.image(image)   
        image1 = Image.open('Home/State Farm Arena1.jpeg')
        st.image(image1)
    
  
  if option_teams=="Charlotte Hornets":
    st.markdown('### 主場: Spectrum Center')
    col1,col2 = st.columns((6,4))
    with col1: 
        SpectrumCenter= folium.Map(location=[35.22528408738218, -80.83934793137779], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Spectrum Center"
        folium.Marker([35.22528408738218, -80.83934793137779], popup="Spectrum Center", tooltip=tooltip
        ).add_to(SpectrumCenter)
        folium_static(SpectrumCenter)
        st.markdown('#### 地址：333 E Trade St, Charlotte, NC 28202美國')
        st.markdown('#### 觀眾席數：20200席')

    with col2:
        image = Image.open('Home/Spectrum Center.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Spectrum Center1.jpeg')
        st.image(image1)
    
  
  if option_teams=="Miami Heat":
    st.markdown('### 主場: FTX Arena')
    col1,col2 = st.columns((6,4))
    with col1:  
        FTXArena= folium.Map(location=[25.78136, -80.18793], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "FTX Arena"
        folium.Marker([25.78136, -80.18793], popup="FTX Arena", tooltip=tooltip
        ).add_to(FTXArena)
        folium_static(FTXArena)
        st.markdown('#### 地址：601 Biscayne Blvd, Miami, FL 33132美國')
        st.markdown('#### 觀眾席數：19600席')
        
    with col2:
        image = Image.open('Home/FTX Arena.jpeg')       
        st.image(image)
        image1 =Image.open('Home/FTX Arena1.jpg')
        st.image(image1)
  if option_teams=="Orlando Magic":
    st.markdown('### 主場: Amway Center')
    col1,col2 = st.columns((6,4))
    with col1:  
        AmwayCenter= folium.Map(location=[28.539343909610295, -81.38387496040187], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Amway Center"
        folium.Marker([28.539343909610295, -81.38387496040187], popup="Amway Center", tooltip=tooltip
        ).add_to(AmwayCenter)
        folium_static(AmwayCenter)
        st.markdown('#### 地址：400 W Church St Suite 200, Orlando, FL 32801美國')
        st.markdown('#### 觀眾席數：18846席')
        
    with col2:
        image = Image.open('Home/Amway Center.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Amway Center1.jpeg')
        st.image(image1)
    
  
  if option_teams=="Washington Wizards":
    st.markdown('### 主場: Capital One Arena')
    col1,col2 = st.columns((6,4))
    with col1:        
        CapitalOneArena= folium.Map(location=[38.89830942692672, -77.02088898904876], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Capital One Arena"
        folium.Marker([38.89830942692672, -77.02088898904876], popup="Capital One Arena", tooltip=tooltip
        ).add_to(CapitalOneArena)
        folium_static(CapitalOneArena)
        st.markdown('#### 地址：601 F St NW, Washington, DC 20004美國')
        st.markdown('#### 觀眾席數：20,356席')
    with col2:
        image = Image.open('Home/Capital One Arena.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Capital One Arena1.jpeg')
        st.image(image1)
   
  if option_teams=="Denver Nuggets":
    st.markdown('### 主場: Ball Arena')
    col1,col2 = st.columns((6,4))
    with col1:
        BallArena= folium.Map(location=[39.74868, -105.00758], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Ball Arena"
        folium.Marker([39.74868, -105.00758], popup="Ball Arena", tooltip=tooltip
        ).add_to(BallArena)
        folium_static(BallArena)
        st.markdown('#### 地址：1000 Chopper Cir, Denver, CO 80204美國')
        st.markdown('#### 觀眾席數：19155席')     
    with col2:   
        image = Image.open('Home/Ball Arena .jpeg')
        st.image(image) 
        image1 = Image.open('Home/Ball Arena 1.jpeg')
        st.image(image1)
   
  
  if option_teams=="Minnesota Timberwolves":
    st.markdown('### 主場: Target Center')
    col1,col2 = st.columns((6,4))
    with col1:
        TargetCenter= folium.Map(location=[44.97956, -93.27617], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Target Center"
        folium.Marker([44.97956, -93.27617], popup="Target Center", tooltip=tooltip
        ).add_to(TargetCenter)
        folium_static(TargetCenter)
        st.markdown('#### 地址：600 N 1st Ave, Minneapolis, MN 55403美國')
        st.markdown('#### 觀眾席數：18798席')      
    with col2:
        image = Image.open('Home/Target Center.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Target Center1.jpeg')
        st.image(image1)
   
  if option_teams=="Oklahoma City Thunder":
    st.markdown('### 主場: Chesapeake Energy Arena')
    col1,col2 = st.columns((6,4))
    with col1: 
        ChesapeakeEnergyArena= folium.Map(location=[35.4634, -97.5151], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Chesapeake Energy Arena"
        folium.Marker([35.4634, -97.5151], popup="Chesapeake Energy Arena", tooltip=tooltip
        ).add_to(ChesapeakeEnergyArena)
        folium_static(ChesapeakeEnergyArena)
        st.markdown('#### 地址：100 W Reno Ave, Oklahoma City, OK 73102美國')
        st.markdown('#### 觀眾席數：18203席') 
    with col2:
        image = Image.open('Home/Chesapeake Energy Arena .jpeg')       
        st.image(image)
        image1 =Image.open('Home/Chesapeake Energy Arena1.jpeg')
        st.image(image1)
    
  if option_teams=="Portland Trail Blazers":
    st.markdown('### 主場: Moda Center')
    col1,col2 = st.columns((6,4))
    with col1:   
        ModaCenter= folium.Map(location=[45.53158, -122.66685], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Moda Center"
        folium.Marker([45.53158, -122.66685], popup="Moda Center", tooltip=tooltip
        ).add_to(ModaCenter)
        folium_static(ModaCenter)
        st.markdown('#### 地址：1 N Center Ct St, Portland, OR 97227美國')
        st.markdown('#### 觀眾席數：20630席')
    with col2:
        image = Image.open('Home/Moda Center.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Moda Center1.jpeg')
        st.image(image1)
 
  if option_teams=="Utah Jazz":
    st.markdown('### 主場: Vivint Arena')
    col1,col2 = st.columns((6,4))
    with col1:
        VivintArena= folium.Map(location=[40.76832, -111.90108], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Vivint Arena"
        folium.Marker([40.76832, -111.90108], popup="Vivint Arena", tooltip=tooltip
        ).add_to(VivintArena)
        folium_static(VivintArena)
        st.markdown('#### 地址：301 S Temple, Salt Lake City, UT 84101美國')
        st.markdown('#### 觀眾席數：20000席')  

    with col2:
        image = Image.open('Home/Vivint Arena.jpeg')       
        st.image(image)
        image1 =Image.open('Home/Vivint Arena1.jpeg')
        st.image(image1)
  if option_teams=="Golden State Warriors":
    st.markdown('### 主場: Chase Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Chase_Center= folium.Map(location=[37.768056, -122.3875], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Chase Center"
        folium.Marker([37.768056, -122.3875], popup="Chase Center", tooltip=tooltip
        ).add_to(Chase_Center)
        folium_static(Chase_Center)
        st.markdown('#### 地址：1 Warriors Way, San Francisco, CA 94158美國')
        st.markdown('#### 觀眾席數：18064席')           
    with col2:       
        image = Image.open('Home/Chase_Center.jpg')
        st.image(image)   
        image1 = Image.open('Home/Chase_Center_Tickets.jpg')
        st.image(image1)
    
  
  if option_teams=="Los Angeles Clippers":
    st.markdown('### 主場: Staples Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Staples_Center= folium.Map(location=[34.043056, -118.267222], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Staples Center"
        folium.Marker([34.043056, -118.267222], popup="Staples Center", tooltip=tooltip
        ).add_to(Staples_Center)
        folium_static(Staples_Center)
        st.markdown('#### 地址：1111 S Figueroa St, Los Angeles, CA 90015美國')
        st.markdown('#### 觀眾席數：19060人')
        
    with col2:
        image = Image.open('Home/Staples_Center.jpg')
        st.image(image)        
        image1 = Image.open('Home/Staples_Center_Tickets.jpg')
        st.image(image1)
   
  if option_teams=="Los Angeles Lakers":
    st.markdown('### 主場: Staples Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Staples_Center= folium.Map(location=[34.043056, -118.267222], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Staples Center"
        folium.Marker([34.043056, -118.267222], popup="Staples Center", tooltip=tooltip
        ).add_to(Staples_Center)
        folium_static(Staples_Center)
        st.markdown('#### 地址：1111 S Figueroa St, Los Angeles, CA 90015美國')
        st.markdown('#### 觀眾席數：19060人')
        
    with col2:
        image = Image.open('Home/Staples_Center.jpg')
        st.image(image)        
        image1 = Image.open('Home/Staples_Center_Tickets.jpg')
        st.image(image1)
    
  
  if option_teams=="Phoenix Suns":
    st.markdown('### 主場: Footprint Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Footprint_Center= folium.Map(location=[33.445833,-112.071389], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "FootprintCenter"
        folium.Marker([33.445833,-112.071389], popup="Footprint Center", tooltip=tooltip
        ).add_to(Footprint_Center)
        folium_static(Footprint_Center)
        st.markdown('#### 地址：US Airways Center, 201S 1st St, Phoenix, AZ 85004美國')
        st.markdown('#### 觀眾席數：18422人')
     
    with col2:     
        image = Image.open('Home/Footprint_Center.jpg')
        st.image(image)       
        image1 = Image.open('Home/Footprint_Center_Tickets.jpg')
        st.image(image1)
    

  if option_teams=="Sacramento Kings":
    st.markdown('### 主場: Golden1 Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Golden1_Center= folium.Map(location=[38.580361, -121.499611], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Golden1Center"
        folium.Marker([38.580361, -121.499611], popup="Golden1 Center", tooltip=tooltip
        ).add_to(Golden1_Center)
        folium_static(Golden1_Center)
        st.markdown('#### 地址：500 David J Stern Walk, Sacramento, CA 95814美國')
        st.markdown('#### 觀眾席數：17500人')  
         
    with col2:       
        image = Image.open('Home/Golden1_Center.jpg')
        st.image(image)     
        image1 = Image.open('Home/Golden1_Center_Tickets.jpg')
        st.image(image1)
   
  if option_teams=="Dallas Mavericks":
    st.markdown('### 主場: American Airlines Center')
    col1,col2 = st.columns((6,4))
    with col1:
        American_Airlines_Center= folium.Map(location=[32.790556, -96.810278], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "American Airlines Center"
        folium.Marker([32.790556, -96.810278], popup="American Airlines Center", tooltip=tooltip
        ).add_to(American_Airlines_Center)
        folium_static(American_Airlines_Center)
        st.markdown('#### 地址：2500 Victory Ave, Dallas, TX 75219美國')
        st.markdown('#### 觀眾席數：20000-21041席')
      
    with col2:   
        image = Image.open('Home/American_Airlines_Center.jpg')
        st.image(image)  
        image1 = Image.open('Home/American_Airlines_Center_Tickets.jpg')
        st.image(image1)
    
  
  if option_teams=="Houston Rockets":
    st.markdown('### 主場:Toyota Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Toyota_Center= folium.Map(location=[29.750833, -95.362222], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Toyota Center"
        folium.Marker([29.750833, -95.362222], popup="Toyota Center", tooltip=tooltip
        ).add_to(Toyota_Center)
        folium_static(Toyota_Center)
        st.markdown('#### 地址：1510 Polk St, Houston, TX 77002美國')
        st.markdown('#### 觀眾席數：18300人')

    with col2:     
        image = Image.open('Home/Toyota_Center.jpg')
        st.image(image)        
        image1 = Image.open('Home/Toyota_Center_Tickets.jpg')
        st.image(image1)
    
  if option_teams=="Memphis Grizzlies":
    st.markdown('### 主場: FedExForum Center')
    col1,col2 = st.columns((6,4))
    with col1:
        FedExForum_Center= folium.Map(location=[35.138333, -90.050556], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "FedExForum Center"
        folium.Marker([35.138333, -90.050556], popup="FedExForum Center", tooltip=tooltip
        ).add_to(FedExForum_Center)
        folium_static(FedExForum_Center)
        st.markdown('#### 地址：191 Beale St, Memphis, TN 38103美國')
        st.markdown('#### 觀眾席數：17794人')
           
    with col2:   
        image = Image.open('Home/FedExForum_Center.jpg')
        st.image(image)   
        image1 = Image.open('Home/FedExForum_Center_Tickets.jpg')
        st.image(image1)
    
    
  if option_teams=="New Orleans Pelicans":
    st.markdown('### 主場: Smoothie King Center')
    col1,col2 = st.columns((6,4))
    with col1:
        Smoothie_King_Center= folium.Map(location=[29.948889, -90.081944], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "Smoothie King Center"
        folium.Marker([29.948889, -90.081944], popup="Smoothie King Center", tooltip=tooltip
        ).add_to(Smoothie_King_Center)
        folium_static(Smoothie_King_Center)
        st.markdown('#### 地址：1501 Dave Dixon Dr, New Orleans, LA 70113美國')
        st.markdown('#### 觀眾席數：16867人')
   
    with col2:      
        image = Image.open('Home/Smoothie_King_Center.jpg')
        st.image(image)        
        image1 = Image.open('Home/Smoothie_King_Center_Tickets.jpg')
        st.image(image1)
    
  if option_teams=="San Antonio Spurs":
    st.markdown('### 主場: ATT Center')
    col1,col2 = st.columns((6,4))
    with col1:
        ATT_Center= folium.Map(location=[29.426944, -98.4375], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "ATT Center"
        folium.Marker([29.426944, -98.4375], popup="ATT Center", tooltip=tooltip
        ).add_to(ATT_Center)
        folium_static(ATT_Center)
        st.markdown('#### 地址：1 AT&T Center Parkway, San Antonio, TX 78219美國')
        st.markdown('#### 觀眾席數：18418人')
    
    with col2:        
        image = Image.open('Home/ATT_Center.jpg')
        st.image(image)        
        image1 = Image.open('Home/ATT_Center_Tickets.jpg')
        st.image(image1)
