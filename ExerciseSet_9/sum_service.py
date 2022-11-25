import sys
import json
from flask import Flask, request

app = Flask(__name__)
@app.route('/sum/<number1>/<number2>')
def sum(number1, number2):
    try:
        number1 = float("number1")
        number2 = float("number2")
        sum = number1+number2

        response = {
            "number1" : number1,
            "number2" : number2,
            "sum" : sum,
            "status" : 200
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as added",
            "status":400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status":404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetypes="application/json")
    return http_response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)