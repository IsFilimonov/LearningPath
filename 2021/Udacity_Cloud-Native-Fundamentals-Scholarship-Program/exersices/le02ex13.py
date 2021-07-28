"""
- A log line should be recorded the timestamp and the requested endpoint e.g. "{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"
- The logs should be stored in a file with the name app.log. Refer to the logging Python module for more details.
- Enable the collection of Python logs at the DEBUG level. Refer to the logging Python module for more details.
"""
import logging
import datetime

from flask import Flask, json, request


LOGGING_FORMAT = "{TIMESTAMP}, {ENDPOINT_NAME} endpoint was reached"

app = Flask(__name__)

handler = logging.FileHandler("app.log")
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)


@app.route('/status')
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.debug(LOGGING_FORMAT.format(
        TIMESTAMP=datetime.datetime.now(),
        ENDPOINT_NAME=request.url_rule.rule))

    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.debug(LOGGING_FORMAT.format(
        TIMESTAMP=datetime.datetime.now(),
        ENDPOINT_NAME=request.url_rule.rule))

    return response


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
