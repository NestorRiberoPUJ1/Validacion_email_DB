from flask import Flask, redirect,render_template,flash,session,request
from flask_app import app
from flask_app.models.user import Email

@app.route("/")
def root():

    return render_template("index.html")


@app.route("/create",methods=["POST"])
def create():

    if(Email.disponibilidad(request.form)):
        session["email"]=request.form["email"]
        Email.save(request.form)
        return redirect("/success")
    else:
        flash("El correo ya está en uso")
        return redirect("/")

@app.route("/success")
def success():
    emails = Email.mostrarTodos()
    return render_template("success.html",emails=emails)