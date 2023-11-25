from flask import Flask, request, Blueprint
from flask_restx import Api, Resource, fields
from models import *

api_bp = Blueprint('customer', __name__)
api = Api(api_bp, version='1.0', title='Customer API', description='API for managing customers')



user_model = api.model('Customer', {
    'id': fields.Integer(description='Customer ID'),
    'Companyname': fields.String(description='Company Name'),
    'City': fields.String(description='City'),
    'Code': fields.String(description='Customer Code'),
    'Address': fields.String(description='Address'),
    'State': fields.String(description='State'),
    'ZipCode': fields.String(description='Zip Code'),
    'EmailID': fields.String(description='Email ID'),
    'PhoneNumber': fields.String(description='Phone Number'),
    'FeedTaxId': fields.String(description='Feed Tax ID'),
    'DateFrom': fields.Date(description='Date From'),
    'DataThru': fields.Date(description='Data Thru'),
    'Status': fields.String(description='Status'),
})


class CustomerList(Resource):
    # @api.expect(user_model, validate=True)
    def get(self):
        customer = Customer.query.all()
        if customer:
            result = {
                'S.No': customer.id,
                'Company Name': customer.Companyname,
                'City': customer.City,
                'Code' : customer.Code,
                'Address': customer.Address,
                'State' : customer.State,
                'ZipCode' : customer.ZipCode,
                'Email ID' : customer.EmailID,
                'Phone Number' : customer.PhoneNumber,
                'Feed Tax Id #' : customer.FeedTaxId,
                'Start Date' : customer.DateFrom,
                'End Data' : customer.DataThru,
                'Status' : customer.Status
            }
            return result, 200
        else:
            return 'Customer not found', 404
class CustomerList(Resource):
    @api.expect(user_model, validate=True)
    def post(self):
        data = request.get_json()
        next_user_id = Customer.query.order_by(Customer.id.desc()).first()
        if next_user_id:
            next_user_id = next_user_id.id + 1
        else:
            next_user_id = 1

        if all(key in data for key in ['Companyname', 'City', 'Code', 'Address','State','ZipCode','EmailID','PhoneNumber','FeedTaxId','DateFrom','DataThru','Status']):
            new_customer = Customer(
                SNo = data[{next_user_id}],
                Companyname=data['Companyname'],
                City=data['City'],
                Code= data['Code'],
                Address=data['Address'],
                State=data['State'],
                ZipCode=data['ZipCode'],
                EmailID=data['EmailID'],
                PhoneNumber=data['PhoneNumber'],
                FeedTaxId=data['FeedTaxId'],
                DateFrom=data['DateFrom'],
                DataThru=data['DataThru'],
                Status=data['Status']
            )
            db.session.add(new_customer)
            db.session.commit()
            return 'Customer created successfully', 201
        else:
            return 'Invalid data provided for creating customer', 400
        
class Customerapi(Resource):
    def get(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            result = {
                'Companyname': customer.Companyname,
                'City': customer.City,
                'Code': customer.Code,
                'Address': customer.Address,
                'State': customer.State,
                'ZipCode': customer.ZipCode,
                'EmailID': customer.EmailID,
                'PhoneNumber': customer.PhoneNumber,
                'FeedTaxId': customer.FeedTaxId,
                'DateFrom': customer.DateFrom,
                'DataThru': customer.DataThru,
                'Status': customer.Status
            }
            return result, 200
        else:
            return 'Customer not found', 404
    def put(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            data = request.get_json()
            if all(key in data for key in ['customername', 'city', 'address', 'number']):
                customer.Companyname=data['Companyname'],
                customer.City=data['City'],
                customer.Code= data['Code'],
                customer.Address=data['Address'],
                customer.State=data['State'],
                customer.ZipCode=data['ZipCode'],
                customer.EmailID=data['EmailID'],
                customer.PhoneNumber=data['PhoneNumber'],
                customer.FeedTaxId=data['FeedTaxId'],
                customer.DateFrom=data['DateFrom'],
                customer.DataThru=data['DataThru'],
                customer.Status=data['Status']
                db.session.commit()
                return 'Customer updated successfully', 200
            else:
                return 'Invalid data provided for update', 400
        else:
            return 'Customer not found', 404
        
    def delete(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return 'Customer deleted successfully', 200
        else:
            return 'Customer not found', 404
        
class ProjectList(Resource):
    def get(self, project_id):
        project = Project.query.get(project_id)
        if project:
            customer = Customer.query.filter_by(id=project.customer_id).first()
            if customer:
                result = {
                    'S.No': project.id,
                    'Project Name' : project.ProjectName,
                    'Project Name' : project.ProjectCode,
                    # 'customer_id': customer.id,
                    'Company Name': customer.CompanNname,
                    'Effective From' : project.EffectiveFrom,
                    'Effective Thru' : project.EffectiveThru
                }
                return result, 200
            else:
                return 'Customer not found for this project', 404
        else:
            return 'Project not found', 404

    def post(self):
        data = request.get_json()
        customer_id = data.get('customer_id')
        # Other project data extraction from the request
        new_project = Project(customer_id=customer_id)
        db.session.add(new_project)
        db.session.commit()
        return 'Project created successfully', 201
class ProjectAPI(Resource):
    def put(self, project_id):
        project = Project.query.get(project_id)
        if project:
            data = request.get_json()
            if 'customer_id' in data:
                project.customer_id = data['customer_id']
            # Update other project data here as needed
            db.session.commit()
            return 'Project updated successfully', 200
        else:
            return 'Project not found', 404

    def delete(self, project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return 'Project deleted successfully', 200
        else:
            return 'Project not found', 404
        
# # Add resources to the API
api.add_resource(CustomerList,'/customer')
api.add_resource(Customerapi,'/customer/<int:customer_id>')
# api.add_resource(Projectapi, '/project/<int:project_id>')