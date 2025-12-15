from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    nu = datetime.now()
    if nu.hour < 16:
        tidstekst = "Klokken er før 16"
    else:
        tidstekst = "Klokken er efter 16"
    return render_template("index.html", tidstekst=tidstekst)

if __name__ == "__main__":
    app.run(debug=True)
