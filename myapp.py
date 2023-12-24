import streamlit as st
import pickle
import pandas as pd
import sys
sys.path.insert(1, "C:/past/your/coppied/path/here/streamlit_option_menu")
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Movie Recommender System', page_icon=':clapper:', layout='wide', initial_sidebar_state='auto')

st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name= option_menu(None, ['A Movie Recommendation System using NLP'],
icons = ['film'],  menu_icon = 'cast', orientation= 'horizontal',default_index = 0)

df = pd.read_csv('imdb_movies.csv')
# Recommend movies based on content
def recommend(movie):
    movie_index = df[df['names'] == movie].index[0]
    distances = spacy[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:22]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].names)

    return recommended_movies

def score_movie(movie):
    movie_index = df[df['names'] == movie].index[0]
    distances = spacy[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:22]
    score=[]
    for i in movies_list:
        score.append(df.iloc[i[0]].score)
    return score
def genre_movies(movie):
    movie_index = df[df['names'] == movie].index[0]
    distances = spacy[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:22]
    genre=[]
    for i in movies_list:
        score.append(df.iloc[i[0]].genre)
    return genre

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

spacy = pickle.load(open('spacy_preprocessing.pkl','rb'))
selected_movie_name = st.selectbox('Select a movie to recommend', df['names'].values)
movie_count = st.slider(label="The number of films", min_value=5, max_value=20)
if st.button('Recommend'):
    st.markdown("<h3 style='text-align: left; color: black;'>Recomended Film</h3>", unsafe_allow_html=True)
    recommendations = recommend(selected_movie_name)
    scores= score_movie(selected_movie_name)
    genres= genre_movies(selected_movie_name)
    for i in range(min(movie_count,len(recommendations))):
        col1,col2= st.columns(2)
        with col1:
            st.write(recommendations[i])
        with col2:
            st.write(f"score: **{scores[i]}**")
        with col3:
            st.write(f"genres: **{genres[i]}**") 
