from flask import Flask, jsonify, request 
from flask_cors import CORS
import orm as db
app = Flask(__name__)
CORS(app)

@app.route("/average")
def get_averge():
    """
    Return the average grade for each sem in JSON
    :return:
    """
    average, all_sem = db.fetch_average_grade()
    return jsonify( {'average': average, 'all_sem': all_sem} )

@app.route("/<string:id>/latest_results")
def latest_results(id):
    results = db.fetch_grade(id)
    context = dict(results = [results[0], results[1], results[2], results[3]], user = id)
    return jsonify(context)

@app.route("/<string:id>/plot", methods=["POST"])
def plot(id):
    """
    Receive JSON payload to plot results for each sem
    and store the results in DB
    """

    data = request.json
    gpas = list(data["sem1"], data["sem2"], data["sem3"], data["sem4"])
    status = db.insert_grades(id, gpas)
    return jsonify(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
