from flask import Flask, render_template, send_from_directory, request
import requests
from flask_cors import CORS

app = Flask(__name__)
#CORS(app, origins=["http://127.0.0.1:5000"])
# 仮想的なAPIのURL（実際のAPIのエンドポイントに置き換えてください）
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
def ax_js_file():
    return send_from_directory('./static', "axios.min.js")
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
    index()