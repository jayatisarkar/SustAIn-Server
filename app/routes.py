from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET", "POST"])
def lookup_barcode():
    pass


if __name__ == "__main__":
    app.run(debug=True)