# # from flask import Flask, render_template, request
# # import mysql.connector
# #
# # app = Flask(__name__)
# #
# # # Connect to MySQL
# # connection = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     passwd="2003",
# #     database="registration_db"
# # )
# #
# # cursor = connection.cursor()
# #
# #
# # @app.route('/')
# # def home():
# #     return render_template('form.html')
# #
# #
# # @app.route('/register', methods=['POST'])
# # def register():
# #
# #     name = request.form.get('name')
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     mobile = request.form.get('mobile')
# #
# #     # Check whether email already exists
# #     cursor.execute(
# #         "SELECT * FROM users WHERE email = %s",
# #         (email,)
# #     )
# #
# #     if cursor.fetchone():
# #         return "Email already registered!"
# #
# #     # Insert data into database
# #     cursor.execute(
# #         """
# #         INSERT INTO users (name, email, password, mobile)
# #         VALUES (%s, %s, %s, %s)
# #         """,
# #         (name, email, password, mobile)
# #     )
# #
# #     connection.commit()
# #
# #     return "Registration Successful!"
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True, port=9000)
#
#
# from flask import Flask, render_template, request
# import mysql.connector
# app = Flask(__name__)
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2003",
#     database="store"
# )
# cursor = connection.cursor()
# @app.route("/add-note", methods=["GET", "POST"])
# def add_note():
#
#     if request.method == "POST":
#
#         title = request.form.get("title")
#         notes = request.form.get("notes")
#
#         if not title or not notes:
#             return "Title and notes are required"
#
#         cursor.execute(
#             """INSERT INTO notes (title, notes) VALUES (%s, %s)""",
#             (title, notes)
#         )
#
#         connection.commit()
#
#         return "Note added successfully"
#
#     return render_template("add_note.html")
# if __name__ == "__main__":
#     app.run(debug=True, port=9000)

#
# from flask import Flask,jsonify
# app=Flask(__name__)
# @app.route("/student")
# def student():
#     data={
#         "id":1,
#         "name":"Ravi",
#         "course":"python"
#     }
#     return jsonify(data)
# @app.route("/students")
# def students():
#     data=[
#         {
#             "id":1,"name":"Ravi",
#         },
#         {
#             "id":2,"name":"Priya",
#         },
#         {
#             "id":3,"name":"kiran",
#         }
#     ]
#     return jsonify(data)
# app.run(debug=True)
# if __name__=="__main__":
#     app.run(debug=True)

# from flask import Flask,jsonify
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return jsonify({
#         "message": "Hello World"
#     })
# app.run(debug=True)


from flask import Flask, make_response, request
app = Flask(__name__)
@app.route('/')

def home():
    return """
    <h1>Cookie example!</h1>
    <a href="/set-cookie">Set Cookie</a><br>
    <a href="/get-cookie">Get Cookie</a><br>
    <a href="/delete-cookie">Delete Cookie</a>
    
    """

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie has been set")
    response.set_cookie('username', 'Charan', max_age=600,httponly=True,samesite="lax")
    response.set_cookie('city', 'vizag',max_age=600,httponly=True,samesite="lax")
    return response
    response.set_cookie('city', 'vizag')
    return response
@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    city = request.cookies.get('city')
    return f"Welcome! {username}  from {city}"

@app.route('/delete-cookie')
def delete_cookie():
    response = make_response("Cookie has been deleted")
    response.delete_cookie('username')
    return response

app.run(debug=True)
