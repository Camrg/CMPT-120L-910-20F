from flask import Flask, render_template
import logging
app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.warning("dont mess with me")
    return render_template('Helloworld.html')