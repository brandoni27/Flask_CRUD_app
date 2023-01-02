from flask import Flask, render_template, session, redirect,request
from user import User
app = Flask(__name__)

app.secret_key="this is the secret key"


@app.route("/")
def users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("list_users.html", all_users = users)

@app.route('/process',methods=['POST'])
def add_users():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.add_user(data)
    return redirect('/')

@app.route('/add_users')
def posted():
    return render_template('add_users.html')
    
if __name__=="__main__":
    app.run(debug=True)