from flask import Flask, jsonify, request
from flask_cors import CORS

from editor import query

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/api/v1/query', methods=['POST'])
def process_query():
    raw_query_obj = request.json

    q_response = query.process(raw_query_obj["query"])

    return jsonify({"data": q_response}), 200


if __name__ == "__main__":
    app.run(debug=True)