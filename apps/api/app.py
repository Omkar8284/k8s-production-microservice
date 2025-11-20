from flask import Flask, jsonify
import socket
import os
import math

app = Flask(__name__)

# -----------------------------
# CPU Stress Function
# -----------------------------
def cpu_stress():
    # This loop intentionally burns CPU to simulate heavy load
    x = 0
    for i in range(1_000_000):   # Increase to 3M/5M if you want more CPU usage
        x += math.sqrt(i)
    return x


# -----------------------------
# Root endpoint
# -----------------------------
@app.route("/")
def home():
    cpu_stress()  # <-- This is what triggers HPA/KEDA scaling
    return jsonify(
        message="Hello from mc-api",
        node=os.environ.get("NODE_NAME", "unknown"),
        hostname=socket.gethostname()
    )


# -----------------------------
# Health endpoint
# -----------------------------
@app.route("/health")
def health():
    return jsonify(status="ok"), 200


# -----------------------------
# Flask server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
