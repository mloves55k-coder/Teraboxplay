from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/extract')
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={url}"
        r = requests.get(api_url, timeout=15)
        return r.json()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel handling
app = app
