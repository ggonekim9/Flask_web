from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user/<path:username>')
def show_user_profile(username):
    return 'User : %s' %username

@app.route('/admin')
def hello_admin():
    return 'hello admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s as guest' %guest

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
    # 启动调试模式
    app.debug = True
    app.run()
    