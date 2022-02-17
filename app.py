from flask import Flask, render_template, redirect, url_for,request


app = Flask(__name__)

from pandas import *
import pickle
import numpy as np
import sklearn
import pandas as pd
from get_rec import *


data = read_csv(r'C:/Users/pmpal/Desktop/Project Anime/static/anime.csv',encoding= 'unicode_escape')
anime_names = data['name'].tolist()


anime_data=data



@app.route('/')
def index():



	return render_template('index.html',anime_names=anime_names[:10])


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