from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():

    
@app.route('/page2')
def home():

def render_fact():
    country = get_country_options()
    country = request.args.get('country')
    year = year_most_dailycigarettes(country)
    fact = "In " + country + ", the year with the highest percentage of daily cigarettes consumed is " + year + "."
    return render_template('home.html', country_options=countries, funFact=fact)

def get_countries():
    """Return a list of countries from the demographic data."""
    with open('smoking.json') as smoking_data:
        year = json.load(smoking_data)
    #countries=[]
    #for d in year:
        #if d["Country"] not in countries:
            #countries.append(d["Country"])
    #a more concise but less flexible and less easy to read version is below.
    countries=list(set([d["Country"] for d in year])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    return countries
    
    def year_most_dailycigarettes(country):
    """Return the year in the given country with the highest daily cigarettes."""
    with open('smoking.json') as smoking_data:
        years = json.load(demographics_data)
    highest=0
    county = ""
    for c in years:
        if c["Country"] == country:
            if c["Age"]["Percent Under 18 Years"] > highest:
                highest = c["Age"]["Percent Under 18 Years"]
                county = c["County"]
    return county
    
@app.route('/page3')
def home():

app.run(debug=False) # change to False when running in production
