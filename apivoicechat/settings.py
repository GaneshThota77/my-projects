class Config:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'LAPTOP-CMPHGTJN'
    database = 'gpttables'

    # Create the connection string
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;CHARSET=UTF8"
    database_uri = f"mssql+pyodbc:///?odbc_connect={connection_string}"

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False