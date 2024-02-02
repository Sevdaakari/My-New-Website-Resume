from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)
#test
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=False, port=5006)