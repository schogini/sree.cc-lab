from flask import Flask
import socket
from redis import Redis, RedisError

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)


app = Flask(__name__)
@app.route("/")

def hello():

    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h1>Visits:</b>{visits}</h1>\n" \
          "<h2><b>My Container ID: {hostname}</h2>\n"

    return html.format(hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)
