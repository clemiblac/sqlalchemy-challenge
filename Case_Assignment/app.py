# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:48:04 2020

@author: clemi
"""

import numpy as np

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

from flask import Flask, jsonify

#%%

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///titanic.sqlite")

#%%

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#%%
#################################################
# Flask Routes
#################################################
#%%
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

#%%
@app.route("/api/v1.0/names")
def names():
    
    results = pd.read_sql('SELECT * FROM passenger', engine)

    results_json = results[['name','age']].to_json(orient='records') 

    return results_json


#%%
@app.route('/api/v1.0/passengers-sql')
def passengers_sql():

    results = pd.read_sql('SELECT * FROM passenger', engine)

    results_json = results.to_json(orient='records') 

    return results_json

#%%
if __name__ == '__main__':
    app.run(debug=True)