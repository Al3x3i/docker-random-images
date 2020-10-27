from flask import Flask, render_template
import os
import random

app = Flask(__name__)

DEFAULT_PORT = 3333
DEFAULT_HOST = "0.0.0.0"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":

    docker_port = os.environ.get("DOCKER_PORT", DEFAULT_PORT)
    
    print("Running Random Web page on: {}:{}".format(DEFAULT_HOST,docker_port))
    app.run(host=DEFAULT_HOST, port=int(docker_port))

    # Use for producion
    #from waitress import serve
    #serve(app, host=DEFAULT_HOST, port=docker_port)
