from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():

    
@app.route('/page2')
def home():

    
@app.route('/page3')
def home():

def get_states():
    """Return a list of state abbreviations from the demographic data."""
    with open('smoking.json') as smoking_data:
        counties = json.load(smoking_data)
    #states=[]
    #for c in counties:
        #if c["State"] not in states:
            #states.append(c["State"])
    #a more concise but less flexible and less easy to read version is below.
    states=list(set([c["State"] for c in counties])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    return states

app.run(debug=False) # change to False when running in production
