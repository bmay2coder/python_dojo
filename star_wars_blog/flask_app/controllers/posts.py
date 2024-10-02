from flask import request, redirect, session

from flask_app.models.post import Post
from flask_app.models import comment

from flask_app import app

@app.route('/star_wars/posts/new', methods=["POST"])
def new_post():
    data = {
        "content": request.form["content"],
        "user_id": request.form["user_id"]
    }

    if not Post.validate_post(data):
        session['data'] = data
        return redirect('/star_wars/blog')

    Post.save(data)
    return redirect('/star_wars/blog')

@app.route("/star_wars/posts/<int:id>/delete")
def delete_post(id):
    Post.delete(id)
    return redirect('/star_wars/blog')

@app.route('/star_wars/posts/comment', methods=["POST"])
def new_comment():
    data = {
        "comment_text": request.form["comment_text"],
        "user_id": request.form["user_id"],
        "post_id": request.form["post_id"]
    }

    comment.Comment.save(data)
    return redirect('/star_wars/blog')