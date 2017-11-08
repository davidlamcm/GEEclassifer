from io import BytesIO
from PIL import Image
from urllib import request
import matplotlib.pyplot as plt # this is if you want to plot the map using pyplot

url = "http://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center=22.31129,113.935106&size=800x800&zoom=18&sensor=false"

buffer = BytesIO(request.urlopen(url).read())
image = Image.open(buffer)

# Show Using PIL
image.show()

# Or using pyplot
plt.imshow(image)
plt.show()
