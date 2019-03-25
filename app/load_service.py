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
    x = 191666634999089
    diff = int(request.args.get('time', '1'))
    number = int(request.args.get('number', str(x)))
    start = time.time()
    b = True
    while b:
        l = factorization(number)
        end = time.time()
        if (end - start > diff):
            b = False

    strng = 'Hi! This is service for factorization of the number 191666634999089'
    strng += ' by default. <br> I like minimalism without huge GUI, so you can go by the link '
    strng += 'localhost:5000/?time=30&number=191666634999089 and rerun the '
    strng += 'computations as long as you want! <br>'
    strng += 'You can change the argument near time (seconds) and desired number (number)'
    strng += ' and run your own computations! <br>'
    strng += 'If you see that hence high load probe done! <br>'
    strng += '<br>'
    strng += 'Factorized list for ' + str(number) + ' is ' + str(l)
    return strng

@app.route("/livetest")
def livetest():
    return "TEST OK"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
