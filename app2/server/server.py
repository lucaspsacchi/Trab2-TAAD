from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'metrics'
app.config['MONGO_URI'] = 'mongodb://100.0.0.2:27017/metrics'


mongo = PyMongo(app)


@app.route('/metrics', methods=['POST'])
def insert_metric():
    data = request.form.to_dict()
    mongo.db.metrics.insert_one(data)
    return jsonify({'CREATED': True}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
