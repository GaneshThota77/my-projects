from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy(metadata=SQLAlchemy.metadata(bind=None))
db = SQLAlchemy()

class Customer(db.Model):

    __tablename__ = 'Customer'

    id = db.Column(db.Integer, primary_key=True)
    Companyname = db.Column(db.String(50))
    Code = db.Column(db.String(20))
    Address = db.Column(db.String(225))
    city = db.Column(db.String(50))
    State = db.Column(db.String(50))
    ZipCode = db.Column(db.String(20))
    EmailID = db.Column(db.String(20))
    PhoneNumber = db.Column(db.String(20))
    FeedTaxId = db.Column(db.String(20))
    DateFrom = db.Column(db.Date)
    DataThru = db.Column(db.Date)
    Status = db.Column(db.Boolean)

class Department(db.Model):

    __tablename__ = 'Department'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(20))
    department_code = db.Column(db.String(20))
    Status = db.Column(db.Boolean)

class Permission(db.Model):

    __tablename__ = 'Permission'

    id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.String(20))
    permission_code = db.Column(db.String(20))

class Roles(db.Model):

    __tablename__ = 'Roles' 
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    Role = db.Column(db.String(50))
    Code = db.Column(db.String(20))
    Department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))
    Permission_id = db.Column(db.Integer, db.ForeignKey('Permission.id'))
    Status = db.Column(db.Boolean)

class Users(db.Model):

    __tablename__ = 'Users' 

    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(20))
    Code = db.Column(db.String(20))
    UserID = db.Column(db.String(20))
    Department_ID = db.Column(db.Integer, db.ForeignKey('Department.id'))
    Reports_To = db.Column(db.String(20))
    EmailID = db.Column(db.String(20))
    Role_id = db.Column(db.Integer, db.ForeignKey('Roles.id'))
    Status = db.Column(db.Boolean)

class Project(db.Model):

    __tablename__ = 'Project' 

    id = db.Column(db.Integer, primary_key=True)
    ProjectName = db.Column(db.String(50))
    ProjectCode = db.Column(db.String(20))
    Customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
    EffectiveFrom = db.Column(db.Date)
    EffectiveThru = db.Column(db.Date)
    Status = db.Column(db.Boolean)

class Forms(db.Model):

    __tablename__ = 'Forms' 

    id = db.Column(db.Integer, primary_key=True)
    FormName = db.Column(db.String(50))
    FormCode = db.Column(db.String(20))
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'))
    Status = db.Column(db.Boolean)

class Queues(db.Model):

    __tablename__ = 'Queues' 

    id = db.Column(db.Integer, primary_key=True)
    QueuesName = db.Column(db.String(50))
    Role_id = db.Column(db.Integer, db.ForeignKey('Roles.id'))
    # ClaimStatus_ID = db.Column(db.Integer, db.ForeignKey('ClaimStatus.id'))
    Permission_id = db.Column(db.Integer, db.ForeignKey('Permission.id'))
    Status = db.Column(db.Boolean)

class QueueRouting(db.Model):

    __tablename__ = 'QueueRouting' 

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'))
    Queues_id = db.Column(db.Integer, db.ForeignKey('Queues.id'))


class ClaimStatus(db.Model):

    __tablename__ = 'ClaimStatus' 

    id = db.Column(db.Integer, primary_key=True)
    TrackingNumber = db.Column(db.String(20))
    claimType = db.Column(db.String(20))
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'))
    Customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
    Queues_id = db.Column(db.Integer, db.ForeignKey('Queues.id'))
    ClaimStatus = db.Column(db.String(20))
    RejectReason = db.Column(db.String(20))
    Status = db.Column(db.Boolean)


# Perform the join query using ORM
# query = session.query(ClaimStatus, Customer, Queue, Project).\
#     join(Customer, ClaimStatus.customer_id == Customer.id).\
#     join(Queue, ClaimStatus.queue_id == Queue.id).\
#     join(Project, ClaimStatus.project_id == Project.id)