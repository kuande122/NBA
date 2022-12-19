import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import matplotlib.pyplot as plt #matplotlib(資料繪圖)
def analysis_chart(option_teams):
    data_list={"三分球命中率":"3P%","兩分球命中率":"2P%","罰球命中率":"FT%","投籃命中率":"FG%","進攻籃板":"ORB","防守籃板":"DRB",
               "總籃數數":"TRB","助攻":"AST","抄截":"STL","火鍋":"BLK","失誤":"TOV","犯規":"PF","得分":"PTS"}
    teams_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name=option_teams) 
    league_data=pd.read_excel("data/nbateamsdata.xlsx",sheet_name="League Average") 
    col1,col2=st.columns((4,6))
    with col1:
        option_data = st.selectbox('想查看數據？',data_list)
    with col2:
#-----折線圖---------------------------------------------------------------
        if option_data=='三分球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.三分球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.三分球命中率,'.-' )
             
        if option_data=='兩分球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.兩分球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.兩分球命中率,'.-' )        
            
        if option_data=='罰球命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.罰球命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.罰球命中率,'.-' )
                  
        if option_data=='投籃命中率':
            plt.style.use("ggplot")
            plt.plot(teams_data.年度,teams_data.投籃命中率 ,'.-' ) 
            plt.plot(league_data.年度,league_data.投籃命中率,'.-' )
  #-----長條圖---------------------------------------------------------------            
        if option_data=='進攻籃板':
           plt.bar(teams_data.年度,teams_data.進攻籃板)
           plt.bar(league_data.年度,league_data.進攻籃板)
            
        if option_data=='防守籃板': 
           plt.bar(teams_data.年度,teams_data.防守籃板)
           plt.bar(league_data.年度,league_data.防守籃板)   
     
        if option_data=='總籃板數': 
           plt.bar(teams_data.年度,teams_data.總籃板數)
           plt.bar(league_data.年度,league_data.總籃板數)   
       
        if option_data=='助攻': 
           plt.bar(teams_data.年度,teams_data.助攻)
           plt.bar(league_data.年度,league_data.助攻)  
        
        if option_data=='抄截': 
           plt.bar(teams_data.年度,teams_data.抄截)
           plt.bar(league_data.年度,league_data.抄截)  
            
        if option_data=='火鍋': 
           plt.bar(teams_data.年度,teams_data.火鍋)
           plt.bar(league_data.年度,league_data.火鍋)       
        
        if option_data=='失誤': 
           plt.bar(teams_data.年度,teams_data.失誤)
           plt.bar(league_data.年度,league_data.失誤)    
         
        if option_data=='犯規': 
           plt.bar(teams_data.年度,teams_data.犯規)
           plt.bar(league_data.年度,league_data.犯規)    
        
        if option_data=='得分':
           plt.bar(teams_data.年度,teams_data.得分)
           plt.bar(league_data.年度,league_data.得分)  

        plt.xlabel('Season',fontsize="10")
        plt.title(option_teams+" "+data_list[option_data]+" vs League Average")
        plt.legend(labels=[option_teams+" "+data_list[option_data],"League Average "+data_list[option_data]], loc = 'best')
        st.pyplot(plt)
           
