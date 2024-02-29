from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Your Python code logic goes here
    data = {'message': 'Hello from Python!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)