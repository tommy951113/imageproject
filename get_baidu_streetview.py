# import requests
# from PIL import Image
# from io import BytesIO
# key = "iSu9UT3xQ1YVNL03ydvVwoOb"
# location = "118.807183,32.063822"
# r = requests.get("http://api.map.baidu.com/panorama/v2?ak=" + key + "&width=1024&height=512&location=" + location + "&fov=360")
# i = Image.open(BytesIO(r.content))
# i.save("streetview2_noparameter.jpg")
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')
plt.title("Equidistant Cylindrical Projection")
plt.show()