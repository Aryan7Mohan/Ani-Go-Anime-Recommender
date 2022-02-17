
from pandas import *
import numpy as np
import sklearn
import pandas as pd


data = read_csv(r'C:/Users/pmpal/Desktop/Project Anime/static/anime.csv',encoding= 'unicode_escape')
anime_names = data['name'].tolist()


anime_data=data



#importing model
import joblib
sig = joblib.load('sig_new_model.pkl')


#getting the indices of anime title
indices = pd.Series(anime_data.index, index=anime_data['name']).drop_duplicates()


def give_rec(title, sig=sig):
	# Get the index corresponding to original_title

	idx = indices[title]

	# Get the pairwsie similarity scores 

	sig_scores = list(enumerate(sig[idx]))

	# Sort the anime

	sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

	# Scores of the 10 most similar anime

	sig_scores = sig_scores[1:21]

	# anime indices
	anime_indices = [i[0] for i in sig_scores]

	# Top 10 most similar anime

	return pd.DataFrame({'Anime name': anime_data['name'].iloc[anime_indices].values,
		                                 'Rating': anime_data['rating'].iloc[anime_indices].values,'Genre': anime_data['genre'].iloc[anime_indices].values,'Type': anime_data['type'].iloc[anime_indices].values,'No. of Episodes': anime_data['episodes'].iloc[anime_indices].values})



