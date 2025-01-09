import streamlit as st
import pandas as pd
import os

# Get the path to the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the image in the imgs folder
obs_processed = os.path.join(current_dir, "notebooks", "csv", "observations_processed.csv")
obs_responses = os.path.join(current_dir, "notebooks", "csv", "observations_responses.csv")

@st.cache_data
def load_data():
    observations = pd.read_csv(obs_processed)
    responses = pd.read_csv(obs_responses, sep="#")
    return observations, responses

def warning():
    st.warning("""The purpose of this application is to test LLM-generated interpretations of medical observations. 
           The explanations are generated fully automatically by a large language model. 
           This application should be used for testing purposes only. 
           It does not provide support for real world cases and does not replace advice from medical professionals.""")