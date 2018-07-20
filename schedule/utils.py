import json
from xml.etree import ElementTree

import requests
import pdb

import xmljson


def get_gecode(location):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'
                            + 'address=' + location + '%20'
                            + '&%20key=AIzaSyCi3Cz6Q1Uu6ftxqyXYv7djfhgxqN9eaMA', )

    # pdb.set_trace()
    result = json.loads(response.text)
    result_location = result['results'][0]['geometry']['location']
    lat = result_location['lat']
    lng = result_location['lng']
    print(lat, lng)


def get_micro_dust(location):
    service_key = '8Y859478tjmmk8A2oYZjUSRYq%2B8ODakvkBAMuvzGx%2FOIrPCIxjDQ6CHS4GNmdLofIxLoAb8sfCb%2F0c4zLJVuNA%3D%3D'
    q = {
        'serviceKey': service_key,
        'numOfRows': 10,
        'pageSize': 10,
        'pageNo': 1,
        'startPage': 1,
        'dataTerm': 'DAILY',
        'ver': 1.0,
        'stationName': location,
    }
    # response = requests.get(
    #     "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty",
    #     params=q)
    response = requests.get(
        f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=8Y859478tjmmk8A2oYZjUSRYq%2B8ODakvkBAMuvzGx%2FOIrPCIxjDQ6CHS4GNmdLofIxLoAb8sfCb%2F0c4zLJVuNA%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1&stationName={location}&dataTerm=DAILY&ver=1.3'
    )
    result_lxml = ElementTree.fromstring(response.text)
    result_json = json.loads(json.dumps(xmljson.badgerfish.data(result_lxml)))
    result_json_item = result_json['response']['body']['items']['item']

    # 캘린더 시간이랑 비교할 것
    for dataTime in result_json_item:
        print(dataTime['dataTime']['$'])

    # get_gecode('강남구')
get_micro_dust('강남구')
