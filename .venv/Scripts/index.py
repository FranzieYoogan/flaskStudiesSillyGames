from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm');

@app.route("/rockpaperscissors")
def rockPaperScissors():
    return render_template('rockpaperscissors.htm');

if __name__ == '__main__':  
   app.run(debug=True)