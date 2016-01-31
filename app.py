import os
import numpy
import scipy
import sklearn
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home from Anaconda'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
