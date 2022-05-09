import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv(r"C:\Users\zaina\Desktop\danish\coursea_data.csv")
data.set_index('course_title')
# Display first 5 rows of newly added csv file
data.columns= ['course_id', 'course_title', 'course_organization', 'course_Certificate_type', 'course_rating', 'course_difficulty', 'course_students_enrolled']
columns = data.columns


def get_important_features(data):
    important_features = []
    for i in range (0,data.shape[0]):
        important_features.append(data['course_title'][i]+ ' '+data['course_Certificate_type'][i]+' '+data['course_organization'][i]+' '+data['course_difficulty'][i])
    return important_features
data['important_features'] = get_important_features(data)


cm = CountVectorizer().fit_transform(data['important_features'])
cs = cosine_similarity(cm)
print(data['course_title'])


title = input("Enter the similar Course Title \n")

course_id = data[data.course_title == title]['course_id'].values[0]
scores = list(enumerate(cs[course_id]))

sorted_scores = sorted(scores, key = lambda x:x[1],  reverse = True)
sorted_scores = sorted_scores[1:]

j = 0
print('The 5 most recommended courses to', title, 'are :\n')
for _ in sorted_scores:
    course_title = data[data.course_id== _[0]]['course_title'].values[0]
    print(j+1 , course_title)
    j +=1
    if j>4:
        break