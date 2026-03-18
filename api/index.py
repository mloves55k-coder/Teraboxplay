from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL"}), 400
    
    try:
        # Using a reliable third-party bypasser backend
        api_res = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={url}"
        r = requests.get(api_res, timeout=10)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For Vercel Serverless
def handler(app, event, context):
    return app(event, context)
  
