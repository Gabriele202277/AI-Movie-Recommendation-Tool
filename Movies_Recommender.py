# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:55:44 2025

@author: gabri
"""

import pandas as pd
import matplotlib.pyplot as plt



## Part 1: read csv files and visualization

# Read the movies_metadata file
movies_metadata = pd.read_csv('movies_metadata.csv')
# Read the ratings file
ratings = pd.read_csv('ratings.csv')

# Print the first 5 rows of each dataset
print(movies_metadata.head())
print(ratings.head())


# Count how many unique movies there are
unique_movies = movies_metadata['movie_id'].nunique()

# Count how many unique users have rated how many unique movies
unique_users = ratings['user_id'].nunique()
unique_rated_movies = ratings['movie_id'].nunique()

print(f"Number of unique movies: {unique_movies}")
print(f"Number of unique users: {unique_users}")
print(f"Number of unique rated movies: {unique_rated_movies}")



# Visualise the vote_average column
plt.figure(figsize=(10, 5))
plt.hist(movies_metadata['vote_average'].dropna(), bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Vote Average (movies_metadata.csv)', fontsize=16)
plt.xlabel('Vote Average', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.grid(True)
plt.show()

# Visualise the vote_count column
plt.figure(figsize=(10, 5))
plt.hist(movies_metadata['vote_count'].dropna(), bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Votes Count / movie (movies_metadata.csv)', fontsize=16)
plt.xlabel('Vote Count', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.grid(True)
plt.xlim(0, 8000)
plt.show()


# Visualise the distribution of the rating column
plt.figure(figsize=(10, 5))
plt.hist(ratings['rating'].dropna(), bins=10, edgecolor='k', alpha=0.7)
plt.title('Distribution of Ratings (ratings.csv)', fontsize=16)
plt.xlabel('Rating', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.grid(True)
plt.show()

# Visualise the ratings count

plt.figure(figsize=(10, 5))
plt.hist(ratings['movie_id'].value_counts(), bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Ratings Count / movie (ratings.csv)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.xlabel('Ratings count', fontsize=16)
plt.grid(True)
plt.xlim(0, 250)
plt.show()


