import emoji
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return emoji.emojize('Python is :thumbs_down:')
    # return emoji.demojize('Python is 👍')
    return emoji.emojize('This is making me :grimacing:')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)






# from flask import Flask
# app = Flask(__name__)

# @app.route('')
# def hello_world():
#     return 'Hello, World!'