import psycopg2
import folium
from scrapper import db_conf_scrapper
from folium.features import DivIcon
from map_config import *
import pickle
from pathlib import Path


def db_connection(table):
    connection = psycopg2.connect(
        database = db_conf_scrapper.database,
        password = db_conf_scrapper.password,
        host = db_conf_scrapper.host,
        user = db_conf_scrapper.user
        )
    cursor = connection.cursor()
    cursor.execute(f'SELECT shop,price FROM {table}')
    res = cursor.fetchall()
    connection.close()
    return res 
    
def folium_marker(location,price,fill):
    marker = folium.Marker(
        popup=location[2],
        location= location[:2],
        icon=DivIcon(
        icon_size=(60,36),
        icon_anchor=(0,0),
        html=f"""<div style="font-size: 16pt; color: white">
        <g>
        <svg>
        <rect width="90" height="30" fill={fill} opacity=".9" rx="15"/>
        <text x="10" y="20" font-family="Verdana" font-size="16" fill="white">{price} руб.</text>
        </g>
        </svg></div>""")    )
    return marker
def create_map(rose_name):
    data = db_connection(rose_name)
    map = folium.Map(location=[53.9, 27.5667],zoom_start=12)
    
    for row in data:
        shop = row[0]
        price = row[1]
        if shop == 'rozyminsk.by':
            fill = "orange"
            for location in rozyminsk_locations:
                marker = folium_marker(location,price,fill)
                marker.add_to(map)
        elif shop == 'daflor.by':
            fill = "green"
            for location in daflor_loactoins:
                marker = folium_marker(location,price,fill)
                marker.add_to(map)
        elif shop == 'розы.бел':
            fill = "blue"
            for location in rosesbel_locations:
                marker = folium_marker(location,price,fill)
                marker.add_to(map)
        elif shop == 'orsrose.by':
            fill = 'fuchsia'
            for location in orsrose_locations:
                marker = folium_marker(location,price,fill)
                marker.add_to(map)
        elif shop == 'яцветы.бел':
            fill = 'purple'
            for location in imflowers_locations:
                marker = folium_marker(location,price,fill)
                marker.add_to(map)
    
    context = {'map':map._repr_html_()}  
    return context


def get_from_pickle():
    path = Path(Path.cwd(),'scrapper','prices_cache.pickle')
    with open(path, 'rb') as data:
        data = pickle.load(data)
    return data

get_from_pickle()