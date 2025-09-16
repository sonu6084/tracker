from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv("data.csv")
    return df.to_dict(orient="records")

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
