import streamlit as st
#from streamlit_option_menu import option_menu
import pickle

#load model
model = pickle.load(open('D:/mldeploy/streamlit/mental_disorder_model.sav', 'rb'))


#sidebar for nav_bar
# with st.sidebar:
#     selected = option_menu('Mental Disorder Symptoms Prediction',['Symtoms Mental Disorder Prediction','Mental Disorder Predictions'], default_index=0)

#Disorder Predictions Pages
# if (selected == "Symtoms Mental Disorder Prediction"):
st.title('Mental Disorder Prediction')

# getting the input data from the user
Yes = 1
No = 0

col1, col2 = st.columns(2)

with col1:
    #Pregnancies = st.text_input('Nervous (please answer Ya: 1 or No: 0)')
    nervous = st.selectbox(
    'Are you feeling nervous?',
    (Yes, No))
    st.write(nervous)
with col2:
    panic = st.selectbox(
    'Are you feeling panic?',
    (Yes, No))
    st.write(panic)

with col1:
    breat_rap = st.selectbox(
    'Are you feeling breating rapidly?',
    (Yes, No))
    st.write(breat_rap)

with col2:
    sweating = st.selectbox(
    'Are you feeling sweating?',
    (Yes, No))
    st.write(sweating)

with col1:
    trouble_cons = st.selectbox(
    'Are you feeling trouble in concentration?',
    (Yes, No))
    st.write(trouble_cons)

with col2:
    sleep = st.selectbox(
    'Are you having trouble in sleeping?',
    (Yes, No))
    st.write(sleep)

with col1:
    work = st.selectbox(
    'Are you having trouble in work?',
    (Yes, No))
    st.write(work)
with col2:
    hope = st.selectbox(
    'Are you feeling hopelessness?',
    (Yes, No))
    st.write(hope)
with col1:
    angry = st.selectbox(
    'Are you often feel angry?',
    (Yes, No))
    st.write(angry)

with col2:
    over_react = st.selectbox(
    'Are you having over react with something?',
    (Yes, No))
    st.write(over_react)
with col1:
    eat = st.selectbox(
    'Are you having change in eating?',
    (Yes, No))
    st.write(eat)
with col2:
    suicidal = st.selectbox(
    'Are you have feel suicidal thought?',
    (Yes, No))
    st.write(suicidal)

with col1:
    tired = st.selectbox(
    'Are you feel tired now?',
    (Yes, No))
    st.write(tired)
with col2:
    cf = st.selectbox(
    'Are you have a close friend?',
    (Yes, No))
    st.write(cf)
with col1:
    socmed = st.selectbox(
    'Are you having social media addiction?',
    (Yes, No))
    st.write(socmed)

with col2:
    weight = st.selectbox(
    'Your weight increase?',
    (Yes, No))
    st.write(weight)
with col1:
    material_poss = st.selectbox(
    'Do you feel material possessions?',
    (Yes, No))
    st.write(material_poss)
with col2:
    introvert = st.selectbox(
    'Are you feeling introvert?',
    (Yes, No))
    st.write(introvert)

with col1:
    memory = st.selectbox(
    'Do you feel popping up stressful memory?',
    (Yes, No))
    st.write(memory)
with col2:
    nightmares = st.selectbox(
    'Do you having nightmares?',
    (Yes, No))
    st.write(nightmares)
with col1:
    avoid = st.selectbox(
    'Are you Avoid Peapole or activitise?',
    (Yes, No))
    st.write(avoid)

with col2:
    feel_negative = st.selectbox(
    'Do you feel negatively?',
    (Yes, No))
    st.write(feel_negative)
with col1:
    trouble_conss = st.selectbox(
    'Do you feel trouble consentrations?',
    (Yes, No))
    st.write(trouble_conss)
with col2:
    blaming = st.selectbox(
    'Are you blaming yourself?',
    (Yes, No))
    st.write(blaming)
# code for Prediction
diagnosis = ''

# creating a button for Prediction

if st.button('Disorder Prediction Result'):
    prediction = model.predict([[nervous, panic, breat_rap, sweating, trouble_cons, sleep, work, hope, angry, over_react, eat, suicidal, tired, cf, socmed, weight, material_poss, introvert, memory, nightmares, avoid, feel_negative, trouble_conss, blaming]])
    
    if (prediction[0] ==0):
        diagnosis ='The person is Anxiety'
    elif(prediction[0]==1):
        diagnosis ='The person is Depression'
    elif(prediction[0]==2):
        diagnosis ='The Person is Loneliness'
    elif(prediction[0]==3):
        diagnosis ='The Person is Normal'
    elif(prediction[0]==4):
        diagnosis ='The Person is Stress'
        st.text('This is some text.')
    
st.success(diagnosis)


# if (selected == "Mental Disorder Predictions"):
#     st.title('404 Under Maintains')