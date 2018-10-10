from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():

    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    title = 'Signup'

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        for page in username:
            if page.isspace():
                username_error = 'No spaces between words.'
                username = ''
            else:
                if (len(username) < 3) or (len(username) > 20):
                    username_error = 'Username needs to be 3-20 characters.'
                    username = ''

        if not username:
            username_error = 'Not a valid username'
            username = ''

        for page in password:
            if page.isspace():
                password_error = 'No spaces between words.'
            else:
                if (len(password) < 3) or (len(password) > 20):
                    password_error = 'Password must be 3-20 characters and not spaces between words.'
        if not len(password):
            password_error = 'Not a valid password'

        if password != verify_password:
            verify_password_error = 'Passwords do not match.'

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = 'This is not a valid email.'
            email = ''

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect('/start?username={0}'.format(username))

    return render_template('home.html', title=title, username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           verify_password_error=verify_password_error, email_error=email_error)

@app.route('/start')
def start():
    title = "Welcome"
    username = request.args.get('username')
    return render_template('start.html', title=title, username=username)

if __name__ == '__main__':
    app.run()

#Victor Marquez