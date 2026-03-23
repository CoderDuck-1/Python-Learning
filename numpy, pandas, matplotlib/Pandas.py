import csv
import pandas as pd

def calculate_rating_stats(data, industry=None):
    ratings = []
    for row in data:
        if row[3]!='NULL' and (not industry or row[1]==industry):
            ratings.append(float(row[3]))
    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = sum(ratings) / len(ratings)
    return max_rating, min_rating, avg_rating

with open('C:/Users/Lakshya/Desktop/Python Projects/Python-Learning/numpy, pandas, matplotlib/Assets/1_intro/movies.csv') as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]

    max_rating, min_rating, avg_rating = calculate_rating_stats(data)
    print(f"All records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

    max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
    print(f"Bollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

    max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
    print(f"Hollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

#Using Pandas
# A pandas DataFrame is a two-dimensional, size-mutable tabular data structure with labeled axes (rows and columns) in Python

df = pd.read_csv('C:/Users/Lakshya/Desktop/Python Projects/Python-Learning/numpy, pandas, matplotlib/Assets/1_intro/movies.csv')
print(df.head())
print(df.tail())
print(df.sample())
print(df[2:6])
print(df["imdb_rating"]) #same as df.imdb_rating
print(df.shape)
print(df.industry.unique())
print(df.industry.value_counts())
print(type(df))
print(dir(df.imdb_rating))

df_b = df[df.industry=="Bollywood"]
df_h = df[df.industry=="Hollywood"]
print(df_b.imdb_rating.min(), df_b.imdb_rating.max(), df_b.imdb_rating.mean())
print(df_h.imdb_rating.min(), df_h.imdb_rating.max(), df_h.imdb_rating.mean())




