from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def add(x, y):
    return x + y
def multipy(x, y):
    return x * y
def divi(x, y):
    return x / y
def minus(x, y):
    return x - y

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # unit tests
    assert 5 == add(3,2)
    assert 6 == multipy(3,2)
    assert 10 == minus(20,10)
    assert 5 == divi(10,2)
    app.run(debug=True, host='0.0.0.0', port=port)