import requests
from PIL import Image
from io import BytesIO
key = "iSu9UT3xQ1YVNL03ydvVwoOb"
# location = "118.807183,32.063822"
url = "http://api.map.baidu.com/panorama/v2?ak="
panoids = ['09000600121706201415155184A']
# r = requests.get(url+key+"&width=1024&height=512&panoid=09002500121709071630027646O&fov=360")
# print(r.content)
for panoid in panoids:
    r = requests.get("http://api.map.baidu.com/panorama/v2?ak=" + key
    + "&width=1024&height=512&panoid=" + panoid + "&fov=360")
    i = Image.open(BytesIO(r.content))
    i.save("images/" + panoid + ".jpg")