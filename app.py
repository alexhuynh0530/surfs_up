import datetime as dt
import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# create a variable for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database 
session = Session(engine)

# create a Flask application called "app."
app = Flask(__name__)

# the welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end
    ''')

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    #code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query to get the date and precipitation for the previous year.
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    #use jsonify() to format our results into a JSON structured file
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    #query that will allow us to get all of the stations
    results = session.query(Station.station).all()
    #unraveling our results into a one-dimensional array using function np.ravel()
    #using results as parameter
    #next, convert unravled results array into a list using list() function
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Monthly Temperature Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    #query that will allow us to get all of the stations
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    #jsonify our temps list, and then return it
    return jsonify(temps=temps)

# Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    #create list called sel equal to the query selecting minimum, average, and maximum temperatures from SQLite db
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           
    
    if not end:
        #query our database using the list that we just made
        results = session.query(*sel).\
        filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    #calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)