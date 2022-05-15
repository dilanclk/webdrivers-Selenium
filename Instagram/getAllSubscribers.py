from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
loginButton.click()
time.sleep(5)

profile_select = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]")
profile_select.click()
time.sleep(5)

profileButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]")
profileButton.click()
time.sleep(10)

buttons = browser.find_elements_by_css_selector(".Y8-fY")
followersButton = buttons[1]
followersButton.click()
time.sleep(10)


jscommand = """
followers =document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()
