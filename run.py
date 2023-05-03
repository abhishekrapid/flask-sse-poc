from config import app, logging
from app.controller.server_sent_events import server_sent_event

app.register_blueprint(server_sent_event)

if __name__ == '__main__':
    logging.info('Server start.....')
    app.run(port='5000')

