from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def home():
    nu = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", klokkeslaet=nu)

if __name__ == "__main__":
    app.run(debug=True)
