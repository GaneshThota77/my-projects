from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import openai
import json
from config import *
from models import *
from main import *


# from sqlalchemy import text
bp = Blueprint("api", __name__)
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
# db = SQLAlchemy(app)

# # Set up your OpenAI API key
openai.api_key = YOUR_OPENAI_API_KEY


# API endpoint to handle messages
@app.route('/handle_message', methods=['POST'])
def handle_message():
    data = request.json
    user_message = data.get('user_message')
    if user_message:
        response = process_user_message(user_message)
    else:
        response = "Invalid input."

    return jsonify({"message": response})


# # Function to process user messages and interact with GPT-3
def process_user_message(user_message):
    # Step 1: send the conversation and available functions to GPT
    # Check for greetings
    """def run_conversation():       
        This line defines a function (a set of instructions) called "run_conversation" that you can later use to start a conversation.
        
        messages = [...]
        Here, we create a variable called "messages" that stores a list of messages. In this example, it starts with a message from the user asking about the weather in Boston.
        
        functions = [...]
        This part sets up a list of functions that the computer program can use. In this case, there's one function called "get_current_weather" that's described as a way to get the current weather in a specific location.
        
        response = openai.ChatCompletion.create(...)
        This line sends the user's message and the available functions to a program called "GPT" (a smart computer program that understands text). It then gets a response from GPT.
        
        response_message = response["choices"][0]["message"]
        This line extracts the message from GPT's response so we can work with it.
        
        if response_message.get("function_call"):
        This checks if GPT wants to call a function based on the response. In simpler terms, it's looking to see if GPT is asking the program to do something specific.
        
        available_functions = {...}
        This sets up a dictionary that matches function names (like "get_current_weather") with the actual functions that can do those tasks.
        
        function_name = response_message["function_call"]["name"]
        If GPT wants to call a function, this line figures out which function it's asking for.
        
        function_to_call = available_functions[function_name]
        This line finds the actual function (like "get_current_weather") that matches the name GPT provided.
        
        function_args = json.loads(response_message["function_call"]["arguments"])
        It extracts the arguments (information) that GPT wants to pass to the function. For example, it might want to know the weather in Boston.
        
        function_response = function_to_call(...)
        This line calls the function (like "get_current_weather") with the provided arguments to get a response. It's like asking the function to do its job.
        
        messages.append(...)
        Here, we add the information about the function call and its response to the ongoing conversation. This helps GPT understand what's happening.
       
        second_response = openai.ChatCompletion.create(...)
        Finally, we send the updated conversation to GPT to get a new response that takes into account the function's response. This keeps the conversation going.
        
        return second_response
        The function then returns this new response from GPT, which can be used or displayed as needed.
       """

    messages = [{"role": "user", "content": user_message}]
    functions = [
        {
            "name": "get_leave_balance",
            "description": "Get the leave balance from database for an employee.",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "The id of the employee whose leave balance you want to check."
                    }
                },
                "required": ["employee_id"]
            }
        },
        
        {
            "name": "get_holiday_leaves",
            "description": "Get the list of holidays from the database.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "returns": {
                "type": "string",
                "description": "A string containing the list of holidays with date, description, and day of the week."
            }
        },
        {
            "name": "get_all_employees",
            "description": "Query all employee data from the database.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "returns": {
                "type": "string",
                "description": "A list of employee objects with ID, name, and leave balance."
            }
        },
        {
            "name": "leave_policy",
            "description": "Query all leave policies from the database.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "returns": {
                "type": "string",
                "description": "A string containing a list of leave policies with ID and policy name."
            }
            
        }


    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        available_functions = {
            "get_leave_balance": get_leave_balance,
            "get_holiday_leaves": get_holiday_leaves,
            "get_all_employees":get_all_employees,
            "leave_policy":leave_policy,
        }
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions.get(function_name)
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(function_args)

        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        ) 
     
    
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )  # get a new response from GPT where it can see the function response

        return second_response['choices'][0]['message']['content']
    else:
        return response_message.get('content', 'GPT-3 response is empty.')
# Function to process user messages and interact with GPT-3

# Function to get employee leave balance
def get_leave_balance(arguments):
    employee_id = arguments.get('employee_id')

    # Query the database for the leave balance of the employee with the given name
    employee = Employee.query.filter_by(id=employee_id).first()

    # # SQL query to retrieve employee data by name or ID
    # query = text("SELECT * FROM employee WHERE name = :identifier OR id = :identifier")
    # result = db.engine.execute(query, identifier=employee_identifier)


    if employee:
        leave_balance = employee.leave_balance
        return f"your leave balance is {leave_balance} days."
    else:
        return "Employee not found."
    
def get_holiday_leaves(arguments):
    holidays = Holiday.query.all()  # Use .all() to get all holiday records

    if holidays:
        holiday_list = [f"{holiday.HolidayDate}: {holiday.Description}" for holiday in holidays]
        return "Your holidays list:\n" + "\n".join(holiday_list)
    else:
        return "No holidays found in the database."
    
def get_all_employees(arguments):
    """
    Query all employee data from the database.

    Returns:
        str: A string containing employee data in a formatted list.
    """
    all_employees = Employee.query.all()
    
    if all_employees:
        employee_list = [f"ID: {employee.id}, Name: {employee.name}, Leave Balance: {employee.leave_balance}"
            for employee in all_employees
        ]
        return "Employee List:\n" + "\n".join(employee_list)
    
    return "No data found in the database"
def leave_policy(arguments):
    policies = LeavePolicy.query.all()
    if policies:
        policy_list = [f"ID: {policys.id}, leave_policy: {policys.leave_policy}"
            for policys in policies ]
        
        return "Employee List:\n" + "\n".join(policy_list)
    
    return "No data found in the database"
# if __name__ == '__main__':
#     app.run(debug=True)










































# def process_user_message(user_message):
#     # Step 1: send the conversation and available functions to GPT
#     messages = [{"role": "user", "content": user_message}]
#     functions = [
#         {
#             "name": "get_employee_info",
#             "description": "Get information about an employee.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "employee_identifier": {
#                         "type": "string",
#                         "description": "The name or ID of the employee."
#                     }
#                 },
#                 "required": ["employee_identifier"]
#             }
#         }
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         functions=functions,
#         function_call="auto",  # auto is default, but we'll be explicit
#     )
#     response_message = response["choices"][0]["message"]

#     # Step 2: check if GPT wanted to call a function
#     if response_message.get("function_call"):
#         # Step 3: call the function
#         available_functions = {
#             "get_employee_info": get_employee_info,
#         }
#         function_name = response_message["function_call"]["name"]
#         function_to_call = available_functions.get(function_name)
#         function_args = json.loads(response_message["function_call"]["arguments"])
#         function_response = function_to_call(function_args)

#         # Step 4: send the info on the function call and function response to GPT
#         messages.append(response_message)  # extend conversation with assistant's reply
#         messages.append(
#             {
#                 "role": "function",
#                 "name": function_name,
#                 "content": function_response,
#             }
#         )  # extend conversation with function response
#         second_response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#         )  # get a new response from GPT where it can see the function response

#         return second_response['choices'][0]['message']['content']
#     else:
#         return response_message.get('content', 'GPT-3 response is empty.')

# # Function to get employee information by name or ID
# def get_employee_info(arguments):
#     employee_identifier = arguments.get('employee_identifier')

#     # Query the database for employee data by name or ID
#     employee = Employee.query.filter(
#         (Employee.name == employee_identifier) | (Employee.id == employee_identifier)
#     ).first()

#     if employee:
#         # Return employee information as needed
#         return f"Employee ID: {employee.id}, Name: {employee.name}, Leave Balance: {employee.leave_balance} days."
#     else:
#         return "Employee not found."

# # Function to process user messages and interact with GPT-3
# def process_user_message(user_message):
#     # Step 1: send the conversation and available functions to GPT
#     messages = [{"role": "user", "content": user_message}]
#     functions = [
#         {
#             "name": "get_leave_balance",
#             "description": "Get the leave balance for an employee.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "employee_name": {
#                         "type": "string",
#                         "description": "The name of the employee whose leave balance you want to check."
#                     }
#                 },
#                 "required": ["employee_name"]
#             }
#         }
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages,
#         functions=functions,
#         function_call="auto",  # auto is default, but we'll be explicit
#     )
#     response_message = response["choices"][0]["message"]

#     # Step 2: check if GPT wanted to call a function
#     if response_message.get("function_call"):
#         # Step 3: call the function
#         available_functions = {
#             "get_leave_balance": get_leave_balance,
#         }
#         function_name = response_message["function_call"]["name"]
#         function_to_call = available_functions.get(function_name)
#         function_args = json.loads(response_message["function_call"]["arguments"])
#         function_response = function_to_call(function_args)

#         # Step 4: send the info on the function call and function response to GPT
#         messages.append(response_message)  # extend conversation with assistant's reply
#         messages.append(
#             {
#                 "role": "function",
#                 "name": function_name,
#                 "content": function_response,
#             }
#         )  # extend conversation with function response
#         second_response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#         )  # get a new response from GPT where it can see the function response

#         return second_response['choices'][0]['message']['content']
#     else:
#         return response_message.get('content', 'GPT-3 response is empty.')
# Function to process user messages and interact with GPT-3