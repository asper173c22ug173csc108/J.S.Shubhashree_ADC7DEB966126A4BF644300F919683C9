Server (Flask)
from flask import Flask
app = Flask('app')
@app.route('/')
def hello_world():
  return 'Hello, World!'
app.run(host='0.0.0.0', port=8080)

Factorial
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))

Hello World￼Not
