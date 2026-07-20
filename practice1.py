import streamlit as st
import pickle
model1=pickle.load(open("area.pkl","rb"))
def deploy():
    st.title("Area Price Prediction Model")
    area=st.number_input("Enter the value of area")
    pred=st.button("Predict Price")
    if pred:
        predi=model1.predict([[area]])
        st.write("Price of area is: ",predi[0])

deploy()