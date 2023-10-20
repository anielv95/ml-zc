"""This file is to deploy the model and it was extracted from
https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-05-deployment/churn_serving.py"""

import pickle
import numpy as np

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
  X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]


with open('dv.bin', 'rb') as f_in: # very important to use 'rb' here, it means read-binary 
    dv = pickle.load(f_in)

with open('model1.bin', 'rb') as f_in: # very important to use 'rb' here, it means read-binary 
    model = pickle.load(f_in)

app = Flask('predict')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    prediction = predict_single(customer, dv, model)
    
    result = {
        'score_probability': float(prediction)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8585)