from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    sent = False
    if request.method == "POST":
        # Demo form: no email is sent and no information is stored.
        sent = True
    return render_template("index.html", year=datetime.now().year, sent=sent)

if __name__ == "__main__":
    app.run(debug=True)
