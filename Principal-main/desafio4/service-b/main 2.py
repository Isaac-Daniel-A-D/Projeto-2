from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

EMPLOYEE_SERVICE_URL = os.environ.get("EMPLOYEE_SERVICE_URL", "http://employees-api:8000/employees")

@app.route("/print-badges")
def print_badges():
    try:
        response = requests.get(EMPLOYEE_SERVICE_URL, timeout=5)
        response.raise_for_status()
        employees = response.json()
    except Exception as e:
        return jsonify({"error": "Employee Service Unavailable", "details": str(e)}), 503

    badges = []
    for emp in employees:
        badge_format = f"[ID: {emp['id']}] {emp['name'].upper()} // {emp['department']} Dept."
        badges.append({
            "employee_id": emp['id'],
            "badge_preview": badge_format,
            "status": "Ready to Print"
        })
    
    return jsonify(badges)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)