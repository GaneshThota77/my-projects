class Config:
    driver = 'ODBC+Driver+17+for+SQL+Server'
    server = 'LAPTOP-CMPHGTJN'
    database = 'ProviderPortel'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect=DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;CHARSET=UTF8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
