from flask import redirect,render_template,url_for,request,make_response
import controllers as cont


def handleLogin():
    if (request.method=='POST'):
        return handleLoginPOST()
    else:
        return handleLoginGET()


def handleLoginPOST():
    username=request.form['username']
    password=request.form['password']
    res=cont.authenticate(username,password)  #res=(id,name)
    if res==None:
        response = make_response("Wrong username or password", 401) 
        return response
    else:
        token=cont.createJWT(username,res)
        response = make_response(redirect(url_for("home")))  
        response.set_cookie('jwt_token', token, httponly=True)
        return response
    

def handleLoginGET():
    uname=cont.verifyCookie()
    if(uname!=None):# step1: cookie verification if verified
        return redirect(url_for("home"))
    else: # step2: not verified/no cookie
        return render_template("login.html")




def handleHome():
    uname=cont.verifyCookie()
    if uname==None:
        return redirect(url_for("login"))
    else:
        return render_template("home.html",Name=uname)