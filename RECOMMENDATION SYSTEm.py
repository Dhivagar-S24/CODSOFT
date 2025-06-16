import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'title': ['The Matrix', 'John Wick', 'Avengers', 'Interstellar', 'Inception'],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'An ex-hitman comes out of retirement to track down the gangsters that took everything from him.',
        'Earth’s mightiest heroes must come together to stop a global threat.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'A thief who steals corporate secrets through dream-sharing is given a chance to erase his criminal record.'
    ]
}

df = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(title):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # top 3 recommendations
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

print("Recommendations for 'Inception':")
print(recommend('Inception'))