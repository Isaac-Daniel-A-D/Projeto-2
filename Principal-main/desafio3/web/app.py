import os
import time
from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'app_data')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASSWORD', 'pass')
REDIS_HOST = os.getenv('REDIS_HOST', 'cache')

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

@app.route("/")
def visit():
    results = {}

    try:
        r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
        hits = r.incr('visit_count')
        results['redis_cache'] = f"Updated! Total hits: {hits}"
    except Exception as e:
        results['redis_cache'] = f"Error: {str(e)}"

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS access_log (id SERIAL PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
        cur.execute("INSERT INTO access_log DEFAULT VALUES;")
        conn.commit()
        cur.close()
        conn.close()
        results['postgres_db'] = "Log entry saved successfully."
    except Exception as e:
        results['postgres_db'] = f"Error: {str(e)}"

    return jsonify({
        "status": "Service Operational",
        "actions": results
    })

if __name__ == "__main__":
    time.sleep(3) 
    app.run(host="0.0.0.0", port=5000)