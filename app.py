# pip install -U streamlit
# pip install -U plotly

# you can run your app with: streamlit run app.py

import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Tweet Classification for Substance Use Detection')

message = st.text_input('Enter a Tweet')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])

    # print(prediction)
    # st.write(prediction)
    
    if prediction[0] == 'addict':
        st.warning('Tweeted by a drug addicted person')
    else:
        st.success('Tweeted by a normal person')


# st.balloons()