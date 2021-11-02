from flask import Flask, render_template
from flask import session

app = Flask(__name__, static_folder="./static")

@app.route('/')
@app.route('/index.html')
def index():
  return render_template("index.html")

@app.route('/tin_tuc')
@app.route('/tin_tuc.html')
def tin_tuc():
    return render_template("tin_tuc.html")

@app.route('/tiem_chung')
@app.route('/tiem_chung.html')
def tiem_chung():
  return render_template("tiem_chung.html")

if __name__ == "__main__":
  app.run(port = 5050)
