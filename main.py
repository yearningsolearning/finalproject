from flask import Flask, render_template, request, session, redirect, url_for, flash
import psycopg2
import re
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# def get_db_connection():
#     return psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='admin',
#         host='localhost',
#         port='5432'
#     )

def get_db_connection():
    return psycopg2.connect(
        dbname='final_dbms',
        user='final_dbms_user',
        password='kiyFsG55ZbMbw59HJi49ere5c8bOQBHf',
        host='dpg-cqq3a02j1k6c73da6nbg-a.oregon-postgres.render.com',
        port='5432'
     )

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@app.route("/")
def home():
    return render_template("home.html")

def get_semester_id(semester_name):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT semester_id FROM sem WHERE name = %s;", (semester_name,))
        semester = cursor.fetchone()
        
        if semester:
            return semester[0]
        else:
            cursor.execute("INSERT INTO sem (name) VALUES (%s) RETURNING semester_id;", (semester_name,))
            semester_id = cursor.fetchone()[0]
            connection.commit()
            return semester_id
            
    except Exception as e:
        print(f"Error: {e}")
        return None
        
    finally:
        cursor.close()
        connection.close()

def add_user(username, email, password, semester_name):
    semester_id = get_semester_id(semester_name)
    if semester_id is None:
        print("Failed to get semester ID.")
        return
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        insert_query = '''
            INSERT INTO "user" (username, email, password)
            VALUES (%s, %s, %s) RETURNING user_id;
        '''
        
        cursor.execute(insert_query, (username, email, password))
        user_id = cursor.fetchone()[0]

        cursor.execute('''
            INSERT INTO user_sem (user_id, semester_id) VALUES (%s, %s);
        ''', (user_id, semester_id))
        connection.commit()
        
        print("User added successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        connection.close()

@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        semester_name = request.form["semester"]

        add_user(username, email, password, semester_name)
        flash("Account created successfully!")
        return redirect(url_for("loginhello"))

    return render_template("sign.html")

@app.route("/loginhello", methods=["GET", "POST"])
def loginhello():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        semester_name = request.form["semester"]
        
        if is_valid_email(email):
            connection = get_db_connection()
            cursor = connection.cursor()

            try:
                cursor.execute("SELECT semester_id FROM sem WHERE name = %s;", (semester_name,))
                semester_result = cursor.fetchone()

                if semester_result:
                    semester_id = semester_result[0]
                else:
                    cursor.execute("INSERT INTO sem (name) VALUES (%s) RETURNING semester_id;", (semester_name,))
                    semester_id = cursor.fetchone()[0]
                    connection.commit()

                cursor.execute(
                    "SELECT password, email, username FROM \"user\" WHERE email = %s;",
                    (email,)
                )
                result = cursor.fetchone()

                if result and result[0] == password and result[1] == email and result[2] == username:
                    session["user"] = email
                    session["semester_id"] = semester_id

                    cursor.execute(
                        "SELECT subject_id, name FROM subjects WHERE semester_id = %s;",
                        (semester_id,)
                    )
                    subjects = cursor.fetchall()
                    session["subjects"] = [{"id": subject[0], "name": subject[1]} for subject in subjects]

                    return redirect(url_for("user"))
                else:
                    flash("Invalid username/email or password.")
                    return redirect(url_for("loginhello"))

            except Exception as e:
                flash(f"An error occurred: {str(e)}")
                return redirect(url_for("loginhello"))

            finally:
                cursor.close()
                connection.close()
        else:
            flash("Invalid email format. Please use a valid email address.")
            return redirect(url_for("loginhello"))

    return render_template("loginhello.html")



@app.route("/user")
def user():
    if "user" in session:
        subjects = session.get("subjects", [])
        return render_template("subject.html", subjects=subjects)
    else:
        return redirect(url_for("loginhello"))



@app.route("/subject/<int:subject_id>erec")
def subject_description(subject_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute(
        "SELECT average_marks, study_days, resources FROM subject_descriptions WHERE subject_id = %s;",
        (subject_id,)
    )
    subject_info = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if subject_info:
        avg_marks, study_days, resources = subject_info
        return render_template("subject_description.html", avg_marks=avg_marks, study_days=study_days, resources=resources)
    else:
        flash("Subject description not found.")
        return redirect(url_for("user"))
    
    
@app.route("/logout")
def logout():
    session.clear()  
    flash("You have been logged out.")
    return redirect(url_for("home"))     



@app.route("/adminsign", methods=["GET", "POST"])
def adminsign():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        admin_credentials = {
            "agrimaregmi2004@gmail.com": "Agrima11",
            "pratistha.sapkota123@gmail.com": "Pratistha21",
            "sanskriti.khatiwada@gmail.com": "Sanskriti37",
        }

        if email in admin_credentials and password == admin_credentials[email]:
            session["admin"] = email
            return redirect(url_for("admin_subjects"))
        else:
            flash("Invalid admin credentials.")
            return redirect(url_for("adminsign"))

    return render_template("adminsign.html")

@app.route("/admin/subjects", methods=["GET", "POST"])
def admin_subjects():
    if request.method == "POST":
        subject_name = request.form["subject_name"]
        semester_name = request.form["semester"]

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT semester_id FROM sem WHERE name = %s;", (semester_name,))
            semester_result = cursor.fetchone()

            if semester_result:
                semester_id = semester_result[0]
            else:
                cursor.execute("INSERT INTO sem (name) VALUES (%s) RETURNING semester_id;", (semester_name,))
                semester_id = cursor.fetchone()[0]
                connection.commit()

            cursor.execute(
                "INSERT INTO subjects (name, semester_id) VALUES (%s, %s) RETURNING subject_id;",
                (subject_name, semester_id)
            )
            subject_id = cursor.fetchone()[0]
            connection.commit()

            flash(f"Subject '{subject_name}' added successfully!")
            return redirect(url_for("admin_subjects"))

        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect(url_for("admin_subjects"))

        finally:
            cursor.close()
            connection.close()

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT subject_id, name FROM subjects;")
        subjects = cursor.fetchall()

        return render_template("admin_subjects.html", subjects=subjects)

    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for("home"))

    finally:
        cursor.close()
        connection.close()
        

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

