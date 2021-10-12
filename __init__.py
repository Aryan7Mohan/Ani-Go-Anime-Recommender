from flask import Flask, render_template, redirect, url_for,request


app = Flask(__name__)

from pandas import *
import pickle
import numpy as np
import sklearn
import pandas as pd

data = read_csv(r'C:/Users/pmpal/Desktop/Project Anime/static/anime.csv',encoding= 'unicode_escape')
anime_names = data['name'].tolist()


anime_data=pd.read_csv(r'C:/Users/pmpal/Desktop/Project Anime/static/anime.csv',encoding= 'unicode_escape')








import joblib
		
with open('model_pickle','rb') as file:
	mp = pickle.load(file)
		
with open('tvf_pickle','rb') as file:
	tfv_mat = pickle.load(file)

#sig = joblib.load('sig_joblib')

#i hate this sigmoid_kernel shit
from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)


#getting the indices of anime title
indices = pd.Series(anime_data.index, index=anime_data['name']).drop_duplicates()

def give_rec(title, sig=sig):
	# Get the index corresponding to original_title

	idx = indices[title]

	# Get the pairwsie similarity scores 

	sig_scores = list(enumerate(sig[idx]))

	# Sort the movies

	sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

	# Scores of the 10 most similar movies

	sig_scores = sig_scores[1:21]

	# Movie indices
	anime_indices = [i[0] for i in sig_scores]

	# Top 10 most similar movies

	return pd.DataFrame({'Anime name': anime_data['name'].iloc[anime_indices].values,
		                                 'Rating': anime_data['rating'].iloc[anime_indices].values,'Genre': anime_data['genre'].iloc[anime_indices].values,'Type': anime_data['type'].iloc[anime_indices].values,'No. of Episodes': anime_data['episodes'].iloc[anime_indices].values})








@app.route('/')
def index():



	return render_template('index.html',anime_names=anime_names)


@app.route('/result', methods=['GET', 'POST'])
def result():





	if request.method=="POST":
		name = request.form.get("name",False)
		#print(name)
		df=give_rec(name)
		#print(df)


		return render_template('result.html',tables=[df.to_html(classes='data')], titles=df.columns.values)



if __name__ == "__main__":
    app.run(debug=True)