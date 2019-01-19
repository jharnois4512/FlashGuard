import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import browser.client


alert_script = "var r = confirm(\"Press a button!\"); if (r == true) { window.location.replace(\"http://www.youtube.com\") } else { alert('Proceed to video') }; console.log(txt);"
browser = webdriver.Chrome(executable_path="/home/brycetherower/PycharmProjects/upgraded-guacamole/browser/chromedriver")
youtube = "https://www.youtube.com/"
browser.get(youtube)
browser.maximize_window()


def pause_vid():
    browser.execute_script(alert_script)
    while 1:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present())
            print("alert is here!")
        except TimeoutException:
            time.sleep(1)
            print("alert is no longer here!")
            break


def browserScraper():
    while 1:
        currentURL = browser.current_url
        try:
            wait = WebDriverWait(browser, 2)
            wait.until(EC.url_changes(currentURL))
            currentURL = browser.current_url
            if "watch?" in currentURL:
                try:
                    video = browser.find_element_by_id("movie_player")
                except WebDriverException:
                    video = browser.find_element_by_id("player")
                client.client_sock(currentURL)
                
                time.sleep(1)
                video.click()
                time.sleep(1)
                pause_vid()

            print ("Different page has been detected")
        except TimeoutException:
            print("SAME PAGE")

browserScraper()
