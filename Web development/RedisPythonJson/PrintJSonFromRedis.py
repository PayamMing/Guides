from flask import Flask, jsonify, render_template, make_response
import time
import datetime
from random import random
import logging
import redis
from functools import wraps

# TODO: Remove CORS header from production
# Cross Origin Resource Sharing: Allow any
def CORS_ANY(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return_data = func(*args, **kwargs)
        response = make_response(return_data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapped

_DEBUG = False

r = redis.StrictRedis(host='127.0.0.1',port=6379)


app = Flask(__name__)


# Make Jinja not interfere with Vue.js
options = app.jinja_options.copy()
options.update({
    'variable_start_string': '%%',
    'variable_end_string': '%%'
})
app.jinja_options = options

if not _DEBUG:
    JSONIFY_PRETTYPRINT_REGULAR = False
    app.config.from_object(__name__)


@app.route('/minHash')
@CORS_ANY
def myfunction():
	try:
		minVar = r.hget('MinHash','Sofia')
	except TypeError:
		minVar = 0
	return jsonify(minVar)


@app.route('/toggle_hash')
@CORS_ANY
def writeData():
    minVar = 'Sofia'
    r.hset('MinHash', 'Sofia', 'HIIII')
    minVar = r.hget('MinHash', minVar)
    return jsonify({'MinHash':minVar})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
