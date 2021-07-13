from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/login/<name>')
def login(name):
    admins = ["Godwin", "Thapelo", "Jason", "Candice"]
    students = ["Brent", "Adam", "Ronald", "Zoe"]
    if name in admins:
        return redirect(url_for('admin_page', name=name))
    elif name in students:
        return redirect(url_for('user_page', name=name))
    else:
        return redirect(url_for('visitor_page', name=name))


@app.route('/admin/')
def admin_page():
    return "This is the admin page"


@app.route('/user/')
def user_page():
    return "This is the user page"


@app.route('/visitor/')
def visitor_page():
    return "This is the visitors page"


@app.route('/payment/<int:sal>')
def payment_page(sal):
    if sal >= 20000:
        return "You are rich"
    else:
        return redirect('https://www.sahomeloans.com/%27')


if __name__ == '__main__':
    app.debug = True
    app.run()
