from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('home.html')

    
@app.route('/p1')
def page1():
    countrys = get_country_options()
    country = request.args.get('country')
    return render_template('page1.html', Country_options=countrys)

@app.route('/p2')
def page2():
    return render_template('page2.html')

@app.route('/countrys')
def render_smokers_selCountry():
    country = request.args.get('country')
    dailySmoker = get_Smokers(country)
    
    displayDailySmoker = "In " + country + ", the daily cigarettes smoked is " + str(dailySmoker) + "%"
    
    return render_template('page1.html', dailySmoker=displayDailySmoker)




def get_country_options():
    with open('smoking.json') as smoking_data:
        data = json.load(smoking_data)
    countries=[]
    for c in data:
        if c["Country"] not in countries:
            countries.append(c["Country"])
    options=""
    for c in countries:
        options += Markup("<option value=\"" + c + "\">" + c + "</option>")
    return options
    
def get_Smokers(country):
     with open('smoking.json') as smoking_data:
            data = json.load(smoking_data)
     countrySel = country
     dailySmoker = 0
     for d in data:
        if d["Country"] == countrySel:
            dailySmoker = d["Data"] ["Daily cigarettes"]
     return dailySmoker
if __name__=="__main__":
    app.run(debug=True)
