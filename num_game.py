from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)
app.secret_key = '0331'


@app.route('/')
def home():
    session["number"]= int(random.random () * 100)
    return render_template("num_game.html")

@app.route("/guess_again")
def guess_again():
    if session["answer"]== "Correct":
        color= "green"
    else:
        color = "red"
    return render_template("num_game.html", answer=session["answer"], color=color)

@app.route("/guess", methods=["POST"])
def guess():
    if session["number"] == int(request.form["number"]):
        session["answer"] = "Correct"
    elif session["number"] > int(request.form["number"]):
        session["answer"] = "Too Low"
    else:
        session["answer"] = "Too High"
    return redirect("/guess_again")


if __name__=="__main__":
    app.run(debug=True)