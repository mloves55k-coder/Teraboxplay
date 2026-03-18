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
        # Public API bypasser
        api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={target_url}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(api_url, headers=headers, timeout=10)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ko serverless function batane ke liye ye zaroori hai
def handler(event, context):
    return app(event, context)

# Local testing ke liye
if __name__ == '__main__':
    app.run()
    
