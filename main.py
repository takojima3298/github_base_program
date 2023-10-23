from flask import Flask, render_template, send_from_directory, request
import requests
from flask_cors import CORS

app = Flask(__name__)
#CORS(app, origins=["http://127.0.0.1:5000"])
# 仮想的なAPIのURL（実際のAPIのエンドポイントに置き換えてください）
API_URL = "https://example-api.com/data"
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
@app.route('/gcp5/static/styles.css')
def css_file():
    return send_from_directory('./static', "styles.css")

@app.route('/gcp5/static/scripts.js')
def js_file():
    return send_from_directory('./static', "scripts.js")

@app.route('/gcp5/static/axios.min.js')
def ax_js_file():
    return send_from_directory('./static', "axios.min.js")
@app.route("/", methods=["GET", "POST"])
def index():
    session_key = request.args.get("session_key", "", type=str)
    return render_template("form.html", session_key=session_key)

if __name__ == "__main__":
    app.run(debug=True)
    index()
# def main(request):
#    print("000")
#    if request.path == '../static/styles.css':
#        return css_file()
#    elif  request.path == '../static/scripts.js':
#        return js_file()
#    elif  request.path == '../static/axios.min.js':
#        return ax_js_file()
#    else:
#        print("aaaa")
#        return index()
    