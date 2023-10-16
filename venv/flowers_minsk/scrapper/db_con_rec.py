import psycopg2
import time
from db_conf_scrapper import database, password, host, user

#Создание базы данных
def creation_db():
    connection = psycopg2.connect(
        database = database,
        password = password,
        host = host,
        user = user

    )
    cursor = connection.cursor()
    roses = ('avalanche_white','pich_yellow',
            'naomi_red','aqua_pink','penny_yellow',
            'naomi_white','freedom_red')
            
    print('[INFO] DB postgres_scrapper COONECTED')
    for rose in roses:
        cursor.execute(f'DROP TABLE IF EXISTS {rose}')
        connection.commit()
    print('[INFO] ALL CULUMNS DROPPED')
    for rose in roses:
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {rose}
                   (id SERIAL PRIMARY KEY , 
                    shop TEXT,
                    price FLOAT, 
                    date_time TEXT)''')
        connection.commit()
        
    print('[INFO] NEW COLUMNS CREATED')
    return connection


#сделать запись полученных данных в соответсвующие таблицы
def make_record(data,connection):
    data = data.split('|')
    print(data[:-1])
    cursor = connection.cursor()
    current_time = time.asctime()
    roses_names = ('роза аваланш (avalanche)','пич',
             'наоми р','аква','пенни',
             'вайт наоми','роза фридом')
    
    table_names = ['avalanche_white','pich_yellow',
                   'naomi_red','aqua_pink','penny_yellow',
                    'naomi_white','freedom_red']
    for row in data[:-1]:
        row = row.split(',')
        name = row[0]
        for index,rose_name in enumerate(roses_names):
            if name == rose_name:
                cursor.execute(f'''INSERT INTO {table_names[index]} (shop,price,date_time) 
                   VALUES (%s,%s,%s)''',(row[2],row[1],current_time))
                connection.commit()
                print(f'Added to {table_names[index]} table, shop: {row[2]}, price: {row[1]},time: {current_time}')
    return print('DB creation DONE')

def close_connection(connection):
    connection.close()
    print('[INFO] CONECTIONS CLOSED')
