from selenium import webdriver
import loginInfo
import time


browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

log_in = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/form/div[3]/div/p/a")

log_in.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

# This allows us to enter data in the input field. We get the data from the file we created before to be able to log in here.
username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)


login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")

login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='search-query']")
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")



searchArea.send_keys("#aaaaaaaaaa")

searchButton.click()

time.sleep(5)

# The scroll code allows us to go to the bottom of the page. The process scrolls until there are no more pages to refresh.
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

# It allows us to retrieve all tweets after the Scoll process is finished.
elements = browser.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")


for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("There is a problem...")


browser.close()
