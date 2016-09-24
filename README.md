# Python 3, Anaconda, Scipy, Numpy, etc and Flask on Heroku!

__Finally an example of how it's done!__

1. Create a `conda-requirements.txt` for conda installs and pip installs are in `requirements.txt`
2. Using gunicorn then my Procfile applies.
3. Use this buildpack `https://github.com/arose13/conda-buildpack.git`

## Note
- Make sure that python version is first on the list
- Make sure that Numpy is in front of Scipy on the conda-requirements.txt
- Make sure that Scipy is in front of Scikit-learn (If you're using it) on the conda-requirements.txt
