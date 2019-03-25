#!/usr/bin/env python3
import time
from flask import Flask, request
app = Flask(__name__)

def factorization(n):
    fact = []
    i = 2
    while i <= n:
        if n % i ==  0:
            fact.append(i)
            n //= i
        else:
            i += 1
    return fact

@app.route('/')
def highload_probe():
    diff = int(request.args.get('time', ''))
    x = 191666634999089
    start = time.time()
    b = True
    while b:
        factorization(x)
        end = time.time()
        if (end - start > diff):
            b = False
    return 'High load probe done'

@app.route("/livetest")
def livetest():
    return "TEST OK"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
