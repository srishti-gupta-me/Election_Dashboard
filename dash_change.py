import streamlit as st
import pandas as pd
import numpy as np
from plotly.tools import FigureFactory as ff
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
import streamlit.components.v1 as components
import base64

favicon_image = Image.open('ashoka.jpeg')
st.set_page_config(page_title="Previous Election Insights", page_icon=favicon_image, layout="wide")



#To hide hamburger menu

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)




#Landing Page 
components.html("""<html>
<style>

body {
  height: 800px;  
  background-color: white;
} 

#title
{ text-align: center;
font-family: Arial;
font-size: 3vw;
padding: 0px;
margin-top:0vh;
margin-left:20vw;
position: absolute;
}

#sub-heading
{ text-align: center;
font-family: Arial;
font-size: 1.8vw;
padding: 0px;
margin-top:30vh;
margin-left:50vw;
position: absolute;
}

#logo
{
  margin-top:0vh;
  margin-left:85vw;
  margin-right:auto;
  position: absolute;
}


</style>
<html>
<body>

<main>
<h1 id="title">Assembly Elections 2022<h1>
<p id="sub-heading"><i>Metrics from the past</i><p>

<img id="logo" src="https://github.com/srishti-gupta-me/Election_Dashboard/blob/main/logo.png?raw=true"/>
  
</main>
</body>
</html>
""", height=150)

landing_con=st.container()

landing_con_1, landing_con_2, landing_con_3, landing_con_4=landing_con.columns([0.5,1.5,1.5,0.5])

bg=Image.open(r'./initial_bg.png')

with landing_con_2:
    st.image(bg, use_column_width='always')  

original_title = '<p style="font-family:Arial; font-size: 1vw; margin-top: 15vh;">Click on any of the buttons below to see what the numbers looked like in the last round of elections for the poll bound states of Punjab, Uttarakhand, Uttar Pradesh, Manipur and Goa.</p>'

landing_con_3.markdown(original_title, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")



st.markdown("""<hr/>""", unsafe_allow_html=True)



@st.cache
def bar_chart(df,x_var,y_var, title="", x_axis_title="",y_axis_title=""):
    fig = px.bar(
        df,
        x=x_var,
        y=y_var,
        title=title
    )

    fig.update_layout(
        autosize=False,
        height=500,
        title={
        'text': title,
        'y':0.9,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top'}
    )

    fig.update_xaxes(
        title=x_axis_title,
    )

    fig.update_yaxes(
        title=y_axis_title,
        showgrid=False,
    )


    return fig.update_traces(
        hoverinfo="text",
        insidetextfont=dict(
            color="white"
        ),
    )

#NOTA
st.markdown("<div id='linkto_nota'>sa</div>", unsafe_allow_html=True)   
 
nota_container=st.container()
nota_1,nota_2, nota_3=nota_container.columns([3,1,3])

read_and_cache_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
data = read_and_cache_csv('./nota.csv', nrows=100000)

nota_1.plotly_chart(bar_chart(data.astype(str), data.State,data.Nota_Percentage,"Nota Vote","State","Percentage"), use_container_width=True)

nota_3.image('./geo.png')

st.markdown("""<hr/>""", unsafe_allow_html=True)

#Parties

st.markdown("<div id='linkto_party'>pa</div>", unsafe_allow_html=True)   
 
party_container=st.container()
party_1,party_2, party_3=party_container.columns([3,1,3])

read_and_cache_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
data = read_and_cache_csv('./nota.csv', nrows=100000)

party_1.plotly_chart(bar_chart(data.astype(str), data.State,data.Nota_Percentage,"Contesting Parties","State","Percentage"), use_container_width=True)

party_3.image('./geo.png')

st.markdown("""<hr/>""", unsafe_allow_html=True)


#Voter Turnout

st.markdown("<div id='linkto_turnout'></div>", unsafe_allow_html=True)   
 
turnout_container=st.container()
turnout_1,turnout_2, turnout_3=turnout_container.columns([3,1,3])

read_and_cache_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
data = read_and_cache_csv('./nota.csv', nrows=100000)

turnout_1.plotly_chart(bar_chart(data.astype(str), data.State,data.Nota_Percentage,"Turnout","State","Percentage"), use_container_width=True)

turnout_3.image('./geo.png')

st.markdown("""<hr/>""", unsafe_allow_html=True)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 255, 0);
}
</style>""", unsafe_allow_html=True)


st.button('x')



