from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/live")
def live():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 8080))
    db_user = os.environ.get("DB_USER", "undefined")
    db_pass = os.environ.get("DB_PASS", "undefined")
    timeout = os.environ.get("ORDER_PROCESS_TIMEOUT", "30")

    print(f"Starting orders-service on port {port}")
    print(f"DB_USER: {db_user}")
    print(f"DB_PASS: {db_pass}")
    print(f"ORDER_PROCESS_TIMEOUT: {timeout}")

    app.run(host="0.0.0.0", port=port)
