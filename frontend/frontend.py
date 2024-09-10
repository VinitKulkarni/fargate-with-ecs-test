from flask import Flask
import requests
import socket
import os

app = Flask(__name__)
hostname = socket.gethostname()
backend_url = os.getenv('BACKEND_SERVICE_URL')

@app.route('/')
def index():
    response = requests.get(f"{backend_url}/data")
    return f"It is {hostname}.\n{response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)