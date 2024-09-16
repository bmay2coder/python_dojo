from flask import render_template, request, redirect, session
from datetime import datetime

from flask_app.models.user import User

from flask_app import app

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route("/users/<int:id>")
def view_user(id):
    user = User.get_by_id(id=id)
    print(user)
    return render_template("view_user.html", user=user)

@app.route('/users/new', methods=["GET","POST"])
def create_user():
    if request.method == 'GET':
        
        if session.get('data'):
            data = session['data']
        else:
            data = {
                "fname": "",
                "lname": "",
                "program": ""
            }
        return render_template("new_user.html", data=data)

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    
    if not User.validate_user(data):
        session['data'] = data
        return redirect('/users/new')
    
    user_id = User.save(data)
    return redirect('/users/'+str(user_id))

@app.route('/users/<int:id>/edit', methods=["GET","POST"])
def edit_user(id):
    user = User.get_by_id(id=id)
    if request.method == 'GET':
        return render_template("edit_user.html", user=user, date=datetime.now())

    User.update(request.form)
    return redirect('/users/'+str(id))

@app.route("/users/<int:id>/delete")
def delete_user(id):
    User.delete(id)
    return redirect('/')