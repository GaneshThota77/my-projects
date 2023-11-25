
#from crypt import methods
#from lib2to3.pgen2.token import tok_name
from flask import Flask,request,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import uuid   #for genarating random id
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rohit@localhost/newdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'massage':'token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'massage': 'token is invalid'},401)
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/user',methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'massage':'cannot perform that function!'})
    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify(output) 

@app.route('/user/<user_id>',methods=['GET'])
@token_required
def get_one_users(current_user,public_id):
    if not current_user.admin:
        return jsonify({'massage':'cannot perform that function!'})

    user = User.query.filter_by(public_id =public_id).first()
    
    if not user:
        return jsonify({'massage' : 'no user found!'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify(user_data)

@app.route('/user',methods=['POST'])
@token_required
def create_users(current_user):
    if not current_user.admin:
        return jsonify({'massage':'cannot perform that function!'})
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method= 'rohit777')
    new_user = User(public_id = str(uuid.uuid4(())),name=data['name'],password=hashed_password,admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message:new user created"})

@app.route('/user/<user_id>',methods=['PUT'])
@token_required
def update_users(current_user,public_id):
    if not current_user.admin:
        return jsonify({'massage':'cannot perform that function!'})

    user = User.query.filter_by(public_id =public_id).first()
    
    if not user:
        return jsonify({'massage' : 'no user found!'})
    user.admin =True
    db.session.commit()

    return jsonify({'massage':'user has been updated'})

@app.route('/user/<user_id>',methods=['DELETE'])
@token_required
def delete_users(current_user,public_id):
    if not current_user.admin:
        return jsonify({'massage':'cannot perform that function!'})

    user = User.query.filter_by(public_id =public_id).first()
    
    if not user:
        return jsonify({'massage' : 'no user found!'})
    db.session.delete(user)
    db.session.commit()

    return jsonify({'massage':'user has been deleted'})
@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify',401)

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return jsonify({'message':'no  user found'})
    
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
        
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('could not verify',401)


@app.route('/todo', methods=['GET'])
@token_required
def todo_all_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    output = []
    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        output.append(todo_data)
    return jsonify(output)

@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def todo_one_todos(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id,user_id=current_user.id).first()
    if not todo:
        return jsonify({'message':'no todo found!'})
    todo_data = {}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete   
    return jsonify(todo_data)

@app.route('/todo', methods=['POST'])
@token_required
def create_todos(current_user):
    data = request.get_json()
    new_tudo = Todo(text=data['text'], complete=False,user_id=current_user.id)
    db.session.add(new_tudo)
    db.session.commit()
    return jsonify({'message':'todo created'})

@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def update_todos(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id,user_id=current_user.id).first()
    if not todo:
        return jsonify({'message':'no todo found!'})

    todo.complete = True
    db.session.commit()

    return jsonify({'message':'Todo item hasbeen updated'})

@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todos(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id,user_id=current_user.id).first()
    if not todo:
        return jsonify({'message':'no todo found!'})
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message':'todo item deleted'})

    
if __name__ == '__main__':
    app.run(debug=True)