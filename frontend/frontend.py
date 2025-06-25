from flask import Flask
import requests
import socket
import os

app = Flask(__name__)
hostname = socket.gethostname()
backend_url = "http://backend:8080"

@app.route('/')
def message():
    return "hiii"


@app.route('/api')
def index():
    response = requests.get(f"{backend_url}/data")
    return f"It is {hostname}.\n{response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
