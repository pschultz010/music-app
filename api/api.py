from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = make_response(
        jsonify(
            {"data": "hello from python api"}
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/artists")
def get_artists():
    artists = ["Eminem", "Snoop Dogg", "Dr. Dre"]
    
    artists[1] = "DJ Min"

    return jsonify({"artists": artists})

@app.route("/update")
def update_artists():
    return jsonify({"artists": ["Tame", "Gaga"]})