import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
dat = pd.read_csv(r"C:\Users\zaina\Desktop\danish\movies1.csv")
data= pd.DataFrame(dat, columns = ['title','genre','duration','director', 'writer','actors']).head(200).astype(str)
n = []
for _ in range(0,data.shape[0]):
    n.append(_)
n=np.array(n)
np.transpose(n)
n=pd.DataFrame(n)
n.columns=['Movie_id']
data= pd.concat([n,data], axis =1)
data.set_index('Movie_id')


data.columns= ['Movie_id', 'title','genre','duration','director', 'writer','actors']
columns = data.columns

def get_important_features(data):
    important_features = []
    for i in range (0,data.shape[0]):
        important_features.append(data['title'][i]+' '+data['genre'][i]+' '+data['director'][i]+' '+data['actors'][i]+' '+data['writer'][i])
    return important_features
data['important_features'] = get_important_features(data)


cm = CountVectorizer().fit_transform(data['important_features'])
cs = cosine_similarity(cm)
print(data['title'], "\n")


title1 = input("Enter the Movie Title \n")

movie_id = data[data.title == title1]['Movie_id'].values[0]
print(movie_id)
scores = list(enumerate(cs[movie_id]))


sorted_scores = sorted(scores, key = lambda x:x[1],  reverse = True)
sorted_scores = sorted_scores[1:]

j = 0
print('The 5 most recommended courses to', title1, 'are :\n')
for _ in sorted_scores:
    movie_title = data[data.Movie_id== _[0]]['title'].values[0]
    print(j+1 , movie_title)
    j +=1
    if j>4:
        break