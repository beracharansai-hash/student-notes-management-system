'''
render templete()
------------------
the module is used from acess the .htmml files from the template folder

template variable
-----------------
A variable defined in the function


from flask import Flask, render_template
SNM = Flask(__name__)
@SNM.route('/')
def home():
    name="sam"
    age=20
    batch="pfs-003"
    return render_template('home.html',name =name , age =age, batch=batch)

if __name__ == '__main__':
    SNM.run(debug=True,port=9000)
'''
'''
from flask import Flask, render_template
SNM = Flask(__name__)
@SNM.route('/result')
def home():
    marks = 85
    return render_template('result.html',marks = marks)

if __name__ == '__main__':
    SNM.run(debug=True,port=9000)


from flask import Flask, render_template
SNM = Flask(__name__)
@SNM.route('/result')
def students():
    students=['sam','charan','mohi','kundhan']
    return render_template('students.html',students = students)
if __name__ == '__main__':
    SNM.run(debug=True,port=9000)'''
# from flask import Flask, render_template, request
#
# SNM = Flask(__name__)
# @SNM.route('/')
# def home():
#     return render_template('homepag.html')
# @SNM.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         name=request.form['name']
#         email=request.form['email']
#         password=request.form['password']
#     print(name)
#     print(email)
#     print(password)
# if __name__ == '__main__':
#     SNM.run(debug=True,port=9000)

# from flask import Flask, render_template
# SNM = Flask(__name__)
# @SNM.route('/result')
# def age():
#     age = 40
#     return render_template('result.html',age = age)
#
# if __name__ == '__main__':
#     SNM.run(debug=True)


# from flask import Flask, render_template, request
#
# SNM = Flask(__name__)
# @SNM.route('/')
# def home():
#    return render_template('homepag.html')
# @SNM.route('/register', methods=['GET', 'POST'])
# def register():
#      if request.method == 'POST':
#         name=request.form['name']
#         email=request.form['email']
#         password=request.form['password']
#      print(name)
#      print(email)
#      print(password)
# if __name__ == '__main__':
#   SNM.run(debug=True,port=9000)

# import mysql.connector
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2003",
#     database="pfs3"
# )
# cursor = connection.cursor()
# cursor.execute("select * from students")
# data_=cursor.fetchall()
# print(data_)
#
#
# from flask import Flask, render_template, request
# import mysql.connector
# connection=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2003",
#     database="snm_db"
# )
# cursor=connection.cursor()
# SNM=Flask(__name__)
# @SNM.route('/')
# def home():
#     return "Welcome to registration system"
# @SNM.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         mobile=request.form.get('mobile')
#         password = request.form.get('password')
#
#         if not name or not email or not password:
#             return "ALL FIELDS ARE REQUIRED."
#
#         cursor.execute(
#             """
#             SELECT *
#             FROM users
#             WHERE email = %s
#             """,
#             (email,)
#         )
#
#         Duplicate_mail = cursor.fetchone()
#
#         if Duplicate_mail:
#             return "Email already exists"
#
#         cursor.execute(
#             """
#             INSERT INTO users (name, email,Mobile ,password)
#             VALUES (%s, %s, %s,%s)
#             """,
#             (name, email,mobile, password)
#         )
#
#         connection.commit()
#
#         return "Registration Successful"
#         connection.commit()
#         return "Registration Successful"
#     return render_template('SNMregister.html')
# if __name__ == '__main__':
#     SNM.run(debug=True,port=9000)
#
#



#
#
# import bcrypt
# password="sai12345678@"
# hashed_password=(bcrypt.hashpw
#                  (password.encode
#                   ("utf-8"),
#                               bcrypt.gensalt()
#                               ))
# print(hashed_password)
'''
from flask import Flask, render_template,request,url_for,session,redirect
import mysql.connector
import bcrypt

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",
    database="snm_db"
)

cursor = connection.cursor()

SNM = Flask(__name__)
SNM.secret_key="secret-key"
@SNM.route('/')
def home():
    return "Welcome to registration system"

@SNM.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')

        password = request.form.get('password')

        if not name or not email or not password:
            return "ALL FIELDS ARE REQUIRED."

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        Duplicate_mail = cursor.fetchone()

        if Duplicate_mail:
            return "Email already exists"
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        hashed_password = hashed_password.decode("utf-8")
        cursor.execute(
            """
            INSERT INTO users (name, email,password)
            VALUES (%s, %s, %s)
            """,
            (name, email,hashed_password)
        )

        connection.commit()

        return "Registration Successful"

    return render_template('SNMregister.html')

@SNM.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "ALL FIELDS ARE REQUIRED."
        cursor.execute(
            '
            SELECT * FROM users
            WHERE email = %s',
            (email,)
            )
        user=cursor.fetchone()
        if not user:
            return "invalid email or password"
        stored_password =user[3]
        if isinstance(stored_password, str):
            stored_password = stored_password.encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"),stored_password):
            session["user_id"] = user[0]
            session["email"] = user[2]
            return redirect(url_for("dashboard"))
        return "invalid email or password"
    return render_template('SNMlogin.html')


@SNM.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("SNMdashboard.html")
@SNM.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == '__main__':
    SNM.run(debug=True, port=9000)
    


from itsdangerous import URLSafeSerializer, serializer

serializer=URLSafeSerializer('secret-key')
token=serializer.dumps('beracharansai@gmail.com')
print(token)
data=serializer.loads(token)
print(data)
'''
from flask import Flask, render_template, request, url_for, session, redirect, send_file
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import mysql.connector
import os
from werkzeug.utils import secure_filename
import bcrypt
import flask_excel

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",
    database="snm_db"
)
cursor = connection.cursor()

app = Flask(__name__)
app.secret_key = "secret-key"
flask_excel.init_excel(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
ALLOWED_EXTENSIONS = {"txt","pdf","png","jpg","jpeg","gif"}

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/")
def home():
    return "Welcome to registration system"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if not name or not email or not password:
            return "ALL FIELDS ARE REQUIRED."
        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = %s
            """,
            (email,)
        )
        duplicate_mail = cursor.fetchone()
        if duplicate_mail:
            return "Email already exists"
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        hashed_password = hashed_password.decode("utf-8")
        cursor.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
            """,
            (name, email, hashed_password)
        )
        connection.commit()
        return "Registration Successful"
    return render_template("SNMregister.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            return "ALL FIELDS ARE REQUIRED."

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()
        if not user:
            return "invalid email or password"
        stored_password = user[3]
        if isinstance(stored_password, str):
            stored_password = stored_password.encode("utf-8")
        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):
            session["user_id"] = user[0]
            session["email"] = user[2]
            return redirect(
                url_for("dashboard")
            )
        return "invalid email or password"
    return render_template("SNMlogin.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template(
        "SNMdashboard.html"
    )

def generate_token(email):
    serializer = URLSafeTimedSerializer(
        app.config["SECRET_KEY"]
    )
    token = serializer.dumps(
        email,
        salt="password-reset"
    )
    return token


def verify_reset_token(token):
    serializer = URLSafeTimedSerializer(
        app.config["SECRET_KEY"]
    )
    try:
        email = serializer.loads(
            token,
            salt="password-reset",
            max_age=300
        )
        return email
    except SignatureExpired:
        return "expired"
    except BadSignature:
        return "invalid"

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        if not email:
            return "Email is required"
        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()
        if not user:
            return "Invalid email"
        token = generate_token(email)
        reset_link = url_for(
            "reset_password",
            token=token,
            _external=True
        )
        print("\nPASSWORD RESET LINK:")
        print(reset_link)
        print()
        return "Password reset link generated. Check the VS Code terminal."
    return render_template("SNMforgotpassword.html")


@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    email = verify_reset_token(token)
    if email == "expired":
        return "Password reset link has expired. Please request a new link."

    # Invalid token
    if email == "invalid":
        return "Invalid password reset link."
    if request.method == "POST":
        new_password = request.form.get("password")
        if not new_password:
            return "Password is required"
        hashed_password = bcrypt.hashpw(
            new_password.encode("utf-8"),
            bcrypt.gensalt()
        )

        hashed_password = hashed_password.decode("utf-8")
        cursor.execute(
            """
            UPDATE users
            SET password = %s
            WHERE email = %s
            """,
            (hashed_password, email)
        )

        connection.commit()

        return redirect(
            url_for("login")
        )

    return render_template(
        "SNMresetpassword.html"
    )



@app.route("/add-note", methods=["GET", "POST"])
def add_note():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        if not title or not content:
            return "Title and content are required."

        user_id = session["user_id"]

        cursor.execute(
            """
            INSERT INTO notes
            (user_id, title, content)
            VALUES (%s, %s, %s)
            """,
            (user_id, title, content)
        )

        connection.commit()

        return redirect(
            url_for("view_notes")
        )

    return render_template(
        "SNMaddNote.html"
    )

@app.route("/notes")
def view_notes():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        """
        SELECT
            note_id,
            user_id,
            title,
            content,
            created_at,
            updated_at
        FROM notes
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    notes = cursor.fetchall()

    return render_template(
        "SNMnotes.html",
        notes=notes
    )



@app.route("/note/<int:note_id>")
def view_single_note(note_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    cursor.execute(
        """
        SELECT
            note_id,
            user_id,
            title,
            content,
            created_at,
            updated_at
        FROM notes
        WHERE note_id = %s
        AND user_id = %s
        """,
        (note_id, user_id)
    )

    note = cursor.fetchone()

    if not note:
        return "Note not found or you do not have permission to view it."

    return render_template("SNMviewNote.html",note=note)

@app.route("/update-note/<int:note_id>", methods=["GET", "POST"])
def update_note(note_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    cursor.execute(
        """
        SELECT
            note_id,
            user_id,
            title,
            content,
            created_at,
            updated_at
        FROM notes
        WHERE note_id = %s
        AND user_id = %s
        """,
        (note_id, user_id)
    )

    note = cursor.fetchone()

    if not note:
        return "Note not found or you do not have permission to update it."
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if not title or not content:
            return "Title and content are required."
        cursor.execute(
            """
            UPDATE notes
            SET
                title = %s,
                content = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE note_id = %s
            AND user_id = %s
            """,
            (title, content, note_id, user_id)
        )

        connection.commit()

        return redirect(
            url_for(
                "view_single_note",
                note_id=note_id
            )
        )

    return render_template(
        "SNMupdateNote.html",
        note=note
    )



@app.route("/delete-note/<int:note_id>", methods=["POST"])
def delete_note(note_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        """
        DELETE FROM notes
        WHERE note_id = %s
        AND user_id = %s
        """,
        (note_id, user_id)
    )

    connection.commit()

    return redirect(
        url_for("view_notes")
    )


@app.route("/upload-file/<int:note_id>", methods=["GET", "POST"])
def upload_file(note_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    # Check whether note belongs to logged-in user
    cursor.execute(
        """
        SELECT note_id
        FROM notes
        WHERE note_id = %s
        AND user_id = %s
        """,
        (note_id, user_id)
    )

    note = cursor.fetchone()

    if not note:
        return "Note not found or unauthorized access."

    if request.method == "POST":

        file = request.files.get("file")

        if not file:
            return "No file selected."

        if file.filename == "":
            return "No file selected."

        if not allowed_file(file.filename):
            return "File type not allowed."

        # Make filename safe
        filename = secure_filename(file.filename)

        # Check duplicate file for this note
        cursor.execute(
            """
            SELECT file_id
            FROM filedata
            WHERE note_id = %s
            AND file_name = %s
            """,
            (note_id, filename)
        )

        existing_file = cursor.fetchone()

        if existing_file:
            return "File with the same name already exists for this note."

        # Create FULL physical file path
        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        # Save physical file
        file.save(filepath)

        # Save file information in database
        cursor.execute(
            """
            INSERT INTO filedata
            (
                note_id,
                file_name,
                file_path
            )
            VALUES (%s, %s, %s)
            """,
            (
                note_id,
                filename,
                filepath
            )
        )

        connection.commit()

        return "File uploaded successfully."

    return render_template(
        "SNMuploadfile.html",
        note_id=note_id
    )



@app.route("/files")
def view_all_files():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        """
        SELECT
            filedata.file_id,
            filedata.note_id,
            filedata.file_name,
            filedata.file_path,
            filedata.uploaded_at,
            notes.title
        FROM filedata
        JOIN notes
        ON filedata.note_id = notes.note_id
        WHERE notes.user_id = %s
        ORDER BY filedata.uploaded_at DESC
        """,
        (user_id,)
    )

    files = cursor.fetchall()

    return render_template(
        "SNMfiles.html",
        files=files
    )


@app.route("/view-file/<int:file_id>")
def view_file(file_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        """
        SELECT
            filedata.file_path
        FROM filedata
        JOIN notes
        ON filedata.note_id = notes.note_id
        WHERE filedata.file_id = %s
        AND notes.user_id = %s
        """,
        (file_id, user_id)
    )

    file = cursor.fetchone()

    if not file:
        return "File not found or unauthorized access."

    file_path = file[0]

    # Check physical file
    if not os.path.exists(file_path):
        return f"Physical file does not exist: {file_path}"

    # Open file in browser
    return send_file(
        file_path,
        as_attachment=False
    )



@app.route("/download-file/<int:file_id>")
def download_file(file_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        """
        SELECT
            filedata.file_path,
            filedata.file_name
        FROM filedata
        JOIN notes
        ON filedata.note_id = notes.note_id
        WHERE filedata.file_id = %s
        AND notes.user_id = %s
        """,
        (file_id, user_id)
    )

    file = cursor.fetchone()

    if not file:
        return "File not found or unauthorized access."

    file_path = file[0]
    file_name = file[1]

    # Check physical file
    if not os.path.exists(file_path):
        return f"Physical file does not exist: {file_path}"

    # Download file
    return send_file(
        file_path,
        as_attachment=True,
        download_name=file_name
    )



@app.route("/delete-file/<int:file_id>", methods=["POST"])
def delete_file(file_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    cursor.execute(
        """
        SELECT
            filedata.file_path,
            filedata.file_name,
            filedata.note_id
        FROM filedata
        JOIN notes
        ON filedata.note_id = notes.note_id
        WHERE filedata.file_id = %s
        AND notes.user_id = %s
        """,
        (file_id, user_id)
    )
    file = cursor.fetchone()
    if not file:
        return "File not found or unauthorized access."
    file_path = file[0]
    file_name = file[1]
    note_id = file[2]
    if os.path.exists(file_path):
        os.remove(file_path)
    cursor.execute(
        """
        DELETE FROM filedata
        WHERE file_id = %s
        """,
        (file_id,)
    )
    connection.commit()
    return redirect(url_for("view_all_files"))

@app.route("/search", methods=['GET', 'POST'])
def search():
    notes = []
    files = []

    if 'user_id' not in session:
        return redirect(url_for("login"))
    if request.method == 'POST':
        search_text = request.form.get("search","").strip()
        if not search_text:
            return "Please enter search text"
        user_id = session['user_id']
        search_value = "%" + search_text + "%"
        cursor.execute(
            """
            SELECT note_id, title, content, created_at
            FROM notes
            WHERE user_id = %s AND (title LIKE %s OR content LIKE %s)
            """,
            (user_id, search_value, search_value)
        )
        notes = cursor.fetchall()
        cursor.execute(
            """
            SELECT filedata.file_id,
            filedata.note_id,
            filedata.file_name,
            filedata.file_path,
            filedata.uploaded_at
            FROM filedata
            JOIN notes ON filedata.note_id = notes.note_id
            WHERE notes.user_id = %s AND (filedata.file_name LIKE %s OR notes.title LIKE %s)
            """,
            (user_id, search_value, search_value)
        )
        files = cursor.fetchall()
    return render_template("SNMsearch.html", notes=notes, files=files)
@app.route("/download-note-files-excel/<int:note_id>")
def download_note_files_excel(note_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    cursor.execute("""
        SELECT note_id, title
        FROM notes
        WHERE note_id = %s
        AND user_id = %s
    """,(note_id, user_id))
    note = cursor.fetchone()
    if not note:
        return "Note not found"

    cursor.execute("""
        SELECT note_id, title
        FROM notes
        WHERE note_id = %s
    """,(note_id,))

    files = cursor.fetchall()
    data=[["File ID", "File Name", "File Path", "Uploaded At"]]

    for file in files:
        data.append(list(file))

    return flask_excel.make_response_from_array(
        data,
        file_type="xlsx",
        file_name=f"{note[1]}_files.xlsx")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True,port=9000)