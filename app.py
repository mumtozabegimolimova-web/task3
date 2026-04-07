from flask import Flask, request

app = Flask(__name__)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

@app.route('/mumtozabegimolimova_gmail_com', methods=['GET'])
def calculate():
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return "NaN"

        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            return "NaN"

        return str(lcm(x, y))
    except:
        return "NaN"
@app.route('/')
def home():
    return "OK"
