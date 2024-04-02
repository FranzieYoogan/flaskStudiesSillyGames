import random
from flask import Flask, render_template, request
import flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm');

@app.route("/rockpaperscissors",methods = ['POST','GET'])
def rockPaperScissors():
    if(flask.request.method == "POST"):
        userAnswer = request.form['userAnswer'];
        randomValue = random.randint(0,2);
        if(randomValue == 0):
            answer = "rock";
        if(randomValue == 1):
            answer = "paper";
        if(randomValue == 2):
            answer = "scissors";
    
        return render_template('rockpaperscissors.htm',answer = answer,userAnswer = userAnswer);
    else:
        return render_template('rockpaperscissors.htm');

if __name__ == '__main__':  
   app.run(debug=True)