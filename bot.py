
#the code is hosted on github.com/engineervinay if you wanted to make development in code visit profile and fork the code
#if you have any query related to this code you can contact me on github @engineervinay



from selenium.webdriver.common.keys import Keys #importing keys from selenium to enter the comments

from time import sleep #time library for sleepcommand

from random import randint #library to provide random integer values between range

from selenium import webdriver as wb #the library for accesing chrome by our code


def read_config(filename):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    user = config['user']['user']
    passw = config['user']['passw']

    hash = config['hashtag']['hash']

    target_url = config['url']['target_url']
    driver_url = config['url']['driver_url']

    notnow_path = config['path']['notnow_path']
    login_path = config['path']['login_path']
    tag_path = config['path']['tag_path']
    first_thumbnail_path = config['path']['first_thumbnail_path']
    button_like_path = config['path']['button_like_path']
    comment_path = config['path']['comment_path']
    comment_box_path = config['path']['comment_box_path']
    next_path_1 = config['path']['next_path_1']
    next_path_2 = config['path']['next_path_2']
    return [user, passw, hash, target_url, driver_url, login_path, notnow_path, tag_path, first_thumbnail_path, button_like_path, comment_path, comment_box_path, next_path_1, next_path_2]

def generate_comment():
    comm_prob =randint(0,3)
    comments = ['Great work!', 'So Cool!', 'I love your post', 'Nice!']
    return comments[comm_prob]

def check_existence(webdriver, xpath):
    from selenium.common.exceptions import NoSuchElementException        
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def main():
    user, passw, hash, target_url, driver_url, login_path, notnow_path, tag_path, first_thumbnail_path, button_like_path, comment_path, comment_box_path, next_path_1, next_path_2 = read_config('inst.ini')


    # Change this to your own chromedriver path!
    chromedriver_path = driver_url
    webdriver = wb.Chrome(executable_path=chromedriver_path)

    sleep(2)
    #opening instagram login page.
    webdriver.get(target_url)
    sleep(3)


    webdriver.find_element_by_name('username').send_keys(user)#finding username inputbox
    webdriver.find_element_by_name('password').send_keys(passw)

    #finding login button 
    login = webdriver.find_element_by_css_selector(login_path)
    login.click()
    sleep(3)


    #clicking on not now button which occurs when we logged in
    notnow = webdriver.find_element_by_css_selector(notnow_path)
    notnow.click()

    hashtag_list=hash.split(",")
    for hashtag in hashtag_list:

        sleep(5)
        webdriver.get(tag_path + hashtag + '/')
        sleep(5)

        first_thumbnail = webdriver.find_element_by_xpath(first_thumbnail_path)
        first_thumbnail.click()
        sleep(randint(1, 2))

        for x in range(1, 200):
            #username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            #if username not in prev_user_list:
            # If we already follow, do not unfollow

            #if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

            #webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

            #new_followed.append(username)

            #followed += 1

            # Liking the picture
            sleep(randint(3,7))
            #finding the like button using xpath
            button_like = webdriver.find_element_by_xpath(button_like_path)
            button_like.click()

            #to enable commenting box
            webdriver.find_element_by_xpath(comment_path).click()
            #clicking on comment box
            comment_box = webdriver.find_element_by_xpath(comment_box_path)
            sleep(randint(3,7))
            #code to post random comments
            comment_box.send_keys(generate_comment())
            sleep(5)

                    
            sleep(randint(4,6))
            comment_box.send_keys(Keys.ENTER)# Enter to post comment
            sleep(randint(22, 28))

            if check_existence(webdriver, next_path_2):
                webdriver.find_element_by_xpath(next_path_2).click()#clicking on next for next photo
            else:
                webdriver.find_element_by_xpath(next_path_1).click()

            sleep(randint(25, 29))


if __name__ == '__main__':
    main()