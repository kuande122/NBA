import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
def teams_legendplayer():
  legend_list={'Boston Celtics':{'Bill Russell','Larry Bird','Paul Pierce'},'Brooklyn Nets':{'Julius Erving','Jason Kidd','Derrick Coleman'}}
  option_legendplayer = st.sidebar.selectbox('選擇球員？',legend_list[option])
return option_legendplayer
option_legendplayer=teams_legendplayer()
