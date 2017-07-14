import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post
from colorama import Fore,Style


def comment_user_post(insta_username):
    media_id = get_user_post(insta_username)
 #   print(media_id)
    message = raw_input(Fore.YELLOW+Style.BRIGHT+"Enter ur comment....\n")
    payload = {"access_token" : APP_ACCESS_TOKEN, "text":message}
    request_url = (BASE_URL + "media/" + media_id + "/comments")
  #  print(request_url)
    post_a_comment = requests.post(request_url,payload).json()
   # print 'POST request url : %s' % (request_url)

    #print(post_a_comment['meta']['code'])
    if post_a_comment['meta']['code'] == 200:
        print(Fore.YELLOW+Style.BRIGHT+"Post comment successfully")
    else :
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'not successful')

#comment_user_post(insta_username="royal_khann")


