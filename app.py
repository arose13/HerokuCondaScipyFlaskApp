import numpy
import scipy
import sklearn
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home from Anaconda'


if __name__ == '__main__':
    app.run()
