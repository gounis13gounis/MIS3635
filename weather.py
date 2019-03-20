weather={'coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 277.23, 'pressure': 1028, 'humidity': 35, 'temp_min': 275.93, 'temp_max': 278.15}, 'visibility': 16093, 'wind': {'speed': 5.7, 'deg': 290}, 'clouds': {'all': 75}, 'dt': 1553011422, 'sys': {'type': 1, 'id': 5255, 'message': 0.0086, 'country': 'US', 'sunrise': 1552992638, 'sunset': 1553036120}, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}

weather["main"]["temp"]-273.15

import pprint
pprint.pprint(weather["main"])