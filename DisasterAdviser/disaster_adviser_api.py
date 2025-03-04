from flask import Flask, jsonify
from hazard_parser import parse_xml

app = Flask(__name__)


@app.route("/hazards", methods=['GET'])
def get_hazards():
    try:
        hazards = parse_xml()
        return jsonify(hazards), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
