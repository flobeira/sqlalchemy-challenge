import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



# 3. Define static routes
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to the Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    #Query precipitation on the last year
    results = session.query(measurement.date > '2016-08-23').all()

    session.close()
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations():
    session2 = Session(engine)
    #Query precipitation on the last year
    results2 = session2.query(measurement.date).group_by(measurement.station).all()

    session.close()
    # Convert list of tuples into normal list
    all_names2 = list(np.ravel(results2))

    return jsonify(all_names2)

@app.route("/api/v1.0/tobs ")
def tobs():



@app.route("/")
def home():
    return (
        f"Welcome to the Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )



# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
