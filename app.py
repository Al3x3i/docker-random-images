from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# DEFAULT_PORT = 3333
DEFAULT_HOST = "0.0.0.0"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    docker_port = os.environ.get("DOCKER_PORT", random.randrange(1024,1100,1))
    app.run(host=DEFAULT_HOST, port=int(docker_port))
