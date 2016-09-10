import requests
import json

from settings import API_KEY


def order_online(lat, lon):
    url = "https://developers.zomato.com/api/v2.1/geocode?lat={0}&lon={1}".format(lat, lon)
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": API_KEY}

    resp = requests.get(url, headers=header)
    resp_status = resp.status_code
    if resp_status == 200:
        get_data = json.loads(resp.text)
        for i in get_data['nearby_restaurants']:
            name = i['restaurant']['name']
            menu_url = i['restaurant']['menu_url']
            locality = i['restaurant']['location']['locality']
            cost = i['restaurant']['average_cost_for_two']
            print("Visit this url to check menu of {0}, {1} where cost for two is {2}: {3}" \
                .format(name, locality, cost, menu_url))
    else:
        raise Exception(resp_status)


if __name__ == "__main__":
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    order_online(lat, lon)
