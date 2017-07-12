import requests
from constants import *
import urllib
from colorama import *
from PIL import Image


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
   # print 'GET request url : %s' %(request_url)
    own_media = requests.get(request_url).json()
    print own_media
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            image = "C:\Users\DELL\PycharmProjects\instabot\\" + image_name


            print("\n\n")

        else:
            print Fore.RED+Style.BRIGHT+'Post does not exist!'
    else:
        print Fore.RED+Style.BRIGHT+'Status code other than 200 received!'

#get_own_post()