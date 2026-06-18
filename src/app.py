from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>OmniGrid Command Center</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 40px; }
            .header { text-align: center; margin-bottom: 40px; }
            .grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
            .status-ok { color: #28a745; font-weight: bold; font-size: 1.2em; }
            .status-warn { color: #ffc107; font-weight: bold; font-size: 1.2em; }
            .status-danger { color: #dc3545; font-weight: bold; font-size: 1.2em; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>National Infrastructure Command Center</h1>
            <p>Project OmniGrid - Live Telemetry Dashboard</p>
        </div>
        <div class="grid-container">
            <div class="card"><h3>⚡ Energy Grid</h3><p class="status-ok">OPERATIONAL</p><p>Load: 45,000 MW</p></div>
            <div class="card"><h3>📡 Telecom Networks</h3><p class="status-warn">DEGRADED</p><p>Latency: 120ms (Region B)</p></div>
            <div class="card"><h3>💧 Water Utilities</h3><p class="status-ok">OPERATIONAL</p><p>Pressure: Nominal</p></div>
            <div class="card"><h3>🏥 Emergency Services</h3><p class="status-danger">HIGH ALERT</p><p>Active Incidents: 14</p></div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "version": "2.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
