__author__ = 'canerten'

import energenie
from flask import Flask, jsonify,  request,  render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/on/', methods=['GET'])
def on():
    switchVal = request.args.get('switchValue', 0, type=int)
    ret_data = {"value": switchVal}
    energenie.switch_on(switchVal)
    return jsonify(ret_data)


@app.route('/off/', methods=['GET'])
def off():
    switchVal = request.args.get('switchValue', 0, type=int)
    ret_data = {"value": switchVal}
    energenie.switch_off(switchVal)
    return jsonify(ret_data)


@app.errorhandler(404)
def fourOhFour(error):
    return render_template('fourohfour.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
