from flask import Flask, current_app, render_template

from config import app
from models import db, Keyword

@app.route('/', methods=['GET'])
def index():
    """
    Home Page / Survey View
    """
    return render_template('full.html')

@app.route('/about', methods=['GET'])
def about():
    """
    About Page view
    """
    return render_template('about.html')

@app.route('/calculate-results', methods=['POST'])
def calculateResults():
    """
    POST-only URL that retrieves survey results
    based on POSTed keywords
    """
    pass
    
@app.route('/email-results', methods=['POST'])
def emailResults():
    """
    POST-only URL for emailing survey results to user
    """
    pass

#For testing only, production will need a different server
if __name__ == '__main__':
    app.run(debug=True)
