from flask import Flask
from gevent.pywsgi import WSGIServer
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = {"message": "Hello World", "time": current_time}
    return response

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()