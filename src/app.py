from flask import Flask
from compute_failure_rate import failure_rate

app = Flask(__name__)

@app.route("/")
def home():
    result = failure_rate(100, 5)
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
