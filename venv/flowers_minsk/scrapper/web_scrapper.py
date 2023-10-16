from urllib.request import urlopen
from bs4 import BeautifulSoup
from db_con_rec import creation_db, make_record, close_connection
from make_cache import start_cache_procces
#Подключение к сайтам с розами и получение названий роз и цен 
class WebScrapper:

    def _con_and_parse(self,url,tag_names,class_names,
                           tag_prices,class_prices,shop):
            
        r = urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        names_roses = soup.find_all(tag_names,class_= class_names)
        prices_roses = soup.find_all(tag_prices,class_= class_prices)
        return names_roses, prices_roses, shop
    
    def get_data(self,shop_name):
        if 'rozyminsk' in shop_name:
            url = 'https://rozyminsk.by/catalog/rozy/'
            tag_names = 'div'
            tag_prices = 'div'
            class_names = 'pr_title'
            class_prices = 'price'
            shop = 'rozyminsk.by'
            result = self._con_and_parse(
                        url = url,
                        tag_names=tag_names,
                        class_names=class_names,
                        tag_prices=tag_prices,
                        class_prices=class_prices,
                        shop=shop)
            return result
        
        elif 'розы.бел' in shop_name:
            url = 'https://xn--g1anf0c.xn--90ais/rozy/'
            tag_names = 'h3'
            tag_prices = 'div'
            class_names = 'product-name'
            class_prices = 'price'
            shop = 'розы.бел'
            result = self._con_and_parse(
                        url = url,
                        tag_names=tag_names,
                        class_names=class_names,
                        tag_prices=tag_prices,
                        class_prices=class_prices,
                        shop=shop)
            return result
        
        elif 'яцветы.бел' in shop_name:
            url ='https://xn--b1ag3bn2at.xn--90ais/rozy'
            tag_names = 'a'
            tag_prices = 'span'
            class_names = {'class':'catalogue__product-name products-list__name'}
            r = urlopen(url).read()
            soup = BeautifulSoup(r, "html.parser")
            names_roses = soup.find_all(tag_names,class_names)
            rose_names=[]
            for name in names_roses:
                rose_name = name.find_all('span')
                rose_names.append(rose_name[0])
            class_prices = {'class':'catalogue__price catalogue__price--sm'}
            prices_roses = soup.find_all(tag_prices,class_prices)
            shop = shop_name
            return rose_names,prices_roses,shop
        
        elif 'дорорс' in shop_name:
            shop = 'orsrose.by'
            names_roses = []
            prices_roses = []
            urls = ('https://orsrose.by/rozy/rozovye',
                    'https://orsrose.by/rozy/krasnye',
                    'https://orsrose.by/rozy/zheltye',
                    'https://orsrose.by/rozy/belye'
                    )
            tag_names = 'a'
            class_names = 'product_name'
            tag_prices = 'p'
            class_prices = 'price'

            for url in urls:
                dorors_res = self._con_and_parse(
                            url = url,
                            tag_names=tag_names,
                            class_names=class_names,
                            tag_prices=tag_prices,
                            class_prices=class_prices,
                            shop=shop)
                
                names_roses.extend(dorors_res[0])
                prices_roses.extend(dorors_res[1])
            return names_roses,prices_roses, shop
        
        elif 'daflor' in shop_name:
            names_roses = []
            prices_roses = []
            urls = ('https://daflor.by/catalog/krasnye/',
                    'https://daflor.by/catalog/belye/',
                    'https://daflor.by/catalog/oranzhevye-zheltye/',
                    'https://daflor.by/catalog/rozovye/')

            shop = 'daflor.by'
            tag_names = 'a'
            class_names = 'product_item_name'
            tag_prices = 'div'
            class_prices = 'price'
            for url in urls:
                dorors_res = self._con_and_parse(
                            url = url,
                            tag_names=tag_names,
                            class_names=class_names,
                            tag_prices=tag_prices,
                            class_prices=class_prices,
                            shop=shop)
                
                names_roses.extend(dorors_res[0])
                prices_roses.extend(dorors_res[1])
            return names_roses,prices_roses, shop

    
        


Rose = WebScrapper()

roses_minsk = Rose.get_data('rozyminsk')
roses_bel = Rose.get_data('розы.бел')
roses_imflowers = Rose.get_data('яцветы.бел')
roses_dorors = Rose.get_data('дорорс')
roses_daflor = Rose.get_data('daflor')

#Поиск и фильтрация найденных роз и их цен
def find_rose(names_roses,prices_roses,shop):
    
    roses = ('роза аваланш (avalanche)','пич',
             'наоми р','аква','пенни',
             'вайт наоми','роза фридом')
    
    roses_imflowers = ('роза avalanche', 'роза пич avalanche' ,'роза red naomi')

    roses_daflor = ('розы avalanche','peach',
                    'розы red naoimi',
                    'aqua','penny',
                    'white naomi','freedom')
    
    if shop == 'rozyminsk' or 'розы.бел' or 'orsrose.by':
        data = ''
        for rose in roses:
            for index, name in enumerate(names_roses):
                if rose in name.text.lower():
                    price = prices_roses[index].text
                    price = filter(lambda i: i.isdigit() or i=='.',price)
                    price = ''.join(price)
                    if price[-1] == '.':
                        price = price[:-1]
                    data += f'{rose},{price},{shop}|'
                    break
    if shop == 'яцветы.бел' or 'daflor.by':
        if shop == 'яцветы.бел':
            rose_tpl = roses_imflowers
        elif shop == 'daflor.by':
            rose_tpl = roses_daflor
            data = ''
            for index,rose in enumerate(rose_tpl):
                for index2, name in enumerate(names_roses):
                    if rose in str(name).lower():
                        price = prices_roses[index2].text
                        price = filter(lambda i: i.isdigit() or i=='.',price)
                        price = ''.join(price)
                        data += f'{roses[index]},{price[:-1]},{shop}|'
                        break        
    return data

creation_db()

rm_data = find_rose(names_roses = roses_minsk[0],prices_roses = roses_minsk[1],shop =roses_minsk[2])

rb_data = find_rose(names_roses = roses_bel[0],prices_roses = roses_bel[1],shop =roses_bel[2])

im_data = find_rose(names_roses=roses_imflowers[0],prices_roses=roses_imflowers[1],shop=roses_imflowers[2])

dr_data = find_rose(names_roses=roses_dorors[0],prices_roses=roses_dorors[1],shop=roses_dorors[2])

df_data = find_rose(names_roses=roses_daflor[0],prices_roses=roses_daflor[1],shop=roses_daflor[2])

connection = creation_db()
make_record(rm_data,connection)
make_record(rb_data,connection)
make_record(im_data,connection)
make_record(dr_data,connection)
make_record(df_data,connection)
start_cache_procces(connection)
close_connection(connection)
