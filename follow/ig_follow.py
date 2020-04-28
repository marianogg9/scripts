import pandas as pd
import sys
import argparse
from selenium import webdriver
from time import sleep, strftime
from random import randint

def get_options():
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument("-a", "--hashtag", type=str, help="Hashtag(s) to query. More than one? just concatenate them as a list of comma separated words.")
    parser.add_argument("-d", "--path", type=str, help="Web driver full path.", default='path:/chromedriver')
    parser.add_argument("-u", "--username", type=str, help="Instagram account username to use.")
    parser.add_argument("-p", "--password", type=str, help="Instagram account password.")
    parser.add_argument("-n", "--num", type=int, help="How many photos to loop through.")
    options = parser.parse_args()
    return options

def get_driver(options):
    driver_path = options.path
    driver = webdriver.Chrome(executable_path=driver_path)
    sleep(2)
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
    return driver

def login(options,driver):
    username = driver.find_element_by_name('username')
    username.send_keys(options.username)
    password = driver.find_element_by_name('password')
    password.send_keys(options.password)

    button_login = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
    button_login.click()
    sleep(3)

    # these two lines will get rid of the notifications popup (Not now)
    notnow = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()

def follow(options, driver):
    hashtag_list = (options.hashtag).split(",")

    prev_user_list = [] # this one is for the first run. On the following, you could get an activity log csv
    # prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,
    #                 1:2]  # useful to build a user log
    # prev_user_list = list(prev_user_list['0'])

    new_followed = []
    tag = -1
    followed = 0
    likes = 0

    for hashtag in hashtag_list:
        tag += 1
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(5)
        first_thumbnail = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click()
        sleep(randint(1, 2))
        try:
            for x in range(1, options.num):
                username = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

                if username not in prev_user_list:
                    # If we already follow, do not unfollow
                    if driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        follow_button = driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')

                        follow_button.click()
                        new_followed.append(username)
                        followed += 1

                        # Liking the picture
                        button_like = driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')

                        button_like.click()
                        likes += 1
                        sleep(randint(18, 25))

                    # Next picture
                    driver.find_element_by_link_text('Next').click()
                    sleep(randint(25, 29))
                else:
                    driver.find_element_by_link_text('Next').click()
                    sleep(randint(20, 26))
        # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except Exception as e:
            print(e)
            continue

    for n in range(0, len(new_followed)):
        prev_user_list.append(new_followed[n])

    updated_user_df = pd.DataFrame(prev_user_list)
    updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
    print('Liked {} photos.'.format(likes))
    print('Followed {} new people.'.format(followed))

def main():
    options = get_options()
    driver = get_driver(options)
    login(options,driver)
    follow(options,driver)

if __name__ == '__main__':
    main()
