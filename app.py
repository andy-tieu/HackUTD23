from flask import Flask, render_template, request, jsonify

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit_data():
    # Handle user input logic here and respond with JSON data
    data = request.get_json()
    # Process data and return a response

if __name__ == '__main__':
    app.run(debug=True)
