#url data: https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks
#wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import numpy as np 
from datetime import datetime

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ':' + message + '\n')

def extract(url, table_atrributes):
    df = pd.DataFrame(columns=table_atrributes)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            a = col[1].find_all('a')
            data_dict = {"Name":a[1].contents[0],
                          "MC_USD_Billion": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)

    return df


def transform(df, csv_path):
    exchange_rate = pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index(exchange_rate['Currency']).to_dict()['Rate']
    
    MC_USD_Billion  = df["MC_USD_Billion"].tolist()
    MC_USD_Billion  = [float("".join(x.split(','))) for x in MC_USD_Billion]
    MC_USD_Billion  = [np.round(x,2) for x in MC_USD_Billion]
    df["MC_USD_Billion"] = MC_USD_Billion

    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement,sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)    
    print(query_output)

url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
table_atrributes = ['Name','MC_USD_Billion']
# table_atrributes = ['Name','MC_USD_Billion',
#                     'MC_GBP_Billion','MC_EUR_Billion',
#                     'MC_INR_Billion']
output_path = './Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './exchange_rate.csv'

log_progress("Preliminaries complete.")
log_progress("Initiating ETL process.")

extract_data = extract(url, table_atrributes)

log_progress("Data extraction complete.")
log_progress("Initiating Transformation process.")

transformed_data = transform(extract_data, csv_path)

log_progress("Data transformation complete.")
log_progress("Initiating Loading process.")

log_progress("Data saved to CSV file")

load_to_csv(transformed_data,output_path)

log_progress("SQL Connection initiated")
sql_connection = sqlite3.connect(db_name)
load_to_db(transformed_data, sql_connection,table_name)

log_progress("Data loaded to Database as a table, Executing queries")

query_statement = f"SELECT * from {table_name} WHERE MC_USD_billion >= 100"
run_query(query_statement, sql_connection)

query_statement1 = f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query_statement1, sql_connection)

query_statement2 = f"SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement2, sql_connection)

sql_connection.close()
log_progress("Server Connection closed")