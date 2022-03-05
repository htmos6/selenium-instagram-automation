import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def follower_list():
    s = Service('enter-your-path-of-geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get('https://www.instagram.com/accounts/login/')

    username = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
    password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

    username.send_keys('enter-your-username')
    password.send_keys('enter-your-password')
    time.sleep(2)
    driver.implicitly_wait(10)

    login_button = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")
    driver.implicitly_wait(10)
    login_button.click()

    profile_icon = driver.find_element(By.CSS_SELECTOR, "._2dbep.qNELH")
    driver.implicitly_wait(10)
    time.sleep(2)
    profile_icon.click()

    profile = driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div")
    driver.implicitly_wait(10)
    time.sleep(2)
    profile.click()

    following_list = driver.find_elements(By.CSS_SELECTOR, ".Y8-fY")
    following_people = following_list[2]
    driver.implicitly_wait(10)
    time.sleep(2)
    following_people.click()

    #javascript integrated code to python-selenium
    js_script = """
    followers = document.querySelector(".isgrP");
    followers.scrollTo(0, followers.scrollHeight);
    var lenOfPage = followers.scrollHeight;
    return lenOfPage;  
    """

    lenOfPage = driver.execute_script(js_script)
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(2)
        lenOfPage = driver.execute_script(js_script)
        if lastCount == lenOfPage:
            match=True
    time.sleep(5) # to load page contents entirely

    followed_by_me_list = []
    users = driver.find_elements(By.CSS_SELECTOR, "._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")

    for user in users:
        followed_by_me_list.append(user.text)

    ct = 1
    with open("following_people.txt",'w',encoding='utf-8') as file:
        for user in followed_by_me_list:
            file.write(str(ct)+". "+user+"\n")
            ct += 1

    driver.close()

if __name__ == "__main__":
    follower_list()

