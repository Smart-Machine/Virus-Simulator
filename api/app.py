from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

from globals import dataset


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def welcome_page():
    return render_template('others/welcome.html')
    # return "Welcome"


@app.route('/data', methods = ['GET', 'POST'])
def handle_data():

    if request.method == 'POST':
        dataset.add(
            timestamp=request.form['timestamp'],
            cases=request.form['cases'],
            deaths=request.form['deaths'],
            recoveries=request.form['recoveries'],
            infected=request.form['infected']
        )
        return "Server recievied."

    if request.method == 'GET':
        return jsonify(dataset.get()) 
        # return render_template('others/data.html', dataset=dataset) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')
