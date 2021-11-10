#Author: Bibek Itani
#Date: 11/08/21

from flask import Flask, render_template, request
import chatbot as inp
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello():
    return render_template("index.html")


@app.route("/", methods = ['POST'])
def submit():
    #HTML -> .py
    if request.method == "POST":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        #console
        print("Current time:", current_time)
        print(request.form)
        ##endsconsole
        questions = request.form["questions"]
        response = inp.chat(questions)
        print(response)

    #.py -> HTML
        return render_template("index.html", n = response, x = current_time, q = questions)
    

if __name__ == "__main__":
    app.run(debug = True)



#improved code

# from flask import Flask, render_template, request
# import chatbot as inp

# app = Flask(__name__)


# @app.route("/", methods = ['GET'])
# def hello():
#     return render_template("index.html")

    


# @app.route("/submit", methods = ['POST'])
# def submit():
#     #HTML -> .py
#     if request.method == "POST":
#         print(request.form)
#         questions = request.form["questions"]
#         response = inp.chat(questions)

#         print(response)

#     #.py -> HTML
#         return render_template("submit.html", n = response)
    

# if __name__ == "__main__":
#     app.run(debug = True)
