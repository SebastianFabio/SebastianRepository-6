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
    countrys = get_country_options()
    years=get_year_options()
    country = request.args.get('country')
    return render_template('page2.html', Country_options=countrys, year_options=years)    
    
@app.route('/izzie')
def render_sebashasasinglesister():
   
    countrys = get_country_options()
    years=get_year_options()
    country = request.args.get('fabio')
    year1=request.args.get('julianna')
    juliannaizzie=get_smokers(country, year1)
    hotider="The Total Amount Of Smokers In " + country + " In " + str(year1) + " was "+ str(juliannaizzie)
    return render_template('page2.html', Country_options=countrys, year_options=years, izziefab=hotider)    
@app.route('/countrys')
def render_smokers_selCountry():
    country = request.args.get('country')
    dailySmoker = get_Smokers(country)
    countrys = get_country_options()

    displayDailySmoker = "In " + country + ", the daily cigarettes smoked is " + str(dailySmoker)
    
    return render_template('page1.html', dailySmoker=displayDailySmoker, Country_options=countrys)
def get_smokers(country, year):
    with open('smoking.json') as smoking_data:
        data = json.load(smoking_data)
    smokersinc=0
    for c in data:
        if c["Country"] == country and str(c["Year"]) == year:
            smokersinc=c["Data"]["Smokers"]["Total"]
    return smokersinc
            

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
def get_year_options():
    with open('smoking.json') as smoking_data:
        data = json.load(smoking_data)
    countries=[]
    for c in data:
        if str(c["Year"]) not in countries:
            countries.append (str(c["Year"]))
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
