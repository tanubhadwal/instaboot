#.....................ALL FILES ARE IMPORTED HERE................
from like_user_post import like_user_post
from comment_a_Post import comment_user_post
from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info
from delete_a_comment import delete_a_comment
import get_comment_post
from delete_a_bad_comment import delete_negative_comment
from colorama import init
from colorama import Fore,Back,Style
init()
from trending import get_trending_tag_counts

#.....................STARTING MENU BAR......................
show_menu = True
while show_menu:

    #.........................WELCOME........NOTE............................
    print(Fore.GREEN+Style.BRIGHT+'.....................Welcome ....TO......InstaBot..............')
    print(Fore.YELLOW+Style.BRIGHT+"\n...................MAke...... Your... Life.. Easy............\n\n")
    menu_choices = Fore.CYAN+Style.BRIGHT+"What do you want to do? \n 1. Like A Post \n 2. Comment on a post \n 3. Download Own Post \n 4. Download Friend's post \n 5. Get Friend Info. \n 6. Get Friend's comments\n 7. Count ur Tag Popularity\n 8. Delete a Comment\n 9. Delete a bad comments.\n"
    Style.RESET_ALL
    menu_choice = input(menu_choices)

#............................CHOICE MENU IS HERE..................................

    if (menu_choice) > 0:
        menu_choice = int(menu_choice)
#.....................LIKE POST.............................
        if menu_choice == 1:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait liking Ur POst......")
            like_user_post(insta_username)
            print(Style.RESET_ALL)
            print("\n")
            print("\n")
#.......................COMMENT ON A POST.....................
        elif menu_choice == 2:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"wait work under process.......")
            comment_user_post(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
#......................DOWNLOAD POST...........................
        elif menu_choice == 3:
            print (Fore.GREEN+Style.BRIGHT+"WAit Getting ur post.......\n")
            get_own_post()
            print 'Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot\\'
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
#.......................DOWNLOAD FRIEND POST.......................
        elif menu_choice == 4:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait Downloading user post......")
            get_user_post(insta_username)
            print get_user_post.user_id['data'][0['id']]
            print 'Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot\\'
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
#........................GET USER INFORMATION..........................
        elif menu_choice == 5:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait getting information.....")
            get_user_info(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
#.......................GET RECENT COMMENTS...................
        elif menu_choice == 6:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print("\n"+Fore.GREEN+Style.BRIGHT+"Wait getting information.....\n")
            get_comment_post.comment_user_post(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
#...................GET TRENDING TAG........................
        elif menu_choice == 7:
            tag = raw_input(Fore.RED+Style.BRIGHT+"Enter Tagname.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait counting Ur Tags......")
            get_trending_tag_counts(tag)
            print(Style.RESET_ALL)
            print("\n")
            print("\n")
#...................DELETE THE COMMENT......................
        elif menu_choice == 8:
            insta_username = raw_input(Fore.RED + Style.BRIGHT + "Enter Username.........\n")
            print("\n" + Fore.GREEN + Style.BRIGHT + "Wait getting information.....\n")
            delete_a_comment(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
            #.......DELETE.NEGATIVE..COMMENT.....
        elif menu_choice == 9:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"wait work under process.......")
            delete_negative_comment(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        else:
            show_menu = False