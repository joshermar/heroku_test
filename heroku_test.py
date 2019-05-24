import logging
from flask import Flask, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    logging.debug('****TEST LOG MESSAGE****')
    return render_template("about.html", title="about")


if __name__ == '__main__':
    app.run(debug=True)
