from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user

class Post:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.poster = None
        self.comments = []
    DB = "star_wars_blog"

    @classmethod
    def validate_post(cls, post):
        is_valid = True
        if len(post['content'])<=0:
            flash("Post must not be blank")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.DB).query_db(query)
        posts = []
        for post in results:
            posts.append(cls(post))
        return posts

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (content, user_id, created_at, updated_at) VALUES (%(content)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET content=%(content)s, updated_at=%(updated_at)s WHERE id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM posts WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, {"id":id})
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM posts WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {"id":id})
        return cls(results[0])
    
    @classmethod
    def get_posts_with_users(cls):

        query = "SELECT * FROM posts LEFT JOIN users ON users.id = user_id"
        results = connectToMySQL(cls.DB).query_db(query)

        if len(results) == 0:
            return results
        all_posts = []

        for row in results:
            posting_user = user.User({
                "id": row["user_id"],
                "email": row["email"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
                "password": row["password"]
            })

            new_post = Post({
                "id": row["id"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user_id": posting_user.id,
            })
            new_post.poster = posting_user

            all_posts.append(new_post)
        return all_posts
