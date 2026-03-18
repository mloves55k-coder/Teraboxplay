from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/extract')
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL"}), 400
    
    # Direct public bypasser call
    api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={url}"
    r = requests.get(api_url, timeout=10)
    return jsonify(r.json())

# Vercel compatibility
app = app
