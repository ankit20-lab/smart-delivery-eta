from flask_cors import CORS
from flask import Flask, jsonify
from graph_engine import get_best_route

app = Flask(__name__)
CORS(app)

@app.route('/route')


def route():

    path, eta, rider, rider_eta = get_best_route()

    return jsonify({
        "best_route": path,
        "delivery_eta": f"{eta} minutes",
        "assigned_rider": rider,
        "rider_to_customer_time": f"{rider_eta} minutes"
    })

if __name__ == "__main__":
    app.run(debug=True)