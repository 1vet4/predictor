from flask import request, jsonify, render_template
import joblib
import pandas as pd
from flask_restful import Resource
import os

class PredictGDPResource(Resource):

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'model', 'random_forest_model.joblib')
        self.model = joblib.load(model_path, mmap_mode=None)

        self.top_features = ['WEO subject_NGDPRPPPPC_2018', 'WEO subject_NGDPRPPPPC_2017',
                             'WEO subject_NGDPRPPPPC_2016', 'WEO subject_NGDPRPPPPC_2015',
                             'WEO subject_NGDPRPPPPC_2014']


    def post(self):
        try:
            data = request.get_json()

            input_data = pd.DataFrame([data])

            # continent=data[continent]
            # population=data[population]
            # gross_nation_savings=data[gross_nation_savings]
            input_features = input_data[self.top_features]
            print(type(self.model))

            predictions = self.model.predict(input_features)

            predicted_gdp_per_capita = predictions[0]

            response = {
                'prediction': predicted_gdp_per_capita
            }

            return response

        except Exception as e:
            return {'error': str(e)}, 400
