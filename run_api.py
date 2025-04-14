import logging
import sys

from api.app import create_app

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

app = create_app()
if __name__ == '__main__':
    logger.info("Starting application")
    app.run(host='localhost', port=8033, debug=True)
