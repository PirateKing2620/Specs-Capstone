from forms import LoginForm
from customers import customers

from flask import Flask, render_template, redirect, flash, session, request
app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app.secret_key = 'terraria'

@app.route("/login", methods=["GET", "POST"])
def login():
   """Log user into site."""
   form = LoginForm(request.form)

   if form.validate_on_submit():
      username = form.username.data
      password = form.password.data

      user = customers.get_by_username(username)

      if not user or user['password'] != password:
            flash("Invalid username or password")
            return redirect('/login')

      session["username"] = user['username']
      flash("Logged in.")
      return redirect("/base.html")

   return render_template("login.html", form=form)


# @app.route("/register", methods=["GET", "POST"])
# def register():
#    pass

# db.session.add
# db.session.commit

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


if __name__ == '__main__':
	app.run()