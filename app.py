#------------------------------------------------------------------------------#

#--- Importing Libraries ---#

import flask
import joblib
from flask_cors import CORS
from flask import request
from termcolor import colored

#------------------------------------------------------------------------------#
"""Flask app creation with CORS enabled"""
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#------------------------------------------------------------------------------#

# --- Model Loading joblib --- #
model = joblib.load("car_prediction")

#------------------------------------------------------------------------------#

@app.route('/')
def homepage():
    return flask.render_template('form.html')
    
#------------------------------------------------------------------------------#

@app.route('/car_selling',methods=['POST'])
def car_selling():
    print(colored(request.form, "yellow"))
    if request.method == 'POST':
        #getting data from request
        km_driven = int(request.form["km_driven"])
        fuel = int(request.form["fuel"])
        transmission = int(request.form['transmission'])
        owner = int(request.form['owner'])
        mileage = float(request.form['mileage'])
        engine = float(request.form['engine'])
        max_power = float(request.form['max_power'])
        seats = int(request.form['seats'])
        Dealer = int(request.form['Dealer'])
        Individual = int(request.form['Individual'])
        Trustmark_Dealer = int(request.form['Trustmark_Dealer'])
        
        price = model.predict([[km_driven,
                    fuel,
                    transmission,
                    owner,
                    mileage,
                    engine,
                    max_power,
                    seats,
                    Dealer,
                    Individual,
                    Trustmark_Dealer]])[0]
        print(colored(price, "green"))
    return flask.render_template("index.html", value=price)

#------------------------------------------------------------------------------#
		
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5555,debug=True)
