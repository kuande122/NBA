import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import matplotlib.pyplot as plt #matplotlib(資料繪圖)

#def analysis_chart():
    data_list={"三分球命中率":"3P%","兩分球命中率":"2P%","罰球命中率":"FT%","投籃命中率":"FG%","進攻籃板":'ORB',"防守籃板":"DRB",
               "總籃板":"TRB","助攻":"AST","抄截":"STL","火鍋":"BLK","失誤":"TOV","犯規":"PF","得分":"PTS"}
    option_data = st.selectbox('想查看數據？',data_list)
#teams_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=option) 
#area_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=area_list[option_area]) 
#league_data=pd.read_excel("nbateamsdata.xlsx",sheet_name='League Average') 
#if option1=='三分球命中率':
  #col1,col2=st.columns(2)
  #with col1:
  #st.dataframe(area_data)         
  #with col2:
   #plt.style.use("ggplot")
   #plt.plot(teams_data.年度,teams_data.三分球命中率 ,'.-' ) 
   #plt.plot(league_data.年度,league_data.三分球命中率,'.-' )
   #plt.xlabel('Season',fontsize="10")
   #plt.title(option+data_list[option1]+'vs League AVG')
   #st.pyplot(plt) 
