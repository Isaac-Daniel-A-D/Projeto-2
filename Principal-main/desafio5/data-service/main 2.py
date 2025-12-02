from flask import Flask, jsonify, request
import jwt
from functools import wraps

app = Flask(__name__)

SHARED_SECRET = "my_super_secure_project_key_2025"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"message": "Token mal formatado"}), 401
        
        if not token:
            return jsonify({"message": "Token ausente"}), 401

        try:
            data = jwt.decode(token, SHARED_SECRET, algorithms=["HS256"])
            request.current_user = data['sub']
            request.user_role = data['role']
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated

@app.route("/secure/reports")
@token_required
def get_secure_reports():
    user = request.current_user
    role = request.user_role
    
    secret_content = [
        {"id": 1, "report": "Vendas 2025", "status": "Confidencial"},
        {"id": 2, "report": "Salários TI", "status": "Restrito"}
    ]

    return jsonify({
        "message": f"Olá {user}, seu nível de acesso é {role}",
        "data": secret_content
    })

@app.route("/")
def health_check():
    return jsonify({"status": "Data Service Online"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)