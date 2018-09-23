# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.mysql import MySQL
import constraint
import ast

from settings import APP_STATIC

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

application = Flask(__name__)
application.debug = True

@application.route('/show')
def show_recipes(serving_number, time, rating, max_results=3):
    suggestions = cooking_recommendation.loc[(cooking_recommendation['serving_number']==serving_number) 
    & (cooking_recommendation['time']==time) & (cooking_recommendation['rating']==rating), :]
    
    print (cooking_recommendation[:max_results])

    #return render_template('recipeRecommend.html', entries=entries, error=error)
"""
    try:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM recipe_info WHERE dbscan_label = %s;", [cur_flavor])
        fetch_result = cur.fetchall()
        entries = constraint.nutritional_constraints(fetch_result, cur_age, cur_weight, cur_height, cur_gender, 'Active')
        print entries
        conn.close()
        error = None
        return render_template('content.html', entries=entries, error=error)
    except Exception as e:
        print str(e)
        entries = None
        error = 'Database Connection Error!'
        return render_template('content.html', entries=entries, error=error)
"""


@application.route('/', methods=['GET', 'POST'])
def choose_flavor():
    if request.method == 'POST':
        qtd_pessoas = request.form['qtd_pessoas']
        serving_number = request.form['serving_number']
        rating = request.form['rating']
        #return redirect(url_for('most_popular_receita_for_cliente', serving_number=serving_number, time=time, rating=rating))
        return redirect(url_for('show_recipes', serving_number=serving_number, time=time, rating=rating))

    else:
        return render_template('index.html')


application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host = "127.0.0.1", port = 9090)