from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/delicious'
db = SQLAlchemy(app)
class Book_table(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20),nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(120), nullable=True)
    time = db.Column(db.String(120),nullable=True)
    people = db.Column(db.String(120),nullable=True)
    message = db.Column(db.String(120),nullable=True)

class Contact(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20),nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    subject = db.Column(db.String(12), nullable=False)
    message= db.Column(db.String(120), nullable=False)

@app.route('/')
def home():        
    return render_template("index.html")
@app.route('/book_table',methods=["GET","POST"])
def book_table():
    if (request.method=="POST"):
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        message=request.form.get("message")
        date=request.form.get("date")
        time=request.form.get("time")
        people=request.form.get("people")
        entry=Book_table(name=name,email=email,phone_num=phone,date=datetime.datetime.now(),message=message,people=people,time=datetime.datetime.now())
        #(name=name) databasename=your form name
        db.session.add(entry)
        db.session.commit()
        return render_template("index.html")

    return render_template("book_table.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    if(request.method=="POST"):
        name=request.form.get("name")
        email=request.form.get("email")
        subject=request.form.get("subject")
        message=request.form.get("message")
        phone=request.form.get("phone")
        entry=Contact(name=name,email=email,subject=subject,message=message,phone_num=phone)
        db.session.add(entry)
        db.session.commit()
        return render_template("index.html")

    return render_template("contact.html")
    
if __name__=="__main__":
    app.run()
