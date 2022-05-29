from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import btcmodel


import flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#@app.route('/')
#def static_file():
#    return app.send_static_file('index1.html')

@app.route('/index')
def index():
  return flask.render_template('index4.html')

@app.route('/predict_btc', methods=['GET','POST'])
# function for predictions
def predict_btc():
  modelsvr = joblib.load('modelsvr.pkl')
  data = joblib.load("data.pkl")

  year = request.form['year']
  month = request.form['month']
  day = request.form['day']
  
  if len(str(month))==1:
    month = '0'+str(month)
  else:
    month = month
  if len(str(day))==1:
    day = '0'+str(day)
  else:
    month = month
  Date = str(year)+'/'+str(month)+'/'+str(day)

  X = data.iloc[:,1:-1]
  observation = data[data['Date'] == Date]
  x =  observation.iloc[:,1:-1]
  x_scaled = btcmodel.scale_data1(X,x)
  Actual_price = round(np.ravel(observation.iloc[:,-1:].values)[0],2)
  predicted_price = round(np.ravel(modelsvr.predict(x_scaled))[0],2)
  return flask.render_template('index4.html', Actual_price=Actual_price, predicted_price=predicted_price )


if __name__ =="__main__":
    app.run(debug=True)
