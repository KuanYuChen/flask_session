
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
auth={'admin':'admin','user':'user','guest':''}

@app.route('/')
def home():
    if session.get('logged_admin'):
        return "Hello Admin!  <a href='/logout'>Logout</a>"
    elif session.get('logged_user'):
        return "Hello User!  <a href='/logout'>Logout</a>"
    elif session.get('logged_guest'):
        return "Hello Guest!  <a href='/logout'>Logout</a>"
    else:
        return render_template('login.html')
    '''
    if not session.get('logged_admin'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
    '''

 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'] == 'admin' and  request.form['password'] == auth['admin']:
        session['logged_admin'] = True
        print("admin")
    elif request.form['username'] == 'user' and  request.form['password'] == auth['user']:
        session['logged_user'] = True
        print("user")
    elif request.form['username'] == 'guest' :
        session['logged_guest'] = True
        print("guest")
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_admin'] = False
    session['logged_user'] = False
    session['logged_guest'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
