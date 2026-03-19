from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/extract')
def handler():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        # Public bypasser API
        res = requests.get(f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={target_url}", timeout=10)
        return res.json()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
