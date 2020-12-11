from flask import Flask
import logging
app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.warning("dont mess with me")
    return 'Hello, World!'