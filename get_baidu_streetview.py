import requests
from PIL import Image
from io import BytesIO
key = "iSu9UT3xQ1YVNL03ydvVwoOb"
# location = "118.807183,32.063822"
panoids = ['01002500001405051327290575O','09002500121709191550389036G','09002500011603100854132478D',
'09002500001504280917222851A']
for panoid in panoids:
    r = requests.get("http://api.map.baidu.com/panorama/v2?ak=" + key
    + "&width=1024&height=512&panoid=" + panoid + "&fov=360")
    i = Image.open(BytesIO(r.content))
    i.save(panoid + ".jpg")