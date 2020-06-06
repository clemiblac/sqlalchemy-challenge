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
### Flask Setup

app = Flask(__name__)

#%%
# Flask Routes
#%%
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the home page with the list of available routes<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

if __name__ == '__main__':
    app.run(debug=True)
#%%
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#%%
@app.route("/api/v1.0/precipitation")
def precipitation():
        
    results = pd.read_sql('SELECT * FROM measurement', engine)

    results_json = results[['station','prcp']].to_json(orient='records') 

    return results_json

 #Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

 #Return the JSON representation of your dictionary.

#%%
if __name__ == '__main__':
    app.run(debug=True)