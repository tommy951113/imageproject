# import streetview
# panoids = streetview.panoids(lat=-33.85693857571269, lon=151.2144895142714)
# print(panoids)

# import requests

# proxies = {
#     "http": "socks5://127.0.0.1:1080",
#     'https': 'socks5://127.0.0.1:1080'
# }

# r=requests.get("https://www.google.com", proxies=proxies)
# print(r.text)
import requests
from PIL import Image
from io import BytesIO

coordinates = "32.041586,118.786540"
web_service = "https://apis.map.qq.com/ws/streetview/v1/getpano"
radius = 100
key = "4QVBZ-2YNLO-JZNWX-SALX6-BKVSH-VBFUX"
url = web_service + "?location=" + coordinates + "&radius=" + str(radius) + "&key=" + key
r = requests.get(url)
id = r.json()['detail']['id']
pano_service = "https://apis.map.qq.com/ws/streetview/v1/image"
size = "600x300"
pitch = -60
heading = 180
url_pano = pano_service + "?pano=" + id + "&size=" + size + "&pitch=" + str(pitch) + "&heading=" + str(heading) + "&key=" + key
r = requests.get(url_pano)
i = Image.open(BytesIO(r.content))
i.save("streetview_nanjing3.jpg")