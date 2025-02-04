"""Simple Flask Server for testing vscode dev-container"""

from flask import Flask

app = Flask("Simple Flask App")

@app.route("/")
def hello():
    return "Hello world! Your simple flask app is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)