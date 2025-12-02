import datetime
import sys
from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

JWT_SECRET = "my_super_secure_project_key_2025"

@app.route("/api/login", methods=["POST"])
def login():
    credentials = request.json
    if not credentials or 'username' not in credentials or 'password' not in credentials:
        return jsonify({"error": "Credenciais incompletas"}), 400

    user = credentials['username']
    pwd = credentials['password']

    if pwd != "123456":
        print(f"[AUTH] Falha de login para: {user}", file=sys.stderr)
        return jsonify({"error": "Acesso negado"}), 403

    payload = {
        "sub": user,
        "role": "admin" if user == "admin" else "viewer",
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    encoded_token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    print(f"[AUTH] Token gerado para: {user}", file=sys.stdout)
    
    return jsonify({
        "access_token": encoded_token,
        "token_type": "Bearer",
        "expires_in": 3600
    })

@app.route("/api/verify", methods=["GET"])
def get_public_key():
    return jsonify({"secret_check": "active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)