from flask import *

app = Flask(__name__)


@app.route('/')
def mocha():
    return render_template("mocha.html")


if __name__ == '__main__':
    app.run()
