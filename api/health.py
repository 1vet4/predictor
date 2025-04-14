import logging

from flask_restful import Resource

logger = logging.getLogger(__name__)


class HealthResource(Resource):
    def get(self):
        logger.info("Health request")
        return {
            'status': 'OK',
        }
