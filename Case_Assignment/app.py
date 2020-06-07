# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:48:04 2020

@author: clemi
"""
from flask import Flask, jsonify
import numpy as np
from sqlalchemy import create_engine
import pandas as pd
#%%
### Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

#%%
### Flask Setup
app = Flask(__name__)
#%%
# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    """Welcome to the home page with the list of available routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#%%
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    results = pd.read_sql('SELECT * FROM station', engine)

    results_json = results[['station','name']].to_json(orient='records') 

    return results_json

    
#Convert the query results to a dictionary using `date` as the key and `prcp` as the value
#Return the JSON representation of your dictionary.
            

#%%
if __name__ == '__main__':
    app.run(debug=True)
