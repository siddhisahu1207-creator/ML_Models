import streamlit as st
import pickle
model1=pickle.load(open("Insurance.pkl","rb"))
def deploy():
    st.title("Insurance Buyer Prediction Model")
    age=st.number_input("Enter the age")
    pred=st.button("Predict")
    if pred:
        predi=model1.predict([[age]])
        if predi[0]==1:
           st.write("will buy the insurance ")
        else:
            st.write("will not buy the insurance")
deploy()