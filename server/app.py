#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text) #printing the string to the console
    return f'<h1>Printed: {text}</h1>'

@app.route('/count/<int:number>')
def count(number):
    numbers_list = '\n'.join(str(i) for i in range(1, number + 1))
    return f'<pre>{numbers_list}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 // num2 #for integer division
    elif operation == '%':
        result = num1 % num2
    
    return f'<h1>Result: {result}</h1>'

if __name__ == '__main__':
    app.run(port=5557, debug=True)