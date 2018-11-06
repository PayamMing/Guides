

from flask import Flask, jsonify, render_template, make_response
import redis
from functools import wraps


redis_host = '127.0.0.1'
redis_port = 6379

r = redis.StrictRedis(host=redis_host, port=redis_port)

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

#read data 
@app.route('/GPS_RAFT_IN')
@CORS_ANY
def get_gps_raft_in():
	long_raft = r.hget('GPS_RAFT_IN','LONG_RAFT')
	lat_raft = r.hget('GPS_RAFT_IN','LAT_RAFT')
	return jsonify({'latitude' : lat_raft, 'longitude' : long_raft})

@app.route('/UPDATE_GPS_RAFT_IN<float:longitude>, <float:latitude>')
def update_gps_raft_in(longitude, latitude):
	key_gps_raft_in = 'GPS_RAFT_IN'
	key_long_raft = 'LONG_RAFT'
	key_lat_raft = 'LAT_RAFT'
	value_long = longitude
	value_lat = latitude  
	r.hset(key_gps_raft_in, key_long_raft, value_long)
	r.hset(key_gps_raft_in, key_lat_raft, value_lat)
	return jsonify({'updated_latitude' : value_lat, 'updated_longitude' : value_long})






if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')