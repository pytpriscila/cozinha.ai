import pandas as pd
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

application = Flask(__name__)
application.debug = True

cooking_recommendation = pd.read_csv("/home/priscila/Documentos/hackathon-cotidiano/recipe_final.csv",
header=0,
usecols=['index','cuisine','id','rating','time', 'ingredient_amount', 'serving_number'])

print(cooking_recommendation)

cooking_recommendation.info()

#---------------------------------------------
# Funcao para recomendacao de receitas
#----------------------------------------------
# Input: qtd_pessoas, tempo, nivel_dificuldade
#----------------------------------------------
# qtd_pessoas: serving_number
# Receita: ingredient_amount
# nivel_dificuldade: rating
#---------------------------------------
# Output: Receitas
#---------------------------------------
# Receitas: ingredient_amount

def most_popular_receita_for_cliente(serving_number, time, rating, max_results=3):
    suggestions = cooking_recommendation.loc[(cooking_recommendation['serving_number']==serving_number) 
    & (cooking_recommendation['time']==time) & (cooking_recommendation['rating']==rating), :]
    print (cooking_recommendation[:max_results])


#most_popular_receita_for_cliente(4,600,5, max_results=3)

@recomendacao_receita_populares.route('/', methods=['GET', 'POST'])
def choose_plate():
    if request.method == 'POST':
        qtd_pessoas = request.form['qtd_pessoas']
        serving_number = request.form['serving_number']
        rating = request.form['rating']
        return redirect(url_for('most_popular_receita_for_cliente', serving_number=serving_number, time=time, rating=rating))
    else:
        return render_template('index.html')



#selecionando dados do dataset do usuario 0.
'''
user_0 =  dataset.loc[(dataset[1]==0), [1,3,4,5,6,7,8,9,12,13]]
    suggestions = [ (serving_number, time, rating)
                    for serving_number, time, rating in cooking_recommendation]
'''
"""return
def most_popular_receita_for_cliente(user_interests, max_results=3):
    suggestions = [ (interest, frequency)
                    for interest, frequency in popular_interests
                    if interest not in user_interests]
    return suggestions[:max_results]
"""