import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('homepage.html')

@app.route("/helpme")
def helpme():
    return render_template('helpme.html')

@app.route("/finaid")
def finaid():
    return render_template('finaid.html')

@app.route("/schoolfind")
def schoolfind():
    return render_template('schoolfind.html')

@app.route("/stdtest")
def stdtest():
    return render_template('stdtest.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)