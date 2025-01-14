import streamlit as st
import pickle
import requests
import ssl


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6220c9da09e22d23ad7749499d4e22ec&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommend_movies=[]
    recommend_movies_poster = []
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
           #fetch poster
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster

movies = movies_list
movies_list = movies_list['title'].values

st.title('MOVIE RECOMMENDOR SYSTEM')
selected_movie_name = st.selectbox('Select a movie', movies_list)

if st.button('Recommend'):
    st.snow()
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])
    # Add bottom chart