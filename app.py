from flask import Flask, send_from_directory, jsonify, request
from datetime import datetime

app = Flask(__name__, static_folder='static', static_url_path='')

DEMO_RESULTS = {  # Fake rich demo data
    "email": "[email protected]",
    "first_seen": "Nov 13, 2020",
    "last_seen": "Jan 2, 2024",
    "breaches": 4,
    "infostealer_logs": 5,
    "accounts": [
        {"platform": "Google", "id": "123456789", "last_seen": "2025-08-08"},
        {"platform": "LinkedIn", "username": "customer-demo-123456", "full_name": "Customer Demo"},
        {"platform": "GitHub", "username": "customer3146"}
    ]
}

@app.route('/')
def index():
    with open('static/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Strip all tracking & externals
    html = html.replace('js/gtag/js.js', '#removed')
    html = html.replace('G-54BN4RDBV4', '')
    html = html.replace('https://rsms.me/', '#')
    html = html.replace('https://docs.intelbase.is', '#')
    html = html.replace('https://intelbase.is', '#')
    
    # Rebrand to Samarth
    html = html.replace('IntelBase', "Samarth's IntelBase")
    html = html.replace('<title>IntelBase</title>', '<title>Samarth\'s IntelBase - Email OSINT</title>')
    
    # Inject welcome banner
    welcome = '''
    <div style="background: #111; border-bottom: 4px solid #3b82f6; padding: 12px; text-align: center; color: #fff; font-size: 1.1rem;">
        🔥 Welcome to Samarth's Email Intelligence Tool | Made by Samarth | Contact: samarth@protonmail.com for full access
    </div>
    '''
    html = html.replace('<body data-sveltekit-preload-data="hover">', '<body data-sveltekit-preload-data="hover">' + welcome)
    
    return html

@app.route('/api/lookup', methods=['POST'])
def lookup():
    data = request.get_json(silent=True) or {}
    email = data.get('email', '[email protected]')
    result = DEMO_RESULTS.copy()
    result['email'] = email
    result['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return jsonify({"status": "success", "data": result})

@app.route('/api/search')
def search():
    q = request.args.get('q')
    return jsonify({"query": q, "results": DEMO_RESULTS})

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
