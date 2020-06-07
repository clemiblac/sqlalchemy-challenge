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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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
### PRECIPITATION APP
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Convert the query results to a dictionary using `date` as the key and `prcp` as the value
    results = pd.read_sql("SELECT * FROM Measurement", engine)
    
    
    #Return the JSON representation of your dictionary.
    results_json = results[['date','prcp']].to_json(orient='records') 

    return results_json
#%%
### STATIONS APP
@app.route("/api/v1.0/stations")
def stations():
    #Return a JSON list of stations from the dataset.
    results = pd.read_sql("SELECT DISTINCT(station) FROM Measurement", engine)
    results_json = results['station'].to_json(orient='records')
    return results_json
#%%
### TEMPERATURE APP
### Dates and temperature observations for the last year of data
@app.route("/api/v1.0/tobs")
def date_temperature():
    #Query the dates and temperature observations of the most active station for the last year of data.
    results = pd.read_sql("SELECT * FROM Measurement\
                          WHERE date BETWEEN\
                          date('2016-08-23') AND date('2017-08-23')\
                          ORDER BY DATE(date)", engine)
    #Return a JSON list of temperature observations (TOBS) for the previous year.
    results_json = results[['date','tobs']].to_json(orient='records')
    return results_json           

#%%
if __name__ == '__main__':
    app.run(debug=True)
