# all the imports
import pandas as pd
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
#from flaskext.mysql import MySQL
import constraint
import ast

from settings import APP_STATIC

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

application = Flask(__name__)
application.debug = True

cooking_recommendation = pd.read_csv("/home/priscila/Documentos/hackathon-cotidiano/recipe_final.csv",
header=0,
usecols=['index','cuisine','id','rating', 'name', 'time', 'big_image', 'ingredient_amount', 'serving_number'])


@application.route('/show')
def show_recipes():
    max_results=3
    serving_number  = request.args.get('serving_number')
    time = request.args.get('time')
    rating = request.args.get('rating')
    suggestions = cooking_recommendation.loc[(cooking_recommendation['serving_number']==int(serving_number)) 
    & (cooking_recommendation['time']==int(time)) & (cooking_recommendation['rating']==int(rating)), :]
    entries = (cooking_recommendation[:max_results])
    error = None
    print(entries)
    print('aaaahahaha')
    
    #print(entries.info())
   
    
    return render_template('recipeRecommend.html', entries=entries, error=error)

@application.route('/', methods=['GET', 'POST'])
def choose_flavor():
    if request.method == 'POST':
        #qtd_pessoas = request.form['qtd_pessoas']
        serving_number = request.form['qtd_pessoas']
        time = request.form['tempo']
        rating = request.form['activity']
        #return redirect(url_for('most_popular_receita_for_cliente', serving_number=serving_number, time=time, rating=rating))
        return redirect(url_for('show_recipes', serving_number=serving_number, time=time, rating=rating))

    else:
        return render_template('index.html')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host = "127.0.0.1", port = 9090)