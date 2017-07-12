import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_comment_post import comment_user_post
from get_user_post import get_user_post
from colorama import *
init()


def delete_a_comment(insta_username):
    comment_id = comment_user_post(insta_username)
    #print comment_id
    media_id = get_user_post(insta_username)
    request_url = BASE_URL+"media/"+media_id+"/comments/"+comment_id+"?access_token="+APP_ACCESS_TOKEN
    delete_comment = requests.delete(request_url).json()
    if delete_comment['meta']['code'] == 200:
        print Fore.GREEN+Style.BRIGHT+'\n...Comment IS deleted....'
    else:
        print Fore.RED+Style.BRIGHT+'Your Deletion of comment  was unsuccessful. Try again!'

#delete_a_comment(insta_username="radhika12344")