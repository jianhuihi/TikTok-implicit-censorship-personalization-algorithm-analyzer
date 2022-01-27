import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def watch_and_continue(start_url, se_driver: webdriver, no_videos, like_prob=0):
    url = start_url
    urls = [start_url]
    for i in range(no_videos):
        like = random.uniform(0, 1) < like_prob
        url = watch_tiktok(url, se_driver, like)
        urls.append(url)
    return urls


def watch_tiktok(url, se_driver: webdriver, like=False):
    se_driver.get(url)
    _wait_tiktok_to_load(se_driver)
    time.sleep(_get_duration(se_driver) + 2)  # wait until video has certainly played
    if like:  # Then maybe interact
        se_driver.send_keys('L')
    se_driver.send_keys(Keys.DOWN)
    return se_driver.current_url


def _wait_tiktok_to_load(se_driver: selenium.webdriver):
    page_state = se_driver.execute_script('return document.readyState;')
    while page_state != 'complete':
        time.sleep(0.1)  # 100 ms
    return


def _get_video(se_driver: webdriver):
    return se_driver.find_element_by_css_selector("[class*='VideoBasic']")


def _get_duration(se_driver: webdriver):
    return se_driver.execute_script("document.querySelectorAll('[class*=\"VideoBasic\"]')[0].duration")
