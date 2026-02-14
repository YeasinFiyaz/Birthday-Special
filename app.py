import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/photo')
def photo():
    return render_template("photo.html")

@app.route('/final')
def final():
    return render_template("final.html")

if __name__ == "__main__":
    # Get the port from Render environment variable, fallback to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so Render can access it
    app.run(host="0.0.0.0", port=port)
