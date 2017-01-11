import requests
from PIL import Image
from io import BytesIO


def get_image_size(url):
    data=requests.get(url).content
    im=Image.open(BytesIO(data))
    return im.size


url='http://japan.xinhuanet.com/2016-05/30/135394822_14644198712551n.jpg'
width,height=get_image_size(url)
print (width,height)
