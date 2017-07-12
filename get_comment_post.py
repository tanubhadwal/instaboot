import json
import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post
from colorama import *
init()
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def comment_user_post(insta_username):
    media_id = get_user_post(insta_username)
    #print(media_id)
    #  message = raw_input("Enter ur comment....\n")
    # payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    request_url = (BASE_URL + "media/" + media_id + "/comments?access_token=" + APP_ACCESS_TOKEN)
    get_a_comment = requests.get(request_url).json()
    if get_a_comment['meta']['code'] == 200:
        print(Fore.BLUE+Style.BRIGHT+"Here is your recent comment..\n")
        print(Fore.GREEN+Style.BRIGHT+">>> "+get_a_comment['data'][0]['text']+" <<<")
        return(get_a_comment['data'][0]['id'])

        print (Style.RESET_ALL)
    else:
        print(Fore.RED+Style.BRIGHT+'not successful')



#comment_user_post(insta_username="radhika12344")


