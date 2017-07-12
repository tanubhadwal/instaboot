import requests
from constants import *
from get_user_id import *
from colorama import *
init()


def get_user_info(insta_username):
    #function logic here
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    else:
     print 'successfully'
     show== menu_choice

     request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print '\nUsername: %s' % (user_info['data']['username'])
            print '\nNo. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print '\nNo. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print '\nNo. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print Fore.RED+Style.BRIGHT+'There is no data for this user!'
    else:
        print Fore.RED+Style.BRIGHT+'Status code other than 200 received!'
#get_user_info(insta_username="radhika12344")