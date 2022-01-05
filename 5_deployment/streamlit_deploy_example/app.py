import pandas as pd
import pickle
import os
import streamlit as st

from model import predict

def run():
    # Streamlit page title
    st.title("Movie Review Classifier")
    st.markdown('**This is a demo application for classifying movie reviews as positive or negative**')
    hide_footer_style = """<style>.reportview-container .main footer {visibility: hidden;}"""
    st.markdown(hide_footer_style, unsafe_allow_html=True)

    # Load model and vectorizer
    model = pickle.load(open('./models/model.pkl','rb'))
    vect = pickle.load(open('./models/vect.pkl','rb'))

    # Clear input form
    def clearform():
        st.session_state['newreview'] = ''

    # Input form
    with st.form('reviewform'):
        new_review = st.text_area(label='Write or paste movie review text below',
                                    value = '',
                                    key='newreview')
        b1,b2 = st.columns([1,1])
        with b1:
            submit = st.form_submit_button(label='Submit')
        with b2:
            clear = st.form_submit_button(label='Reset', on_click=clearform)

    if submit and new_review !='':
        # Generate prediction
        y, proba = predict(new_review, model, vect)

        # Display the prediction
        st.markdown('### Predicted sentiment: {}'.format(y))
        st.markdown('Probability: {}'.format(proba))



if __name__ == "__main__":
    run()
