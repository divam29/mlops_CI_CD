from flask import Flask, request

app = Flask(__name__)
# Creates the flask application object
# __name is a special python variable and is used by flask to search 
#    for the various files which is there

@app.route("/") #used to create mapping from URL to python function
def hello():
    return "Welcome to MLOps, I hope you are excited!" 

@app.route("/ping")
def pinging():
    return "Hello, this is ping"

@app.route("/user/<username>", methods = ["GET"])
def show_user_name(username):
    return f'Hi {username}. Welcome to MLOps'

@app.route("/add", methods = ["POST"])
def add_numbers():
    data = request.get_json() #get JSON body
    num1 = data["num1"]
    num2 = data["num2"]
    return {"sum" : num1 + num2}


if __name__=="__main__":
    app.run(debug=True)
# app.run(port = 8080, debug = True) if you want to change the port (default is 5000)