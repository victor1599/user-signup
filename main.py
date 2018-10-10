from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

username = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="username">username:</label>
            <input id="username" type="text" name="user_name" />
            <input type="submit" />
        </form> 
    </body>
</html>
"""

@app.route("/")
def index():
    return username

@app.route("/hello", methods=['POST'])
def hello():
    user_name = request.form['user_name']
    return '<h1>Hello, ' + user_name + '<h1>'

app.run()