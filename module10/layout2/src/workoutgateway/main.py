import os
import sys
import uuid
import atexit
import requests
import time
import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from score import do_some_work
from workout import Workout


app = Flask(__name__,
            static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


RUN_CONTROLLER_URL = "please provide url via env vars"

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/api/", methods=('POST',))
@cross_origin()
def main(r=request):
    try:
        mt_in = time.monotonic()
        request_id = str(uuid.uuid4())

        log = {
            "monotonic_time": mt_in,
            "event_t": "request",
            "request_id": request_id,
            "path": "/",
            "errors": [],
        }

        content = r.json

        try:
            workout = Workout.from_dict(content)
        except KeyError as e:
            e_msg = "Missing required field %s" % e

            log["validated"] = False
            log["errors"].append(e_msg)

            return e_msg, 400
        except ValueError as e:
            e_msg = str(e)

            log["validated"] = False
            log["errors"].append(e_msg)

            return e_msg, 400

        log["validated"] = True

        _workout_id = uuid.uuid4()
        workout_id = str(_workout_id)
        p = do_some_work(int(content["intensity"]))
        log["p"] = p

        try:
            headers = {}
            payload = {**workout.as_dict(), "workout_id": workout_id}

            r = requests.post(RUN_CONTROLLER_URL, json=payload, headers=headers)
        except requests.exceptions.ConnectionError:
            log["errors"].append("Downstream not available")
            return "Something went wrong on our side :C", 500

        downstream_status = r.status_code
        log["downstream_response_code"] = r.status_code

        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            log["errors"] = "Downstream errored"

            if downstream_status == 500:
                msg = "Something went wrong on our side :C"
            else:
                msg = r.text

            return msg, downstream_status
        else:
            log["workout_id"] = workout_id
            score = r.json()["score"]
            p2 = do_some_work(score)
            log["p2_over_score"] = p2

        return r.json()
    finally:
        print(json.dumps(log), file=sys.stderr)


@app.route("/health", methods=('GET',))
def health():
    return jsonify({"status": "ok"})

def shutdown_hook():
    log = {
        "event_t": "shutdown",
        "wall_time": time.time(),
        "monotonic_time": time.monotonic(),
        "errors": [],
    }
    print(json.dumps(log), file=sys.stderr)

if __name__ == "__main__":
    port = os.environ["PORT"]
    RUN_CONTROLLER_URL = os.environ["RUN_CONTROLLER_URL"]
    debug = bool(os.environ.get("DEBUG"))

    atexit.register(shutdown_hook)

    log = {
        "event_t": "startup",
        "wall_time": time.time(),
        "monotonic_time": time.monotonic(),
        "config": {
            "port": int(port),
            "run_controller_url": RUN_CONTROLLER_URL,
            "debug": debug
        },
        "errors": [],
    }
    print(json.dumps(log), file=sys.stderr)

    app.run('0.0.0.0', debug=debug, port=port)
