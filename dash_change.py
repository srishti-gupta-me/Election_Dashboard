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
import geopandas as gpd


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
  width:5vw;
  height: auto;
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

original_title = '<p style="font-family:Arial; font-size: 1vw; margin-top: 15vh;">Click on any of the links below to see what the numbers looked like in the last round of elections for the poll bound states of Punjab, Uttarakhand, Uttar Pradesh, Manipur and Goa.</p>'

landing_con_3.markdown(original_title, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")


linkers=""" <style>  
  a {
   justify-content: center;
  align-items: center;
  }
  
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  margin-left:0vw;
  margin-right:0vw;
  margin-top:5vh;
  position: relative;
  text-align: center;
  grid-gap: 2vh 1vw;
}

.grid-item {
  background-color: rgba(255, 255, 255, 1);
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 1vw;
   
}

.button-css {

  padding: 0px 10px;
  background-color: rgba(255, 218, 88, 1);;
  color: #000;
  height:8vh;
  width:8vw;
  border-radius: 10px;
  text-align: center;
  
}</style>

<div class="grid-container">
 <div class="grid-item"><a href=#linkto_nota><button class="button-css">NOTA</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Contesting Parties</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Voter Turnout</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Female Voter Turnout</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Male Voter Turnout</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Constituencies</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Women Winners</button></a></div>
 <div class="grid-item"><a href=#linkto_party><button class="button-css">Newcomers</button></a></div>
</div>


"""
landing_con_3.markdown(linkers, unsafe_allow_html=True)



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
        
        margin=dict(l=0, r=20, t=100, b=0),
        autosize=False,
        width=200,
        height=500,
        title={
        'text': title,
        'y':0.9,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'bottom'}
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
st.markdown("<div id='linkto_nota'></div>", unsafe_allow_html=True)   
 
# nota_container=st.container()
# nota_container.subheader('NOTA Percentage')
# nota_1,nota_2, nota_3=nota_container.columns([2,0.5,2.5])



# nota_2.markdown("""
# <style>
# .vl {
#   border-left: 0.1vw solid grey;
#   margin-left: 3vw;
#   height:80vh;
# }
# </style>
# <div class="vl"></div>
# """, unsafe_allow_html=True)



# read_and_cache_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
# data = read_and_cache_csv('./nota.csv', nrows=100000)

# nota_1.plotly_chart(bar_chart(data.astype(str), data['State'],data['Value'],"","State","Percentage"), use_container_width=True)

# #nota_3.image('./geo.png')

# st.markdown("""<hr/>""", unsafe_allow_html=True)

# #Parties

# st.markdown("<div id='linkto_party'></div>", unsafe_allow_html=True)   
 
# party_container=st.container()
# party_container.subheader('Contesting Parties')

# party_1,party_2, party_3=party_container.columns([2,0.5,2.5])

# read_and_cache_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
# data = read_and_cache_csv('./nota.csv', nrows=100000)

# party_1.plotly_chart(bar_chart(data.astype(str), data.State,data.Value,"","State","Percentage"), use_container_width=True)


# st.markdown("""<hr/>""", unsafe_allow_html=True)



# party_2.markdown("""
# <style>
# .vl {
#   border-left: 0.1vw solid grey;
#   margin-left: 3vw;
#   height:80vh;
# }
# </style>
# <div class="vl"></div>
# """, unsafe_allow_html=True)


# def map_plot(file_link, container_name, color):
#     map_df = gpd.read_file("./maps-master/States/Admin2.shp")
#     map_value= pd.read_csv(file_link)
#     merged = map_df.merge(map_value, how='left', left_on="ST_NM",right_on="State")
#     merged.drop(['State'], axis=1, inplace=True)
#     merged['Value']=merged['Value'].mask(merged['Value'].isnull()==True,-1)

#     # set the value column that will be visualised
#     variable = 'Value'
#     # set the range for the choropleth values
#     vmin, vmax = 0, 100

#     # create figure and axes for Matplotlib
#     fig, ax = plt.subplots(1, figsize=(30, 10))
#     # remove the axis
#     ax.axis('off')


#     # Create colorbar legend
#     sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=vmin, vmax=vmax))
#     # empty array for the data range
#     sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
#     # add the colorbar to the figure
#     # fig.colorbar(sm)

#     # create map
#     merged.plot(column=variable, cmap=color, linewidth=0.8, ax=ax, edgecolor='0.8')

#     # Add Labels
#     merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
#     merged['coords'] = [coords[0] for coords in merged['coords']]

#     states=['Manipur','Punjab','Uttarakhand','Goa','Uttar Pradesh']

#     for idx, row in merged.iterrows():

#         if row['ST_NM'] in states:
#             plt.annotate(text=row['Value'], xy=row['coords'],horizontalalignment='center')

#     container_name.pyplot(fig)
    
# map_plot("nota.csv",nota_3,"Blues")
# map_plot("party.csv",party_3,"Oranges")


assembly_container=st.container()
assembly_container.subheader('General Elections with Assembly Numbers')

ass_1,ass_2=assembly_container.columns([1,1])
ass_csv = st.cache(suppress_st_warning=True)(pd.read_csv)
ass_data = ass_csv('./Assembly_Chart.csv', nrows=100000)


fig = px.sunburst(ass_data, path=['State_Name','Assembly_No','Year'], values='Count',width=600, height=600)

ass_1.plotly_chart(fig, use_container_width=True)

