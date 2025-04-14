from flask import Flask, render_template
import flask_restful
import logging
from .predictor import PredictGDPResource
from .health import HealthResource

logger = logging.getLogger()


def create_app():
    app = Flask(__name__)

    logger.info("Flask App ready")

    api = flask_restful.Api(app, catch_all_404s=True)

    @app.route('/predict_gdp', methods=['GET'])
    def show_form():
        return render_template('index.html')
    api.add_resource(HealthResource, '/health')
    api.add_resource(PredictGDPResource, '/predict_gdp')

    logger.info("App Configured")

    return app
