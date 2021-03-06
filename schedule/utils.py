import json
from xml.etree import ElementTree
import requests
import xmljson
import pdb
from random import *

def get_gecode(location):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'
                            + 'address=' + location + '%20'
                            + '&%20key=AIzaSyCi3Cz6Q1Uu6ftxqyXYv7djfhgxqN9eaMA', )
    result = json.loads(response.text)
    result_location = result['results'][0]['geometry']['location']
    lat = result_location['lat']
    lng = result_location['lng']
    print(lat, lng)


def get_micro_dust(location):
    response = requests.get(
        f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=&numOfRows=10&pageSize=10&pageNo=1&startPage=1&stationName={location}&dataTerm=DAILY&ver=1.3'
    )
    result_lxml = ElementTree.fromstring(response.text)
    result_json = json.loads(json.dumps(xmljson.badgerfish.data(result_lxml)))
    print (location)
    result_json_item = result_json['response']['body']['items']['item']

    return result_json_item[0]['pm25Value']['$'] + randint(1, 5)
