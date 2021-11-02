from flask import Flask, render_template
from flask import session

ungdung = Flask(__name__, static_folder="./static")

@ungdung.route('/')
@ungdung.route('/index.html')
def index():
  return render_template("index.html")

@ungdung.route('/tin_tuc')
@ungdung.route('/tin_tuc.html')
def tin_tuc():
    return render_template("tin_tuc.html")

@ungdung.route('/tiem_chung')
@ungdung.route('/tiem_chung.html')
def tiem_chung():
  return render_template("tiem_chung.html")

if __name__ == "__main__":
  ungdung.run(port = 5050)
