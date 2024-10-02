from flask import render_template, request, redirect, session, flash

from flask_app.models.user import User

from flask_app.models import post, comment

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def root():
    return redirect('/star_wars')

@app.route("/star_wars")
def index():
    if session.get('data'):
        data = session['data']
    else:
        data = {
            "fname": "",
            "lname": "",
            "email": "",
            "password": "",
            "confirm": ""
        }
    return render_template("index.html", data=data)

@app.route('/star_wars/register/user', methods=["POST"])
def register():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm": request.form["confirm"]
    }

    if not User.validate_user(data):
        session['data'] = data
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['password']=pw_hash
    
    user_id = User.save(data)
    
    if session.get('data'):
        session.pop('data')
    session['user_id'] = user_id
    return redirect('/star_wars/blog')

@app.route('/star_wars/login/user', methods=["POST"])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }

    if not User.validate_login(data):
        session['data'] = data
        return redirect('/')
    
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/star_wars/blog')

@app.route('/star_wars/blog')
def show_blog():
    if not session.get('user_id'):
        return redirect('/logout')
    
    all_posts = post.Post.get_posts_with_users()
    
    for i in range(len(all_posts)):
        all_posts[i].comments = comment.Comment.get_comments_from_post(all_posts[i].id)

    user = User.get_by_id(session['user_id'])
    return render_template("blog.html", user=user, all_posts=all_posts)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')