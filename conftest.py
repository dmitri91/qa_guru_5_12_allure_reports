import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def web_browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://github.com/'
    yield browser
    browser.quit()
