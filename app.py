import streamlit as st
import pandas as pd
import joblib
import numpy as np
import time
import pandas as pd

df = pd.read_csv('day.csv')

st.title('Shared Bikes Demand Prediction')

filename = 'finalized_model.sav'
model = joblib.load(filename)

#st.write(str(model))
                            
season = st.selectbox('Season (1:spring, 2:summer, 3:fall, 4:winter)',["1","2","3","4"])

yr = st.selectbox('Year (0: 2018, 1:2019)',["0","1"])

mnth = st.text_input(label=' month (1 to 12)',value=1)

weekday = st.selectbox('Day of the week',["0","1","2","3","4","5","6"])

weathersit = st.selectbox('weathersit',["1","2","3"])

temp = st.text_input(label='Temperature in Celsius',value=0)

atemp = st.text_input(label='Feeling temperature in Celsius',value=0)

hum = st.text_input(label='Humidity',value=0)

windspeed = st.text_input(label='Wind speed',value=0)

casual = st.text_input(label='Count of casual users',value=0)

registered =st.text_input(label='Count of registered users',value=0)


pred = model.predict([[int(season),int(yr),int(mnth),int(weekday),int(weathersit),int(temp),int(atemp),int(hum),int(windspeed),int(casual),int(registered)]])

shu = int(pred)
if st.button('Submit'): 
   st.header('Count of total rental bikes including both casual and registered {}'.format(int(shu)))

    
         
