from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Simple Calculator API! Use /calculate endpoint with parameters 'a', 'b', and 'operation'."

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        operation = request.args.get('operation')

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return jsonify({"error": "Division by zero is not allowed"}), 400
            result = a / b
        else:
            return jsonify({"error": "Invalid operation. Use add, subtract, multiply, or divide."}), 400

        return jsonify({"a": a, "b": b, "operation": operation, "result": result})

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Ensure 'a' and 'b' are numbers."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
