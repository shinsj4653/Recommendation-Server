from flask import Flask, request, jsonify, import_ipynb
from book_recommendation_algorithm_V5-author_duplication import recommend_books

app = Flask(__name__)

@app.route("/api", methods=["GET", "POST"])

# Headers는 'Content-Type': 'application/json'
# Body는 JSON 형식으로 요청

def recommendation():
    if request.method == "POST":
        data = request.get_json()
        isbn = data.get("isbn")
        if isbn:
            return jsonify({"message": "Success! Request method is POST!"}), 201
        else:
            return jsonify({"message": "Error"}), 400
    else:
        return jsonify({"message": "Success! Request method is GET!"}), 200

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port=8080)
