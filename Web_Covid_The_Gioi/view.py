from flask import Flask
from flask import render_template

ungdung = Flask(__name__)

@ungdung.route('/')
def index():
   return render_template('index.html')

@ungdung.route('/trang1')
def trang1(name=None):
    return render_template('trang1.html')

@ungdung.route('/trang2')
def trang2(name=None):
    return render_template('trang2.html')

if __name__ == '__main__':
    ungdung.run(port=5555)