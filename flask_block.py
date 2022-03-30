from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/test1")
def test1():
    return render_template('test1.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')

if __name__ == '__main__':
    app.run(debug=True)    