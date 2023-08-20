import streamlit as st
import pandas as pd
import numpy as np
import joblib

df6=pd.read_csv("Final_sheet.csv")
localities=np.sort(df6.Locality.unique())


lr_mod=joblib.load('house_price_prediction_model')



st.title("House Price Prediction")

First,second = st.columns(2)
with First:
    desired_area=st.number_input("Area",min_value=300.0,max_value=24300.0,step=50.0)

with second:
    desired_bhk=st.number_input("BHK",min_value=1.0,max_value=10.0,step=1.0)


with First:
    desired_bathroom=st.number_input("Bathroom",min_value=1.0,max_value=7.0,step=1.0)

with second:
    desired_parking=st.number_input("Parking",min_value=0.0,max_value=50.0,step=1.0)

desired_locality=st.selectbox("Locality",localities,index=0)

#print("Desired "+str(type(desired_locality)))

if(st.button("Submit")):

    model_input=[]
    model_input.append(desired_area)
    model_input.append(desired_bhk)
    model_input.append(desired_bathroom)
    model_input.append(desired_parking) 
    for i in range(41):
        if(i==desired_locality):
            model_input.append(1)
        else:
            model_input.append(0)
    result=str(lr_mod.predict([model_input])[0])
    st.balloons()
    st.write("Price = "+result)
    

