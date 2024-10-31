import streamlit as st

# Title of the app
st.title("Statsanity: An NBA LSTM model")

# Text input
player_input = st.text_input("Enter a player:")

opponent_input = st.text_input("Enter an opponent:")

# Button to submit input
if st.button("Submit"):
    pass