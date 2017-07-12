import requests
import urllib
from get_user_id import *
from constants import *
import json
from colorama import *
init()
from PIL import Image

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print Fore.RED+Style.BRIGHT+'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
   # print json.dumps(user_media, indent=4, sort_keys=True)
  #  print user_media['data'][0]['comments'][0]

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            (urllib.urlretrieve(image_url, image_name))
            image = "C:\Users\DELL\PycharmProjects\instabot\\"+image_name
            img = Image.open(image)
            img.show()

            return user_media['data'][0]['id']


        else:
            print Fore.GREEN+Style.BRIGHT+'Post does not exist!'
    else:
        print Fore.RED+Style.BRIGHT+'Status code other than 200 received!'

#get_user_post(insta_username="radhika12344")