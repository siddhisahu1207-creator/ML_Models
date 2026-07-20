import streamlit as st
import pickle
model1=pickle.load(open("Room.pkl","rb"))
def deploy():
    st.title("House Prediction Model")
    area=st.number_input("Enter the value of area")
    bedroom=st.number_input("Enter the number of bedroom")
    age=st.number_input("Enter the  age")
    pred=st.button("Predict Price")
    if pred:
        predi=model1.predict([[area,bedroom,age]])
        st.write("Price of house is: ",predi[0])

deploy()