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
        print"User does not Exist"

        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print'GET request url for user post:%s' %( request_url)

    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        # Here we can extract post ID





        if len(user_media['data']):

            image_name = user_media['data'][0]['id'] + '.jpeg'

            image_url = user_media['data'][0]['images']['standard_resolution']['url']

            urllib.urlretrieve(image_url, image_name)

            print'Your image has been downloaded!'
            return user_media['data'][0]['id']


        else:

            print'There is no recent post!'



    else:

        print"Status code other than 200 recevied!"
#get_user_post(insta_username="radhika12344")
def get_user_post_id(insta_username):
    user_id = get_user_id(insta_username)

    if user_id == None:
        print"User does not Exist"

        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print'GET request url for user post:%s' %( request_url)

    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        # Here we can extract post ID





        if len(user_media['data']):


            return user_media['data'][0]['id']


        else:

            print'There is no recent post!'



    else:

        print"Status code other than 200 recevied!"