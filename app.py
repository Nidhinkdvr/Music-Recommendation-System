import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model and dataset
model = joblib.load("music_model.pkl")  # Make sure your trained model is saved as music_model.pkl
songs_df = pd.read_csv("songs_dataset.csv")  # Dataset with song details

# Load custom CSS
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML template
def load_html():
    with open("index.html", "r") as f:
        return f.read()

# Function to recommend songs based on user preference
def recommend_songs(user_input):
    # Dummy recommendation logic (Replace this with your ML model's logic)
    recommendations = songs_df.sample(5)  # Selecting 5 random songs (Replace with model predictions)
    return recommendations

# Streamlit UI
def main():
    st.set_page_config(page_title="Music Recommendation", layout="centered")
    load_css()

    st.markdown(load_html(), unsafe_allow_html=True)

    # User Input
    genre = st.selectbox("Select Genre", songs_df["genre"].unique())
    mood = st.selectbox("Select Mood", ["Happy", "Sad", "Relaxing", "Energetic"])
    artist = st.text_input("Enter Favorite Artist (Optional)", "")

    if st.button("Recommend Songs 🎵"):
        recommendations = recommend_songs([genre, mood, artist])

        st.subheader("Recommended Songs:")
        for index, row in recommendations.iterrows():
            st.write(f"🎶 {row['song_name']} - {row['artist']}")

if __name__ == "__main__":
    main()
