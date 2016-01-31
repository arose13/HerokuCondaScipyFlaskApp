import numpy
import scipy
import sklearn
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home from Anaconda'


if __name__ == '__main__':
    # Use this port=33507 when you want to Flask to work on Heroku....
    app.run()
