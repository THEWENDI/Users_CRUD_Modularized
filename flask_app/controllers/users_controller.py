from flask_app import app

from flask import render_template, request, redirect
# import the class from friend.py
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route('/create')
def create():
    return render_template("form.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/edit_user/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/edit_user',methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/show_user/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))

@app.route('/delete_user/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/')