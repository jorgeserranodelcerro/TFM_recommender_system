__author__ = 'Jorge'

import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from recommender import Recommender

data = pd.read_csv('../Data/userprofile.csv', sep=',', encoding='utf-8')

smoker = sorted(data['smoker'].unique())
drink_level = sorted(data['drink_level'].unique())
dress_preference = sorted(data['dress_preference'].unique())
transport = sorted(data['transport'].unique())
budget = sorted(data['budget'].unique())

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def message():
    title = "Restaurant Recommender"
    
    user_smoker = request.form.get("smoker")
    user_drink = request.form.get("drink_level")
    user_dress = request.form.get("dress_preference")
    user_tran = request.form.get("transport")
    user_budget = request.form.get("budget")
    
    if user_smoker != None and user_drink != None and user_dress != None and user_tran != None and user_budget != None:
        # AQUI VA LA LOGICA PARA LLAMAR AL RECOMENDADOR
        r = Recommender(user_smoker, user_drink, user_dress, user_tran, user_budget)
        res = r.recommend().values.tolist()
    else:
        res = []

    return render_template("main.html", res=res, title=title, smoker=smoker, 
                           drink_level=drink_level, dress_preference=dress_preference, transport=transport, budget=budget,
                           user_smoker=user_smoker, user_drink=user_drink,
                           user_dress=user_dress, user_budget=user_budget, user_tran=user_tran)


if __name__ == '__main__':
    app.run(debug=True)
