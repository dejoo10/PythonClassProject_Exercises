import sys
import json
from flask import Flask, request, Response

#The code looks ok, but it is not responding on the web

app = Flask(__name__)
@app.route('/prime')
def prime():
    args = request.args
    num = int(args.get("number"))

    prime_check = 0

    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                prime_check = "True"
                break
    if prime_check:
        prime_check = "False"
    else:
        prime_check = "True"

    aaa = prime_check

    response = {
        "Number" : num,
        "isPrime" : aaa
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

sys.exit(0)
