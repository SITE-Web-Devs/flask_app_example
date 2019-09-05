from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("typer.html")

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/hacker')
def hacker():
    return render_template("hacker.html")

@app.route('/check/<x>/<y>')
def checker(x, y):
    return render_template("checkers.html", some_width = int(x), some_height = int(y))

if __name__ =="__main__":
    app.run(debug=True)
