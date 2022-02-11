import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def watch_and_continue(start_url, se_driver: webdriver, no_videos, like_prob=0):
    url = start_url
    se_driver.get(url)
    urls = [start_url]
    for i in range(no_videos):
        like = random.uniform(0, 1) < like_prob
        url = _watch_tiktok(url, se_driver, like)
        urls.append(url)
    return urls


def watch_tiktok(url, se_driver: webdriver, like=False):
    se_driver.get(url)
    return _watch_tiktok(url, se_driver, like)


def _watch_tiktok(url, se_driver: webdriver, like=False):
    _wait_tiktok_to_load(se_driver)
    print("Loaded " + url)
    duration = _get_duration(se_driver)
    while duration is None:
        duration = _get_duration(se_driver)
    print(duration)
    time.sleep(duration)  # wait until video has certainly played
    chain = ActionChains(driver=se_driver)
    if like:  # Then maybe interact
        chain.send_keys('L')
        random_pause = random.uniform(0, 1) + 0.5  # Add some randomness to avoid bot detection
        chain.pause(random_pause)
    print("Next...")
    chain.send_keys(Keys.SPACE)
    chain.perform()
    time.sleep(1)
    return se_driver.current_url


def _wait_tiktok_to_load(se_driver: webdriver):
    page_state = se_driver.execute_script('return document.readyState;')
    while page_state != 'complete':
        time.sleep(0.1)  # 100 ms
    return


def _get_video(se_driver: webdriver):
    return se_driver.find_element_by_css_selector("[class*='VideoBasic']")


def _get_duration(se_driver: webdriver):  # Legacy / fallback when api does not work
    return se_driver.execute_script("return document.querySelectorAll('[class*=\"VideoBasic\"]')[0].duration")
