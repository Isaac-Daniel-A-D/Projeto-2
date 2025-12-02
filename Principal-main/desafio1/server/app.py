from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/status")
def server_status():
    container_id = socket.gethostname()
    return jsonify({
        "service": "api-server",
        "status": "online",
        "container": container_id
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Server iniciated on port {port}")
    app.run(host="0.0.0.0", port=port)