#from datetime import datetime
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import psycopg2
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rohit@localhost/persondata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employes_data(db.Model):
    emp_id = db.Column(db.Integer , primary_key = True)
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    email = db.Column(db.String(120))
    salary = db.Column(db.Integer())

    # date_added = db.Column(db.datetime, default=datetime.utcnow)

    # def __init__(self,id,fname,lname,email,salary):
    #     self.id = id
    #     self.fname = fname
    #     self.name = lname
    #     self.email = email
    #     self.salary = salary


@app.route("/add", methods=["POST"])
def submit():
    if request.method=='POST':
        
        posted_data = request.get_json()
        employes = Employes_data(
        emp_id = posted_data['emp_id'],
        fname = posted_data['fname'],
        lname = posted_data['lname'],
        email = posted_data['email'],
        salary = posted_data['salary'])
        
        db.session.add(employes)
        db.session.commit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        return jsonify("Successfully stored  " + str(employes))
        
        
@app.route("/get", methods=["GET"])
def get():
    users = Employes_data.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['emp_id'] = user.emp_id
        user_data['fname'] = user.fname
        user_data['lname'] = user.lname
        user_data['email'] = user.email
        user_data['salary'] = user.salary 
        output.append(user_data)
    return jsonify(output)

@app.route("/get/<emp_id>", methods=["GET"])
def get_one(emp_id):

    user = Employes_data.query.filter_by(emp_id = emp_id).first()
    if not user:
        return jsonify({'msg': 'No user found!'})
    user_data = {}
    user_data['emp_id'] = user.emp_id
    user_data['fname'] = user.fname
    user_data['lname'] = user.lname
    user_data['email'] = user.email
    user_data['salary'] = user.salary
    return jsonify({'user':user_data}) 

@app.route("/update/<emp_id>", methods=["PUT"])
def update_emp(emp_id):
    user = Employes_data.query.filter_by(emp_id=emp_id).first()
    if user:
        user_data = request.get_json()
                    
        emp_id = user_data["emp_id"]
        fname = user_data["fname"]
        lname = user_data["lname"]
        email = user_data["email"]
        salary = user_data["salary"]
        user.emp_id = emp_id
        user.fname = fname
        user.lname = lname
        user.email = email
        user.salary = salary
        db.session.commit()
        return jsonify({'msg': 'Employe has been updated'})
        
    else:
        return jsonify({'msg': 'Employe not found!'})


@app.route("/delete/<emp_id>", methods=["DELETE"])
def delete_emp(emp_id):
    user = Employes_data.query.filter_by(emp_id=emp_id).first()
    if not user:
        return jsonify({'msg': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'msg': 'employe has been deleted'})
    # def __repr__(self):
    #     return '<employes_details %r>' % self.name
if __name__ == '__main__':
    #db.create_all()
    app.run(debug = True)
    
