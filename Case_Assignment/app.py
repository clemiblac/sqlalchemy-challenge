# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:48:04 2020

@author: clemi
"""
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
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
        f"<h4>Below are the list of available Routes:<h4/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Date Ranges<br/>"
        f"Enter your desired start date or end date as shown -- /api/v1.0/YYYY-MM-DD<br/>"
        f"/api/v1.0/&ltstart &gt<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt<br/>"
    )

#%%
### PRECIPITATION APP
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Convert the query results to a dictionary using `date` as the key and `prcp` as the value
    results = pd.read_sql("SELECT * FROM measurement", engine)
    
    
    #Return the JSON representation of your dictionary.
    results_json = results[['date','prcp']].to_json(orient='records') 

    return results_json
#%%
### STATIONS APP
@app.route("/api/v1.0/stations")
def stations():
    #Return a JSON list of stations from the dataset.
    results = pd.read_sql("SELECT DISTINCT(station) FROM measurement", engine)
    results_json = results['station'].to_json(orient='records')
    return results_json
#%%
### TEMPERATURE APP
### Dates and temperature observations for the last year of data
@app.route("/api/v1.0/tobs")
def date_temperature():
    #Query the dates and temperature observations of the most active station for the last year of data.
    results = pd.read_sql("SELECT * FROM measurement\
                          WHERE station='USC00519281'\
                          AND date BETWEEN\
                          date('2016-08-23') AND date('2017-08-23')\
                          ORDER BY DATE(date)", engine)
    #Return a JSON list of temperature observations (TOBS) for the previous year.
    results_json = results[['date','tobs']].to_json(orient='records')
    return results_json           
#%%
### Start date given
@app.route("/api/v1.0/<start>")
def start_date(start):

    """Fetch data  for all dates greater than or equat to the start date the path variable is supplied by the use, or a 404 if not"""
    
 
    # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    start_text=sqlalchemy.text("SELECT date FROM measurement WHERE date >= :name")
    results = pd.read_sql(start_text, engine,params={'name':start})

    results_json = results[['date','tobs']].to_json(orient='records')
    return results_json  
        



    #return jsonify({"error": f" No data for start date {start} was found. Please make sure the format is YYYY-MM-DD"}), 404


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
#%%
  #and `/api/v1.0/<start>/<end>`
#%%
if __name__ == '__main__':
    app.run(debug=True)
