import sys
from math import sqrt
import json
from flask import Flask, request, Response


app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime():
    args = request.args
    number = float(args.get("number"))
    prime = prime_ber(number)

    response = {
        "Number" : number,
        "isPrime" : prime
    }
    return response

def prime_ber(num):
    prime_check = 0
    if(num>1):
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                prime_check = 1
                break
        if (prime_check == 0):
            prime("True")
        else:
            print("False")
    else:
        print("False")
    return prime_ber


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

sys.exit(0)
