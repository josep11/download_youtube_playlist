from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import mybrowser
from myfile import write_file
from myfile import read_file
# import pprint
from colorama import init, Back  # ,Fore
import time


class SimpleClass(object):
    pass

videos = SimpleClass()
init()

urlPlayList = """https://www.youtube.com/watch?v=74Wei0-vAZs&list=PL-bTaZrTDhtb
hxgS59t4HzwCnq2iIYMgV""".replace('\n', '')

# print(urlPlayList)
urlBase = 'http://www.downvids.net/download-youtube-playlist-videos'


browser = mybrowser.initBrowser()
# browser = webdriver.PhantomJS()
browser.get(urlBase)
# browser.implicitly_wait(1)  # esperar si elements no available immediatament


def printElement(element, trimLength=None):  # WebElement
    if element is None:
        print(Back.RED + "NULL element" + Back.BLACK)
        return

    html = element.get_attribute('innerHTML')
    print(Back.CYAN)
    if trimLength:
        print(html[:trimLength])
    else:
        print(html)
    # print(element.text + " " + element.tag_name)
    print(Back.BLACK)
    # print(username.parent)
    # print(username.tag_name)
    # print(username.text)
    # print(username.value_of_css_property)


def find_by_xpath(locator):
    try:
        element = browser.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
    except TimeoutException:
        print(Back.RED + "TimeoutException buscant Login" + Back.BLACK)
        return None
    return element


def find_el_by_text(text):
    # print('Buscant ...')
    # print("//*[contains(.,'%s')" % text)
    return find_by_xpath("//*[contains(.,'%s')]" % text)


def searchPlaylist(urlPlayList):
    searchForm = browser.find_element_by_id('home_search_q')
    submit = browser.find_element_by_id('home_search_submit')
    time.sleep(3)
    # submit = browser.find_element_by_xpath('//*[@id="login-form"]/div/input')
    searchForm.send_keys(urlPlayList)

    submit.click()

searchPlaylist(urlPlayList)


def printArrayElements(urls):
    if not len(urls):
        print("ERROR")
        return

    print(len(urls))

    for i in range(0, len(urls)):
        print(urls[i])


def extractUrlToDownload(trial=0):
    global urls
    # urls = browser.find_elements_by_xpath('//*[@id="search_more"]')
    # print("by xpath")
    # printArrayElements(urls)
    if trial > 3:
        raise

    # print("as video")
    elements = browser.find_elements_by_partial_link_text('as video')
    if not len(elements):
        trial = trial + 1
        extractUrlToDownload(trial)
    else:
        urls = list(map(lambda el: el.get_attribute('href'), elements))
        # print('\n'.join(urls))


def extractVideoNames(trial=0):
    global videoNames

    if trial > 3:
        raise

    elements = browser.find_elements_by_class_name('msgtxt')
    if not len(elements):
        trial = trial + 1
        extractUrlToDownload(trial)
    else:
        videoNames = list(map(lambda el: el.text, elements))

extractUrlToDownload()
extractVideoNames()

if len(videoNames) != len(urls):
    raise Exception('No sa parsejat bé els títols o les urls dels vídeos')

# print('\n'.join(videoNames))
# print('\n'.join(urls))

write_file(zip(videoNames, urls))

# print(list(dictionary))

# print(Back.GREEN)
# element = browser.find_element_by_css_selector(
#     '.filters > td:nth-child(1) > input:nth-child(1)')
# salir = browser.find_element_by_link_text('Salir')

# element.send_keys('100')
# # time.sleep(0.5)
# element.send_keys(Keys.ENTER)
# print(Back.BLACK)

# printElement(salir)
# printElement(element)

# print '\n'.join(map(str,dir(browser)))
if False:
    if not browser.title:
        print('browser title not set')

    # assert 'nutrikabi' in browser.title

    print(browser.title)

# browser.get_screenshot_as_file('prova.png')
# time.sleep(5)
browser.quit()
