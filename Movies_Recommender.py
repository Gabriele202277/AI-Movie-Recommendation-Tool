# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:55:44 2025

@author: gabri
"""

import pandas as pd
import matplotlib.pyplot as plt

save_json = True

## Part 1: read csv files and visualization

# Read the movies_metadata file
movies_metadata = pd.read_csv('movies_metadata.csv')
# Read the ratings file
ratings = pd.read_csv('ratings.csv')

# Print the first 5 rows of each dataset
print(movies_metadata.head())
print(ratings.head())


if save_json: 
    movies_metadata.head().to_json("movies_metadata_head.json", orient="records", indent=4)
    ratings.head().to_json("ratings_head.json", orient="records", indent=4)