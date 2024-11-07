from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('./Template/index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        elif ops == 'subtract':
            r = num1 - num2
            result = f"The difference between {num1} and {num2} is {r}"
        elif ops == 'multiply':
            r = num1 * num2
            result = f"The product of {num1} and {num2} is {r}"
        elif ops == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f"The quotient of {num1} divided by {num2} is {r}"
            else:
                result = "Error: Division by zero is not allowed."
        else:
            result = "Error: Unsupported operation."

        return render_template('results.html', result=result)

@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        ops = request.json.get('operation')
        num1 = int(request.json.get('num1'))
        num2 = int(request.json.get('num2'))
        if ops == 'add':
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        elif ops == 'subtract':
            r = num1 - num2
            result = f"The difference between {num1} and {num2} is {r}"
        elif ops == 'multiply':
            r = num1 * num2
            result = f"The product of {num1} and {num2} is {r}"
        elif ops == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f"The quotient of {num1} divided by {num2} is {r}"
            else:
                result = "Error: Division by zero is not allowed."
        else:
            result = "Error: Unsupported operation."

        return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
