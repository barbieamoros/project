from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    '''
    doctsting
    '''
    return render_template('index.html')

@app.route('/cv')
def cv():
    '''
    doctsting
    '''
    return render_template('cv.html')