from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import singleton


def pyorg():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def bbc_firefox():
    driver = webdriver.Firefox()
    driver.get("http://www.bbc.com/")
    elem = driver.find_element_by_name("q")
    if elem.is_displayed():
        print("Yeah, on display")
        print('IsDisplayed = ' + str(elem.is_displayed()))
    else:
        print("Can't see that elem")
    elem.send_keys("Belarus")
    if elem.is_enabled():
        print("Ohh, rly enabled")
        print('IsEnabled = ' + str(elem.is_enabled()))
    elem.send_keys(Keys.RETURN)
    elem2 = driver.find_element_by_tag_name('a')
    # to main page
    elem2.click()
    time.sleep(10)
    driver.close()


def bbc_chrome():
    driver = webdriver.Chrome()
    driver.get("http://www.bbc.com/")
    elem = driver.find_element_by_name("q")
    elem.send_keys("Belarus")
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.close()


def main():
    # bbc_chrome()
    bbc_firefox()


if __name__ == '__main__':
    main()
