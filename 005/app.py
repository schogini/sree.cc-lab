from flask import Flask

import os
import socket

app = Flask(__name__)
@app.route("/")

def hello():
    html = "<h1><b>My Container ID: {hostname}</h1>"
    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)

