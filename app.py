import streamlit as st
import pandas as pd
import pickle
with open('pipeline.pkl','rb') as f:
  model=pickle.load(f)

df=pd.read_csv('depressed.csv')
st.title('Depression Status')
gender=st.selectbox('Select Gender: ',df['Gender'].unique().tolist())
age=st.number_input('Select your Age: ',1,60,18,1)
city=st.selectbox('Select Your City : ',df['City'].unique().tolist())
academic=st.slider('Select Your Academic Pressure : ',0,5)
workpressure=st.selectbox('Select Your Work Pressure : ',df['Work Pressure'].unique().tolist())
cgpa=st.number_input('Select your CGPA : ',0.0,10.0)
study=st.slider('Select Your Study Satisfaction : ',0,5)
job=st.slider('Select Your Job Satisfaction : ',0,4)
sleep=st.selectbox('Select Your Sleep Duration : ',df['Sleep Duration'].unique().tolist())
habits=st.selectbox('Select Your Dietary Habits : ',df['Dietary Habits'].unique().tolist())
Degree=st.selectbox('Select Your Degree : ',df['Degree'].unique().tolist())
thought=st.selectbox('Select Your suicidal thoughts ? : ',df['Have you ever had suicidal thoughts ?'].unique().tolist())
hours=st.slider('Select Your Work/Study Hours : ',0,11)
stress=st.slider('Select Your Financial Stress : ',1,5)
mental_illness=st.selectbox('Select Your Family History of Mental Illness : ',df['Family History of Mental Illness'].unique().tolist())

def predict(g,a,c,ap,wp,cgpa,ss,js,sd,dh,d,h,wsh,fs,fh):
  input={
      'Gender':[g],
      'Age':[a],
      'City':[c],
      'Academic Pressure':[ap],
      'Work Pressure':[wp],
      'CGPA':[cgpa],
       'Study Satisfaction':[ss],
        'Job Satisfaction':[js],
        'Sleep Duration':[sd],
       'Dietary Habits':[dh],
        'Degree':[d],
        'Have you ever had suicidal thoughts ?':[h],
       'Work/Study Hours':[wsh],
        'Financial Stress':[fs],
       'Family History of Mental Illness':[fh]
  }
  df=pd.DataFrame(input)
  response=model.predict(df)[0]
  if response==0:
    return "The Person is not suffering from depression"
  else:
    return "The Person is suffering from depression"

if st.button('Depression Status'):
  decision=predict(gender,age,city,academic,workpressure,cgpa,study,job,sleep,habits,Degree,thought,hours,stress,mental_illness)
  container=st.container(border=True)
  container.info(decision)
