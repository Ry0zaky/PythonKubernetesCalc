from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Simple Calculator API!",
        "instructions": "Use the /calculate endpoint with query parameters 'a', 'b', and 'operation'.",
        "example": "/calculate?a=5&b=3&operation=add"
    })

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a_param = request.args.get('a')
        b_param = request.args.get('b')

        if a_param is None or b_param is None:
            return jsonify({"error": "Missing required parameters 'a' and 'b'."}), 400

        try:
            a = float(a_param)
            b = float(b_param)
        except ValueError:
            return jsonify({"error": "Invalid input. 'a' and 'b' must be numbers."}), 400

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

    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
