from flask import Flask, render_template

app = Flask(__name__) #Creating a flask object

#LIST OF SHOWS
Shows =["Jojo's Bizarre Adventure", "One Piece", "Haikyuu", "Breaking Bad", "Game of Thrones"]

@app.route("/") #connecting the flask to the actual function below... the / is the base url for the entire website

def index(): #Simple Function
    return  render_template("index.html", len = len(Shows), Shows = Shows)  # here we link our python code to html/flask

app.run(use_reloader = True, debug = True)