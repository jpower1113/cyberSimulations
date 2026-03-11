import os
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# CONFIGURATION
# Ensure this matches where your attack scripts live
OFFENSE_DIR = os.path.join(os.getcwd(), 'offense')
# Ensure this matches where Suricata logs to (from your suricata.pdf logs)
SURICATA_LOG = '/var/log/suricata/fast.log'


@app.route('/')
def index():
    """Render the main dashboard."""
    return render_template('index.html')


@app.route('/simulate', methods=['POST'])
def simulate():
    """Run a specific simulation script."""
    sim_type = request.form.get('type')
    target = "http://localhost"  # We attack ourself (Stage A Apache server)

    # UPDATED: Added 'brute' mapping
    script_map = {
        'sqli': 'simulate_sqli.py',
        'xss': 'simulate_xss.py',
        'flood': 'simulate_flood.py',
        'brute': 'simulate_bruteforce.py'
    }

    script_name = script_map.get(sim_type)

    if not script_name:
        return jsonify({'output': 'Error: Unknown simulation type'}), 400

    script_path = os.path.join(OFFENSE_DIR, script_name)

    # Check if script exists
    if not os.path.exists(script_path):
        return jsonify({'output': f'Error: Script {script_name} not found in {OFFENSE_DIR}'}), 404

    try:
        # Run the python script safely
        # Note: We pass --target, but your brute/flood scripts might ignore it
        # if they hardcoded the URL. That is fine for this demo.
        result = subprocess.run(
            ['python3', script_path, '--target', target],
            capture_output=True, text=True, timeout=15
        )
        output = result.stdout + result.stderr
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'output': f'Execution failed: {str(e)}'}), 500


@app.route('/logs')
def get_logs():
    """Read the last 20 lines of Suricata logs."""
    try:
        # Using 'tail' command is often faster/safer for live logs than reading the whole file
        result = subprocess.run(['tail', '-n', '20', SURICATA_LOG], capture_output=True, text=True)
        return jsonify({'logs': result.stdout})
    except Exception as e:
        return jsonify({'logs': f'Error reading logs: {str(e)}'})


if __name__ == '__main__':
    # Listen on all interfaces so you can access it from outside
    app.run(host='0.0.0.0', port=5001, debug=True)
