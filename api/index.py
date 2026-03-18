from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        # Stable worker bypasser
        api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={target_url}"
        r = requests.get(api_url, timeout=15)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ye line Vercel ke liye sabse zaroori hai
app = app
