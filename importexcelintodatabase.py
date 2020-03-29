import numpy as np 
import pandas as pd 
import xlrd
import tkinter as tk
from tkinter import filedialog
import psycopg2

# Database information

host="localhost"
portnumber="5432"
username="postgres"
password="avinash12"
databasename="Database for test"


#Choose file window using tkinter
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

#Open file

data = pd.read_excel(file_path)
column_values = data.columns
print(column_values)

#find length of the array

length = len(column_values)
print(length)

#Store column data in variable
#We need to add more if condition if the length of array is more


for i in column_values:
    if i==column_values[0]:
        column1=i
        print(column1)    
    if i==column_values[1]:
        column2=i
        print(column2)
    if i==column_values[2]:
        column3=i
        print(column3)
    if i==column_values[3]:
        column4=i
        print(column4)
    if i==column_values[4]:
        column5=i
        print(column5)

#Connecting to postgres DB

try:
    connection = psycopg2.connect(user = username,
                                  password = password,
                                  host = host,
                                  port = portnumber,
                                  database = databasename)

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

#Create table querys

query1 = 'CREATE TABLE bill ('+column1+' varchar(255),'+column2+' varchar(255),'+column3+' varchar(255),'+column4+' varchar(255),'+column5+' varchar(255)'');'
print(query1)
cursor.execute(query1)
connection.commit()
print("Table created successfully in PostgreSQL")