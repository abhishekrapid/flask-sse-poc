from flask_sse import sse
from flask import request, abort, render_template, Blueprint
from config import logging, app

server_sent_event = Blueprint('server-sent-events', 'server-sent-events')


@sse.before_request
def user_authenticate():
    logging.info(request.args)
    if request.args.get('Authorization'):
        logging.info(request.args.get('Authorization'))

        # we can add authentication condition here.
    else:
        logging.error("Invalid User")
        abort(403)


app.register_blueprint(sse, url_prefix='/stream')


@server_sent_event.route('/<transcript_id>')
def index(transcript_id):
    return render_template('index.html', uname=transcript_id)


@server_sent_event.route('/publisher/<transcript_id>')
def publisher(transcript_id):
    sse.publish(
        {
            'message': request.args['message'],
        },
        type=request.args['transcript_id'],
        channel=transcript_id
    )

    return "Message Sent!"

