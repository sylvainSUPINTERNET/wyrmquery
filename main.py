from bson import json_util
from dotenv import load_dotenv
load_dotenv()
# OR, the same with increased verbosity
load_dotenv(verbose=True)

import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from editor import query


app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})




# Read instruction only one time then reuse it everywhere
with open("./editor/instructions.json") as instructionJson:
    instructions = json.load(instructionJson)


@app.route('/api/v1/query', methods=['POST'])
def process_query():
    raw_query_obj = request.json

    q_response = query.process(raw_query_obj["query"], instructions=instructions)
    response_formatted = json.dumps(q_response, default=json_util.default)
    return jsonify({"data": json.loads(response_formatted)}), 200


if __name__ == "__main__":
    app.run(debug=True)

