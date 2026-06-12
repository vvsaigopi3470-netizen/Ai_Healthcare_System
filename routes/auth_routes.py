from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import session

from database.db import mysql

auth = Blueprint("auth", __name__)


# =========================
# REGISTER
# =========================
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        print("Selected Role =", role)

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=%s
            """,
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:

            flash("Email already exists")
            return redirect('/register')

        # Store plain password (Project Demo)
        query = """
        INSERT INTO users
        (
            name,
            email,
            password,
            role
        )
        VALUES
        (%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                name,
                email,
                password,
                role
            )
        )

        mysql.connection.commit()

        flash("Registration Successful")

        return redirect('/login')

    return render_template("register.html")


# =========================
# LOGIN
# =========================
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=%s
            """,
            (email,)
        )

        user = cursor.fetchone()

        print("USER DATA =", user)

        if user:

            stored_password = user[3]
            role = user[4]

            print("Entered Password =", password)
            print("Stored Password =", stored_password)
            print("ROLE =", role)

            if stored_password == password:

                session['user_id'] = user[0]
                session['name'] = user[1]
                session['email'] = user[2]
                session['role'] = role

                role = str(role).strip()

                print("Redirecting Role =", role)

                if role == "Admin":
                    return redirect('/admin_dashboard')

                elif role == "Doctor":
                    return redirect('/doctor_dashboard_view')

                elif role == "Patient":
                    return redirect('/patient_dashboard_view')

                elif role == "Staff":
                    return redirect('/staff_dashboard')

                else:
                    return redirect('/dashboard')

        flash("Invalid Email or Password")

    return render_template("login.html")


# =========================
# DASHBOARD
# =========================
@auth.route('/dashboard')
def dashboard():

    return render_template(
        "dashboard.html"
    )


# =========================
# LOGOUT
# =========================
@auth.route('/logout')
def logout():

    session.clear()

    flash("Logged Out Successfully")

    return redirect('/login')

