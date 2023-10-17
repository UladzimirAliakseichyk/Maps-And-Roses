import pickle
from pathlib import Path
def write_pickle(data):
    path = Path(Path.cwd(),'venv','flowers_minsk','scrapper','prices_cache.pickle')
    with open(path, 'wb') as cache_file:
        pickle.dump(data,cache_file)
    return print(f'I have made cache for: \n {data}')


def start_cache_procces(connection):
    tables = ('avalanche_white','pich_yellow','naomi_red','aqua_pink','penny_yellow',
                    'naomi_white','freedom_red')
    cursor = connection.cursor()
    min_prices={}
    for table in tables:
        cursor.execute(f'SELECT * FROM {table}')
        row = cursor.fetchall()
        if len(row)>0:
            min_prices[table] = min([float(i[2]) for i in row])
    return write_pickle(min_prices)


            
