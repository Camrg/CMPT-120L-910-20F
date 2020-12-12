from flask import Flask, render_template, url_for
import logging
app = Flask(__name__)

#This is the home page, from here you can access all other pages
@app.route('/')
@app.route("/home")
def home():
    app.logger.warning("Welcome to the home page")
    return render_template('Helloworld.html')

@app.route('/aboutme')
def aboutme():
    app.logger.warning("user naviagted to the about me page")
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    app.logger.warning("user navigated to the contact page")
    return render_template('contact.html')

@app.route('/myhobbies')
def myhobbies():
    app.logger.warning("user navigated to the hobbies page")
    return render_template('myhobbies.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404