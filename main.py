from flask import Flask,redirect,render_template,url_for,request
import database as db
import routes


app=Flask(__name__)



@app.route("/",methods=["GET"])
def start():
    return routes.handleHome()


@app.route("/home",methods=['GET'])
def home():
    return routes.handleHome()




@app.route("/login",methods=['POST','GET'])
def login():
    return routes.handleLogin()


# Remaining: Handle Signup, Uploading, viewing files












if __name__=="__main__":
    app.run(port=5000,debug=True)