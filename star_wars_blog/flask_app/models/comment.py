from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import post, user

class Comment:
    def __init__( self , data ):
        self.id = data['id']
        self.comment_text = data['comment_text']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.commenter = None
    DB = "star_wars_blog"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (comment_text, user_id, post_id) VALUES (%(comment_text)s, %(user_id)s, %(post_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_comments_from_post(cls, post_id):

        query = """
            SELECT * FROM posts 
            LEFT JOIN users ON users.id = user_id 
            LEFT JOIN comments ON comments.post_id = posts.id 
            WHERE posts.id = %(post_id)s
        """
        results = connectToMySQL(cls.DB).query_db(query, {"post_id":post_id})

        if len(results) == 0:
            return results
        
        comments = []
        
        for row in results:
            if row["comments.id"]:
                this_comment = Comment({
                    "id": row["id"],
                    "comment_text": row["comment_text"],
                    "user_id": row['comments.user_id'],
                    "post_id": post_id
                })

                this_comment.commenter = user.User.get_by_id(row['comments.user_id'])

                comments.append(this_comment)
        return comments
