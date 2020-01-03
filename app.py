from flask import Flask, jsonify, json
from Controllers.numberController import is_two_sided_prime, number_details

app = Flask(__name__)

@app.route('/isTwoSidedPrime/<int:num>')
def check_two_sided_prime(num):
    return jsonify(is_two_sided_prime(num))

@app.route('/numberDetails/<int:num>')
def get_number_details(num):
    return json.dumps(number_details(num))

app.run(port=3000)