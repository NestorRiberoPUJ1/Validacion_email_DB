from flask_app.config.mysqlconnection import connectToMySQL
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:

    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]

    @classmethod
    def mostrarTodos(cls):
        query="SELECT * FROM email_schema.emails"
        results=connectToMySQL("email_schema").query_db(query)
        emails=[]
        for x in results:
            emails.append(cls(x))
        return emails

    @classmethod
    def save(cls,form):
        query="INSERT INTO email_schema.emails (email) VALUES (%(email)s)"
        result=connectToMySQL("email_schema").query_db(query,form)
        return result

    @staticmethod
    def disponibilidad(user):
        query="SELECT * FROM email_schema.emails WHERE email = %(email)s"
        result=connectToMySQL("email_schema").query_db(query,user)
        if (len(result)<1):
            return True
        else:
            return False