import os
import uuid
import atexit
import json

import redis
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=('POST',))
def main(r=request):
    request_id = str(uuid.uuid4())
    app.logger.debug("Received request %s to /", request_id)

    content = r.json

    app.logger.debug("Request %s positively validated", request_id)

    workout_id = content["workout_id"]
    app.logger.debug("Processing workout %s in request %s", workout_id, request_id)

    # TODO: actually calculate the run score based on random and log the random && score + request id!
    score = 73
    content["score"] = score

    r = redis.Redis(host=os.environ["REDIS_HOST"], password=os.environ["REDIS_PASSWORD"])
    r.set(workout_id, json.dumps(content))
    app.logger.debug("Persisted workout %s in db for request %s", workout_id, request_id)

    return jsonify({"workout_id": workout_id, "score": score})


@app.route("/divide", methods=('GET',))
def divide(r=request):
    return jsonify({"results": 5/0})


@app.route("/health", methods=('GET',))
def health():
    return jsonify({"status": "ok"})

def shutdown_hook():
    app.logger.info("Gracefully shutting down")

if __name__ == "__main__":
    port = os.environ["PORT"]
    debug = bool(os.environ.get("DEBUG"))

    atexit.register(shutdown_hook)

    app.run('0.0.0.0', debug=debug, port=port)
