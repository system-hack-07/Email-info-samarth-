from flask import Flask, send_from_directory, jsonify, request
from datetime import datetime
import os

app = Flask(__name__, static_folder='static', static_url_path='')

# Demo data
DEMO_RESULTS = {
    "email": "[email protected]",
    "first_seen": "Nov 13, 2020",
    "last_seen": "Jan 2, 2024",
    "breaches": 4,
    "infostealer_logs": 5,
    "accounts": [
        {"platform": "Google", "id": "123456789", "last_seen": "2025-08-08"},
        {"platform": "LinkedIn", "username": "customer-demo-123456"},
        {"platform": "GitHub", "username": "customer3146"}
    ]
}

@app.route('/')
def serve_index():
    try:
        with open(os.path.join(app.static_folder, 'index.html'), 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Remove externals
        html = html.replace('js/gtag/js.js', '')
        html = html.replace('G-54BN4RDBV4', '')
        html = html.replace('https://rsms.me/', '')
        html = html.replace('https://docs.intelbase.is', '')
        
        # Rebrand
        html = html.replace('IntelBase', "Samarth's IntelBase")
        
        # Welcome banner
        banner = '''
        <div style="background:#111; color:#fff; padding:15px; text-align:center; font-weight:bold; border-bottom:4px solid #3b82f6;">
            🔥 Welcome to Samarth's Email Intelligence Platform | Made by Samarth | Contact: samarth@demo.com
        </div>
        '''
        html = html.replace('<body', banner + '<body', 1)
        
        return html
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1><p>Make sure static/index.html exists.</p>", 500

@app.route('/api/lookup', methods=['POST'])
def api_lookup():
    try:
        data = request.get_json(silent=True) or {}
        email = data.get('email', '[email protected]')
        result = DEMO_RESULTS.copy()
        result['email'] = email
        result['timestamp'] = datetime.now().isoformat()
        return jsonify({"status": "success", "data": result})
    except:
        return jsonify({"status": "error"}), 500

@app.route('/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except:
        return "404 - File not found", 404

if __name__ == '__main__':
    print("Samarth's IntelBase running...")
    app.run(host='0.0.0.0', port=5000, debug=True)
