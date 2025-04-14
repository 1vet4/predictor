import unittest
import json
from api.predictor import app
from jsonschema import validate


class PredictorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.sample_payload = {
            "info": {"continent": "Europe",
                     "population": 10000,
                     "gross_nation_savings": 50000},
            "WEO subject_NGDPRPPPPC_2014": 0.2,
            "WEO subject_NGDPRPPPPC_2015": 0.3,
            "WEO subject_NGDPRPPPPC_2016": 0.4,
            "WEO subject_NGDPRPPPPC_2017": 0.5,
            "WEO subject_NGDPRPPPPC_2018": 0.5
        }

    def test_predict_endpoint(self):
        response = self.app.post('/predict_gdp', json=self.sample_payload)

        self.assertEqual(response.status_code, 200)

    def test_response_type(self):
        response = self.app.post('/predict_gdp', json=self.sample_payload)
        response = json.loads(response.data)
        self.assertIsInstance(response.get('prediction'), float)

    def test_json_input(self):
        json_schema = {
            "type": "object",
            "properties": {
                "info": {
                    "type": "object",
                    "properties": {
                        "continent": {"type": "string"},
                        "population": {"type": "number"},
                        "gross_nation_savings": {"type": "number"}
                    },
                    "required": ["continent", "population", "gross_nation_savings"],
                    "additionalProperties": False
                },
                "WEO subject_NGDPRPPPPC_2014": {"type": "number"},
                "WEO subject_NGDPRPPPPC_2015": {"type": "number"},
                "WEO subject_NGDPRPPPPC_2016": {"type": "number"},
                "WEO subject_NGDPRPPPPC_2017": {"type": "number"},
                "WEO subject_NGDPRPPPPC_2018": {"type": "number"}
            },
            "required": ["info", "WEO subject_NGDPRPPPPC_2014", "WEO subject_NGDPRPPPPC_2015",
                         "WEO subject_NGDPRPPPPC_2016", "WEO subject_NGDPRPPPPC_2017",
                         "WEO subject_NGDPRPPPPC_2018"]
        }

        validate(instance=self.sample_payload, schema=json_schema)


if __name__ == '__main__':
    unittest.main()
